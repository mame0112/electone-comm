from util.logger import Logger
from datahandler.contentdata import ContentData

from .dataanalyzer import DataAnalyzer
from .dataprocessorparser import DataProcessorParser

from youtube.ytaccessor import YouTubeAccessor

from datastore.DatastoreManager import DatastoreManager


class PropertyDataManager:

    log = Logger("PropertyDataManager")

    def __init__(self):
        self.log.debug('Initialize')

    def analyze_properties(self, content_list):

        self.log.debug('analyze_properties')

        difficulty_list = []
        concert_list = []
        famous_list = []

        # Initialize
        for i in range(10):
            # content_list = []
            difficulty_list.append([])
            concert_list.append([])
            famous_list.append([])

        parser = DataProcessorParser()

        # Check each property
        for i in range(len(content_list)):
            # for content in content_list:
            content = content_list[i]
            analyzer = DataAnalyzer()

            propertyData = analyzer.analyze_content(content)
            propertyData.video_id = content.video_id

            # For Difficulty list
            if len(difficulty_list[propertyData.difficulty]) != 0:
                diff_contents = difficulty_list[propertyData.difficulty]
                diff_contents.append(content)
                # self.log.debug(len(difficulty_list[propertyData.difficulty]))
            else:
                difficulty_list[propertyData.difficulty].append(content)
                # self.log.debug(len(difficulty_list[propertyData.difficulty]))

            # For Concert list
            if len(concert_list[propertyData.concert]) != 0:
                concert_contents = concert_list[propertyData.concert]
                concert_contents.append(content)
                # self.log.debug(len(difficulty_list[propertyData.difficulty]))
            else:
                concert_list[propertyData.concert].append(content)
                # self.log.debug(len(difficulty_list[propertyData.difficulty]))

            # For Famous list
            if len(famous_list[propertyData.famous]) != 0:
                famous_contents = famous_list[propertyData.famous]
                famous_contents.append(content)
                # self.log.debug(len(difficulty_list[propertyData.difficulty]))
            else:
                famous_list[propertyData.famous].append(content)
                # self.log.debug(len(difficulty_list[propertyData.difficulty]))

        jsonObj = parser.parsePropertyListToJson(
            difficulty_list, concert_list, famous_list)

        return jsonObj

    def save_property_data(self):
        self.log.debug('save_property_data')

        # TODO Need to check which youtube data should be extracted

        # Get YouTube Data
        ytaccessor = YouTubeAccessor()
        content_list = ytaccessor.searcH_youtube()

        jsonObj = self.analyze_properties(content_list)

        # Save the Json object to server
        dataManager = DatastoreManager()
        dataManager.put_contents_with_property(jsonObj)
        # dataManager.put_contents_with_property(
        #     difficulty_list, concert_list, famous_list)

        return
