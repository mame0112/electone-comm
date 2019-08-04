import json

from util.logger import Logger
from datahandler.builder import AbstractBuilder

from const import const


class MiniJsonDataBuilder(AbstractBuilder):
    log = Logger("MiniJsonDataBuilder")

    def __init__(self):
        self.log.debug('Initialize')
        self.data = {}

    def set_title(self, title):
        self.data[const.FIELD_TITLE] = title
        return self

    def set_description(self, description):
        self.data[const.FIELD_DESCRIPTION] = description
        return self

    def set_thumbnail_uri(self, thumbnail_uri):
        self.data[const.FIELD_THUMBNAIL_URI] = thumbnail_uri
        return self

    def set_video_id(self, video_id):
        self.data[const.FIELD_VIDEO_ID] = video_id
        return self

    def get_result(self):
        return self.data
