from abc import abstractmethod


class AbstractBuilder:

    @abstractmethod
    def set_title(self, title):
        pass

    @abstractmethod
    def set_description(self, description):
        pass

    @abstractmethod
    def get_result(self):
        pass
