# from util.logger import Logger

# from youtube.ytaccessor import YouTubeAccessor
# from datastore.DatastoreManager import DatastoreManager


# class YouTubeCrawler():

#     log = Logger("YouTubeCrawler")

#     def __init__(self):
#         self.log.debug('Initialize')

#     # TODO To be called from cron
#     def crawel_youtube(self):
#         self.log.debug('crawel_youtube')
#         youtube = YouTubeAccessor()

#         # Get Contents List from YouTube
#         content_list = youtube.searcH_youtube()

#         propertyManager = PropertyDataManager()
#         jsonObj = propertyManager.analyze_properties(content_list)

#         dataManager = DatastoreManager()
#         dataManager.store_contents(content_list)
