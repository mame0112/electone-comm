from util.logger import Logger


class ContentData:
    log = Logger("ContentData")

    def __init__(self):
        pass

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    def set_publish_date(self, publish_date):
        self.publish_date = publish_date

    def set_thumbnail_url(self, thumb_url):
        self.thumb_url = thumb_url

    def set_channel_title(self, channel_title):
        self.channel_title = channel_title

    def set_video_id(self, video_id):
        self.video_id = video_id

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_publish_date(self):
        return self.publish_date

    def get_thumbnail_url(self):
        return self.thumb_url

    def get_channel_title(self):
        return self.channel_title

    def get_video_id(self):
        return self.video_id
