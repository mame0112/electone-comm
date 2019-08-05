import json

from util.logger import Logger

from .contentdatabuilder import ContentDataBuilder
from .minijsondatabuilder import MiniJsonDataBuilder

from .jsondatabuilder import JsonDataBuilder


from . import dbconsts


class DatastoreProcessor():

    log = Logger("DatastoreProcessor")

    def __init__(self):
        self.log.debug('Initialize')

    def convert_entity_to_contentdata(self, entity):
        self.log.debug('convert_entity_to_contentdata')

        self.builder = ContentDataBuilder()

        self.builder.set_song_id(entity[dbconsts.SONG.SONG_ID]).set_title(entity[dbconsts.SONG.REP_TITLE]).set_description(entity[dbconsts.SONG.REP_DESCRIPTION]).set_publish_date(entity[dbconsts.SONG.REP_PUBLISH_DATE]).set_thumbnail_url(
            entity[dbconsts.SONG.REP_THUMB_URL]).set_channel_title(entity[dbconsts.SONG.REP_CHANNEL_TITLE]).set_video_id(entity[dbconsts.SONG.REP_VIDEO_ID]).set_difficulty(entity[dbconsts.SONG.DIFFICULTY]).set_famous(entity[dbconsts.SONG.FAMOUS]).set_concert(entity[dbconsts.SONG.CONCERT])
        return self.builder.get_result()

    def convert_entity_to_json(self, entity):
        self.log.debug('convert_entity_to_json')

        self.builder = JsonDataBuilder()
        self.builder.set_song_id(entity[dbconsts.SONG.SONG_ID]).set_title(entity[dbconsts.SONG.REP_TITLE]).set_description(entity[dbconsts.SONG.REP_DESCRIPTION]).set_publish_date(entity[dbconsts.SONG.REP_PUBLISH_DATE]).set_thumbnail_url(
            entity[dbconsts.SONG.REP_THUMB_URL]).set_channel_title(entity[dbconsts.SONG.REP_CHANNEL_TITLE]).set_video_id(entity[dbconsts.SONG.REP_VIDEO_ID]).set_difficulty(entity[dbconsts.SONG.DIFFICULTY]).set_famous(entity[dbconsts.SONG.FAMOUS]).set_concert(entity[dbconsts.SONG.CONCERT]).set_contents(entity[dbconsts.SONG.CONTENTS])

        return self.builder.get_result()

    def convert_entity_to_mini_json(self, entity):
        self.log.debug('convert_entity_to_mini_json')

        self.builder = MiniJsonDataBuilder()
        self.builder.set_title(entity[dbconsts.SONG.REP_TITLE]).set_description(entity[dbconsts.SONG.REP_DESCRIPTION]).set_thumbnail_url(
            entity[dbconsts.SONG.REP_THUMB_URL]).set_video_id(entity[dbconsts.SONG.REP_VIDEO_ID])

        return self.builder.get_result()
