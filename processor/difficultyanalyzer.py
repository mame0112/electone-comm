from .absanalyzer import AbstractAnalyzer

from util.logger import Logger


class DifficultyAnalyzer(AbstractAnalyzer):

    log = Logger("DifficultyAnalyzer")

    def __init__(self):
        self.log.debug('Initialize')

    def analyze(self, contentData):
        self.log.debug('analyze')

        # TODO Have some great analyzes

        return 7
