from abc import abstractmethod


class AbstractAnalyzer:

    @abstractmethod
    def analyze(self, contentData):
        pass
