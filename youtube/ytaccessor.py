# ytaccessor.py
import os
# from dotenv import find_dotenv, load_dotenv
from os.path import join, dirname
from dotenv import load_dotenv

from util.logger import Logger

from .ytdatabuilder import YouTubeDataBuilder

from googleapiclient.discovery import build

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


class YouTubeAccessor:

    log = Logger("YouTubeAccessor")

    def __init__(self):
        # log = Logger("DatastoreManager")
        self.log.debug('Initialize')

        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)

    def get_youtube_data(self):
        self.log.debug('get_youtube_data')
        return

    def searcH_youtube(self):
        self.log.debug('youtube_search')

        # youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        #                 developerKey=YOUTUBE_API_KEY)
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                        developerKey=os.environ['YOUTUBE_API_KEY'])

        # Call the search.list method to retrieve results matching the specified
        # query term.
        search_response = youtube.search().list(
            part='id, snippet',
            q='Electone',
            type='Video'
        ).execute()

        # YouTube content list
        content_list = []

        for item in search_response['items']:

            builder = YouTubeDataBuilder()

            builder.set_title(item['snippet']['title']).set_description(
                item['snippet']['description']).set_publish_date(item['snippet']['publishedAt']).set_thumbnail_url(item['snippet']['thumbnails']['default']['url']).set_channel_title(item['snippet']['channelTitle']).set_video_id(item['id']['videoId'])

            content_list.append(builder.get_result())

        return content_list
