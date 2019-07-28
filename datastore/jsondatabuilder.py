import json

from util.logger import Logger
from datahandler.builder import AbstractBuilder

from const import const


class JsonDataBuilder(AbstractBuilder):
    log = Logger("JsonDataBuilder")

    def __init__(self):
        self.log.debug('Initialize')
        self.data = {}

    def set_title(self, title):
        self.data[const.FIELD_TITLE] = title
        return self

    def set_description(self, description):
        self.data[const.FIELD__DESCRIPTION] = description
        return self

    def set_publish_date(self, publish_date):
        self.data[const.FIELD_PUBLISH_DATE] = publish_date
        return self

    def set_thumbnail_url(self, thumbnail_url):
        self.data[const.FIELD_THUMBNAIL_URL] = thumbnail_url
        return self

    def set_channel_title(self, channel_title):
        self.data[const.FIELD_CHANNEL_TITLE] = channel_title
        return self

    def set_video_id(self, video_id):
        self.data[const.FIELD_VIDEO_ID] = video_id
        return self

    def get_result(self):
        return self.data
