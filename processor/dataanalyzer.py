from util.logger import Logger

from datahandler.contentpropertydata import ContentPropertyData

from .concertanalyzer import ConcertAnalyzer
from .difficultyanalyzer import DifficultyAnalyzer
from .famouseanalyzer import FamousAnalyzer


class DataAnalyzer:

    log = Logger("DataAnalyzer")

    def __init__(self):
        self.log.debug('Initialize')

    def analyze_content(self, content_list):
        self.log.debug('analyze_content')

        propertyData = ContentPropertyData()

        # TODO Need to send all content_list (Not only 1)
        propertyData.difficulty = DifficultyAnalyzer().analyze(content_list[0])
        propertyData.concert = ConcertAnalyzer().analyze(content_list[0])
        propertyData.famous = FamousAnalyzer().analyze(content_list[0])

        return propertyData
