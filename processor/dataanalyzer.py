from util.logger import Logger

from datahandler.contentpropertydata import ContentPropertyData

from .concertanalyzer import ConcertAnalyzer
from .difficultyanalyzer import DifficultyAnalyzer
from .famouseanalyzer import FamousAnalyzer


class DataAnalyzer:

    log = Logger("DataAnalyzer")

    def __init__(self):
        self.log.debug('Initialize')
        self.propertyData = ContentPropertyData()

    def analyze_content(self, content):
        self.log.debug('analyze_content')

        self.propertyData.difficulty = DifficultyAnalyzer().analyze(content)
        self.propertyData.concert = ConcertAnalyzer().analyze(content)
        self.propertyData.famous = FamousAnalyzer().analyze(content)

        return self.propertyData
