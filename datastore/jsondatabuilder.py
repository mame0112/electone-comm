import json

from util.logger import Logger
from datahandler.builder import AbstractBuilder

from const.const import Consts


class JsonDataBuilder(AbstractBuilder):
    log = Logger("JsonDataBuilder")

    def __init__(self):
        self.log.debug('Initialize')
        self.data = {}

    def set_song_id(self, song_id):
        self.data[Consts.FIELD_SONG_ID] = song_id
        return self

    def set_title(self, title):
        self.data[Consts.FIELD_TITLE] = title
        return self

    def set_description(self, description):
        self.data[Consts.FIELD_DESCRIPTION] = description
        return self

    def set_publish_date(self, publish_date):
        self.data[Consts.FIELD_PUBLISH_DATE] = publish_date
        return self

    def set_thumbnail_url(self, thumbnail_url):
        self.data[Consts.FIELD_THUMBNAIL_URL] = thumbnail_url
        return self

    def set_channel_title(self, channel_title):
        self.data[Consts.FIELD_CHANNEL_TITLE] = channel_title
        return self

    def set_video_id(self, video_id):
        self.data[Consts.FIELD_VIDEO_ID] = video_id
        return self

    def set_difficulty(self, song_id):
        self.data[Consts.FIELD_DIFFICULTY] = song_id
        return self

    def set_famous(self, famous):
        self.data[Consts.FIELD_FAMOUS] = famous
        return self

    def set_concert(self, concert):
        self.data[Consts.FIELD_CONCERT] = concert
        return self

    def get_result(self):
        return self.data
