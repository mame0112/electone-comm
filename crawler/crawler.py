from util.logger import Logger

from datahandler.contentdata import ContentData

from datastore.DatastoreManager import DatastoreManager

from processor.dataanalyzer import DataAnalyzer
from processor.dataprocessorparser import DataProcessorParser

from youtube.ytaccessor import YouTubeAccessor

from datahandler.contentpropertydata import ContentPropertyData


class Crawler():

    log = Logger("Crawler")

    def __init__(self):
        self.log.debug('Initialize')

    # TODO To be called from cron
    def crawel(self):
        self.log.debug('crawel')

        output = ContentData()

        difficulty_list = []
        concert_list = []
        famous_list = []

        dataManager = DatastoreManager()

        # TODO Need to add more services
        youtube = YouTubeAccessor()

        # Get Contents List from YouTube
        content_list = youtube.searcH_youtube()

        if len(content_list) == 0:
            self.log.debug('The number of content is 0')
            return

        # Add Key (Song_id)
        self.set_representative_data(output, content_list, dataManager)

        self.create_properties(output, content_list)

        self.set_mini_contents(output, content_list)

        dataManager.store_contents(output)

    def set_representative_data(self, output, content_list, dataManager):
        content = content_list[0]

        self.add_song_id(output, content, dataManager)

        output.set_title(content.get_title())
        output.set_description(content.get_description())

        self.add_keyword(output, content)

        output.set_publish_date(content.get_publish_date())
        output.set_thumbnail_url(content.get_thumbnail_url())
        output.set_channel_title(content.get_channel_title())
        output.set_video_id(content.get_video_id())

    def add_song_id(self, output, content, dataManager):
        self.log.debug('add_song_id')

        song_id = dataManager.generate_song_id(content.get_title())
        output.set_song_id(song_id)

    def add_keyword(self, output, content):
        self.log.debug('add_keyword')

        # TODO
        output.set_keyword(content.get_title())

    def create_properties(self, output, content_list):
        self.log.debug('create_properties')

        dataanalyzer = DataAnalyzer()
        propertyData = dataanalyzer.analyze_content(content_list)

        output.set_difficulty(propertyData.difficulty)
        output.set_concert(propertyData.concert)
        output.set_famous(propertyData.famous)

    def set_mini_contents(self, output, content_list):
        self.log.debug('set_mini_contents')

        parser = DataProcessorParser()
        miniContentJson = parser.create_mini_content_json_array(content_list)

        output.set_mini_content(miniContentJson)

    # def create_property_jsonObj(self, content_list):
    #     difficulty_list = []
    #     concert_list = []
    #     famous_list = []

    #     # Initialize
    #     for i in range(10):
    #         # content_list = []
    #         difficulty_list.append([])
    #         concert_list.append([])
    #         famous_list.append([])

    #     # parser = DataProcessorParser()

    #     # Check each property
    #     for i in range(len(content_list)):
    #         # for content in content_list:
    #         content = content_list[i]
    #         analyzer = DataAnalyzer()

    #         propertyData = analyzer.analyze_content(content)
    #         propertyData.video_id = content.video_id

    #         # For Difficulty list
    #         if len(difficulty_list[propertyData.difficulty]) != 0:
    #             diff_contents = difficulty_list[propertyData.difficulty]
    #             diff_contents.append(content)
    #             # self.log.debug(len(difficulty_list[propertyData.difficulty]))
    #         else:
    #             difficulty_list[propertyData.difficulty].append(content)
    #             # self.log.debug(len(difficulty_list[propertyData.difficulty]))

    #         # For Concert list
    #         if len(concert_list[propertyData.concert]) != 0:
    #             concert_contents = concert_list[propertyData.concert]
    #             concert_contents.append(content)
    #             # self.log.debug(len(difficulty_list[propertyData.difficulty]))
    #         else:
    #             concert_list[propertyData.concert].append(content)
    #             # self.log.debug(len(difficulty_list[propertyData.difficulty]))

    #         # For Famous list
    #         if len(famous_list[propertyData.famous]) != 0:
    #             famous_contents = famous_list[propertyData.famous]
    #             famous_contents.append(content)
    #             # self.log.debug(len(difficulty_list[propertyData.difficulty]))
    #         else:
    #             famous_list[propertyData.famous].append(content)
    #             # self.log.debug(len(difficulty_list[propertyData.difficulty]))

    #     # jsonObj = parser.parsePropertyListToJson(
    #     #     difficulty_list, concert_list, famous_list)

    #     return jsonObj
