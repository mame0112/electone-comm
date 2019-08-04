from util.logger import Logger
from datahandler.builder import AbstractBuilder
from datahandler.contentdata import ContentData


class ContentDataBuilder(AbstractBuilder):
    log = Logger("DatabaseDataBuilder")

    def __init__(self):
        self.log.debug('Initialize')
        self.data = ContentData()

    def set_song_id(self, song_id):
        self.data[Consts.FIELD_SONG_ID] = song_id
        return self

    def set_title(self, title):
        self.data.set_title(title)
        return self

    def set_description(self, description):
        self.data.set_description(description)
        return self

    def set_publish_date(self, publish_date):
        self.data.set_publish_date(publish_date)
        return self

    def set_thumbnail_uri(self, thumbnail_uri):
        self.data.set_thumbnail_uri(thumbnail_uri)
        return self

    def set_channel_title(self, channel_title):
        self.data.set_channel_title(channel_title)
        return self

    def set_video_id(self, video_id):
        self.data.set_video_id(video_id)
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
