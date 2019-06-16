from util.logger import Logger
from datahandler.builder import AbstractBuilder
from datahandler.contentdata import ContentData


class YouTubeDataBuilder(AbstractBuilder):

    log = Logger("YouTubeDataBuilder")

    def __init__(self):
        self.log.debug('Initialize')
        self.data = ContentData()

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

    def get_result(self):
        # self.log.debug(self.data.get_title())
        # self.log.debug(self.data.get_description())
        # self.log.debug(self.data.get_pablish_date())
        # self.log.debug(self.data.get_thumbnail_uri())
        # self.log.debug(self.data.get_channel_title())
        # self.log.debug(self.data.get_video_id())

        return self.data
