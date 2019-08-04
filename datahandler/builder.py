from abc import abstractmethod


class AbstractBuilder:

    @abstractmethod
    def set_title(self, title):
        pass

    @abstractmethod
    def set_description(self, description):
        pass

    @abstractmethod
    def set_publishdate(self, publish_date):
        pass

    @abstractmethod
    def set_thumbnail_url(self, thumb_url):
        pass

    @abstractmethod
    def set_channel_title(self, channel_title):
        pass

    @abstractmethod
    def set_video_id(self, video_id):
        pass

    @abstractmethod
    def set_difficulty(self, difficulty):
        pass

    @abstractmethod
    def set_concert(self, concert):
        pass

    @abstractmethod
    def set_famous(self, famous):
        pass

    @abstractmethod
    def set_content(self, contentJson):
        pass

    @abstractmethod
    def get_result(self):
        pass
