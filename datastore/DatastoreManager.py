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

    def get_song_data(self):
        self.log.debug('get_song_data')
        # self.log.debug(dbconsts.MASTER_KIND.TITLE)
        return
        # self.log.debug('get_song_data')

    def create_data(self, song_id):

        self.log.debug('create_data')

        client = datastore.Client()
        key = client.key(dbconsts.KIND_SONG, song_id)
        entity = datastore.Entity(key=key)
        entity[dbconsts.PROPERTY_NAME] = "Electone user"
        entity[dbconsts.PROPERTY_THUMBNAIL_URL] = "https://xxxx.com"
        client.put(entity)

        return

    def get_category_content(self, video_id):
        self.log.debug('get_category_content')

        client = datastore.Client()
        key = client.key(dbconsts.KIND_SONG, video_id)

        return

    def get_latest_data(self):
        self.log.debug('get_latest_data')

        client = datastore.Client()
        query = client.query(kind=dbconsts.KIND_SONG)
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
        key = client.key(dbconsts.KIND_SONG, song_id)
        entity = client.get(key)

        data_processor = DatastoreProcessor()
        return data_processor.convert_entity_to_contentdata(entity)

    def store_content(self, content):
        client = datastore.Client()

        video_id = content.get_video_id()
        key = client.key(dbconsts.KIND_SONG, video_id)

        if self.is_new_content(key):

            entity = datastore.Entity(key=key)
            entity[dbconsts.PROPERTY_TITLE] = content.get_title()
            entity[dbconsts.PROPERTY_DESCRIPTION] = content.get_description()
            entity[dbconsts.PROPERTY_PUBLISH_DATE] = content.get_publish_date()
            entity[dbconsts.PROPERTY_THUMBNAIL_URI] = content.get_thumbnail_uri()
            entity[dbconsts.PROPERTY_CHANNEL_TITLE] = content.get_channel_title()
            entity[dbconsts.PROPERTY_VIDEO_ID] = content.get_video_id()

            client.put(entity)

            self.log.debug(content.get_title())

    def is_new_content(self, key):

        client = datastore.Client()
        if client.get(key) is not None:
            self.log.debug('Content already exist')
            return False
        else:
            self.log.debug('New Content')
            return True

    def store_contents(self, content_list):
        self.log.debug('store_contents')

        for content in content_list:
            self.store_content(content)

    # Difficulty
    def get_contents_by_difficulty(self, min, max):
        self.log.debug('get_concents_by_difficulty')
        client = datastore.Client()

        start = client.key(dbconsts.KIND_DIFFICULTY, min)
        endend = client.key(dbconsts.KIND_DIFFICULTY, max)

        query = client.query(kind=dbconsts.KIND_DIFFICULTY)

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

        for i in range(len(difficulty_list)):

            contents = difficulty_list[str(i)]

            if len(contents) is not 0:
                key = client.key(dbconsts.KIND_DIFFICULTY, i)
                entity = client.get(key)

                # If entity for content already exist
                if entity is not None and len(entity[dbconsts.PROPERTY_CONTENTS_DATA]) is not 0:
                    content_list_json = entity[dbconsts.PROPERTY_CONTENTS_DATA]
                    self.log.debug(content_list_json)
                    for j in range(len(contents)):
                        content_list_json.append(contents[j])
                    client.put(entity)
                else:
                    # Otherwise (New Entity for this difficulty)
                    entity_new = datastore.Entity(key=key)
                    entity_new[dbconsts.PROPERTY_CONTENTS_DATA] = contents
                    client.put(entity_new)
