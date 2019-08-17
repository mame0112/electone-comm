from util.logger import Logger

from datahandler.propertyrangedata import PropertyRangeData


class PropertyRangeDataBuilder:

    def __init__(self):
        log = Logger("ContentData")
        self.prdata = PropertyRangeData()
        pass

    def set_diff_min(self, diff_min):
        self.prdata.set_diff_min(diff_min)
        return self

    def set_diff_max(self, diff_max):
        self.prdata.set_diff_man(diff_max)
        return self

    def set_concert_min(self, concert_min):
        self.prdata.set_concert_min(concert_min)
        return self

    def set_concert_max(self, concert_max):
        self.prdata.set_concert_man(concert_max)
        return self

    def set_famous_min(self, famous_min):
        self.prdata.set_famous_min(famous_min)
        return self

    def set_famous_max(self, famous_max):
        self.prdata.set_famous_man(famous_max)
        return self

    def get_result(self):
        return self.prdata
