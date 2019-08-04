import json

from util.logger import Logger

from google.cloud import datastore

from . import dbconsts
from .dataprocessor import DatastoreProcessor

import threading


class DatastoreManager:

    log = Logger("DatastoreManager")

    # dbconst.MAX = 100

    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        # log = Logger("DatastoreManager")
        self.log.debug('Initialize')

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                return cls._instance

    def generate_song_id(self, arg):
        self.log.debug('generate_song_id')

        # TODO
        return arg

    def get_song_data(self):
        self.log.debug('get_song_data')
        # self.log.debug(dbconsts.MASTER_KIND.TITLE)
        return
        # self.log.debug('get_song_data')

    # def create_data(self, song_id):

    #     self.log.debug('create_data')

    #     client = datastore.Client()
    #     key = client.key(dbconsts.SONG.KIND_NAME, song_id)
    #     entity = datastore.Entity(key=key)
    #     entity[dbconsts.PROPERTY_NAME] = "Electone user"
    #     entity[dbconsts.PROPERTY_THUMBNAIL_URL] = "https://xxxx.com"
    #     client.put(entity)

    #     return

    # def get_category_content(self, video_id):
    #     self.log.debug('get_category_content')

    #     client = datastore.Client()
    #     key = client.key(dbconsts.KIND_SONG, video_id)

    #     return

    def get_latest_data(self):
        self.log.debug('get_latest_data')

        client = datastore.Client()
        query = client.query(kind=dbconsts.SONG.KIND_NAME)
        entities = list(query.fetch())

        jsonobj = {"contents": []}
        # latest_contents = {}

        for entity in entities:

            processor = DatastoreProcessor()
            content = processor.convert_entity_to_json(entity)
            # content = processor.convert_entity_to_contentdata(entity)
            # self.log.debug(json.dumps(content))
            # latest_contents.append(content)
            jsonobj["contents"].append(content)

            # self.log.debug(jsonobj)

        return json.dumps(jsonobj)

    def get_data(self, song_id):

        self.log.debug('get_data')

        client = datastore.Client()
        key = client.key(dbconsts.SONG.KIND_NAME, song_id)
        entity = client.get(key)

        data_processor = DatastoreProcessor()
        return data_processor.convert_entity_to_contentdata(entity)

    def is_new_content(self, key):

        client = datastore.Client()
        if client.get(key) is not None:
            self.log.debug('Content already exist')
            return False
        else:
            self.log.debug('New Content')
            return True

    def store_contents(self, content):
        self.log.debug('store_contents')

        client = datastore.Client()

        key = client.key(dbconsts.SONG.KIND_NAME, content.get_song_id())

        if self.is_new_content(key):

            entity = datastore.Entity(
                key=key, exclude_from_indexes=(dbconsts.SONG.CONTENTS,))
            entity[dbconsts.SONG.REP_TITLE] = content.get_title()
            entity[dbconsts.SONG.REP_DESCRIPTION] = content.get_description()
            entity[dbconsts.SONG.REP_PUBLISH_DATE] = content.get_publish_date()
            entity[dbconsts.SONG.REP_THUMB_URL] = content.get_thumbnail_url()
            entity[dbconsts.SONG.REP_CHANNEL_TITLE] = content.get_channel_title()
            entity[dbconsts.SONG.REP_VIDEO_ID] = content.get_video_id()
            entity[dbconsts.SONG.KEYWORD] = content.get_keyword()
            entity[dbconsts.SONG.DIFFICULTY] = content.get_difficulty()
            entity[dbconsts.SONG.FAMOUS] = content.get_famous()
            entity[dbconsts.SONG.CONCERT] = content.get_concert()
            entity[dbconsts.SONG.CONTENTS] = content.get_mini_content()

            client.put(entity)

    def get_category_contents(self, video_id):
        self.log.debug('get_category_contents')
        client = datastore.Client()
        key = client.key(dbconsts.SONG.KIND_NAME, video_id)
        entity = client.get(key)

    # Difficulty
    def get_contents_by_difficulty(self, min, max):
        self.log.debug('get_concents_by_difficulty')
        client = datastore.Client()

        start = client.key(dbconsts.DIFFICULTY.KIND_NAME, min)
        endend = client.key(dbconsts.CONCERT.KIND_NAME, max)

        query = client.query(kind=dbconsts.DIFFICULTY.KIND_NAME)

        query.key_filter(start, '>=')
        query.key_filter(end, '<')

        return

    def put_contents_with_property(self, jsonObj):
        self.log.debug('put_contents_with_property')

        client = datastore.Client()

        difficulty_list = jsonObj["difficulty"]
        concert_list = jsonObj["concert"]
        famous_list = jsonObj["famous"]

        self.log.debug(difficulty_list)
        self.log.debug(concert_list)
        self.log.debug(famous_list)

        self.store_property(
            client, dbconsts.DIFFICULTY.KIND_NAME, difficulty_list)
        self.store_property(client, dbconsts.CONCERT.KIND_NAME, concert_list)
        self.store_property(client, dbconsts.FAMOUS.KIND_NAME, famous_list)

    def store_property(self, client, kind_name, property_list):
        self.log.debug('store_property')

        for i in range(len(property_list)):

            contents = property_list[str(i)]

            if len(contents) is not 0:
                key = client.key(kind_name, str(i))
                entity = client.get(key)

                # If entity for content already exist
                if entity is not None and len(entity[dbconsts.SONG.CONTENTS]) is not 0:
                    content_list_json = entity[dbconsts.SONG.CONTENTS]
                    for j in range(len(contents)):
                        content_list_json.append(contents[j])
                    client.put(entity)
                else:
                    # Otherwise (New Entity for this property)
                    entity_new = datastore.Entity(key=key)
                    entity_new[dbconsts.SONG.CONTENTS] = contents
                    client.put(entity_new)

    def get_content_by_property(self, properties):
        self.log.debug('get_content_by_property')

        obj = json.loads(properties)
        difficulty = obj['difficulty']
        concert = obj['concert']
        famous = obj['famous']

        client = datastore.Client()
        diff_list = []
        concert_list = []
        famous_list = []

        output_list = []
        jsonobj = {"contents": []}

        # key_diff = client.key(dbconsts.KIND_DIFFICULTY, str(difficulty))
        key_diff = client.key(dbconsts.DIFFICULTY.KIND_NAME, str(difficulty))
        entity_diff = client.get(key_diff)
        if diff_list is not None:
            diff_list = entity_diff[dbconsts.SONG.CONTENTS]

        key_concert = client.key(dbconsts.CONCERT.KIND_NAME, str(concert))
        entity_concert = client.get(key_concert)
        if entity_concert is not None:
            concert_list = entity_concert[dbconsts.SONG.CONTENTS]

        key_famous = client.key(dbconsts.FAMOUS.KIND_NAME, str(famous))
        entity_famous = client.get(key_famous)
        if entity_famous is not None:
            famous_list = entity_famous[dbconsts.SONG.CONTENTS]

        for i in range(len(diff_list)):
            # self.log.debug(diff_list[i]['video_id'])
            for j in range(len(concert_list)):
                for k in range(len(famous_list)):
                    if diff_list[i] == concert_list[j] == famous_list[k]:
                        self.log.debug('Same')
                        processor = DatastoreProcessor()
                        output_list.append(
                            processor.convert_entity_to_mini_json(diff_list[i]))

        jsonobj["contents"] = output_list

        return json.dumps(jsonobj)

    def get_recommend_contents(self):
        self.log.debug('get_recommend_contents')

        # TODO
        client = datastore.Client()
        query = client.query(kind=dbconsts.SONG.KIND_NAME)
        entities = list(query.fetch())

        jsonobj = {"contents": []}
        # latest_contents = {}

        for entity in entities:

            processor = DatastoreProcessor()
            content = processor.convert_entity_to_json(entity)
            # content = processor.convert_entity_to_contentdata(entity)
            # self.log.debug(json.dumps(content))
            # latest_contents.append(content)
            jsonobj["contents"].append(content)

            # self.log.debug(jsonobj)

        return json.dumps(jsonobj)
