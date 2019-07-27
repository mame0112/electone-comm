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

        builder = ContentDataBuilder()

        builder.set_title(entity[dbconsts.PROPERTY_TITLE]).set_description(entity[dbconsts.PROPERTY_DESCRIPTION]).set_publish_date(entity[dbconsts.PROPERTY_PUBLISH_DATE]).set_thumbnail_uri(
            entity[dbconsts.PROPERTY_THUMBNAIL_URI]).set_channel_title(entity[dbconsts.PROPERTY_CHANNEL_TITLE]).set_video_id(entity[dbconsts.PROPERTY_VIDEO_ID])
        return builder.get_result()

    def convert_entity_to_json(self, entity):
        self.log.debug('convert_entity_to_json')

        builder = JsonDataBuilder()
        builder.set_title(entity[dbconsts.PROPERTY_TITLE]).set_description(entity[dbconsts.PROPERTY_DESCRIPTION]).set_publish_date(entity[dbconsts.PROPERTY_PUBLISH_DATE]).set_thumbnail_uri(
            entity[dbconsts.PROPERTY_THUMBNAIL_URI]).set_channel_title(entity[dbconsts.PROPERTY_CHANNEL_TITLE]).set_video_id(entity[dbconsts.PROPERTY_VIDEO_ID])

        # self.log.debug(builder.get_result())

        return builder.get_result()

    def convert_entity_to_mini_json(self, entity):
        self.log.debug('convert_entity_to_mini_json')

        builder = MiniJsonDataBuilder()
        builder.set_title(entity[dbconsts.PROPERTY_TITLE]).set_description(entity[dbconsts.PROPERTY_DESCRIPTION]).set_thumbnail_uri(
            entity[dbconsts.PROPERTY_THUMBNAIL_URI]).set_video_id(entity[dbconsts.PROPERTY_VIDEO_ID])

        return builder.get_result()
