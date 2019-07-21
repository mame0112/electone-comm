from .absanalyzer import AbstractAnalyzer

from util.logger import Logger


class FamousAnalyzer(AbstractAnalyzer):

    log = Logger("FamousAnalyzer")

    def __init__(self):
        self.log.debug('Initialize')

    def analyze(self, contentData):
        self.log.debug('analyze')

        # TODO Have some great analyzes

        return 8
