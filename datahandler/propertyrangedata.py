class PropertyRangeData:

    def __init__(self):
        self.diff_min = 0
        self.diff_max = 0
        self.concert_min = 0
        self.concert_max = 0
        self.famous_min = 0
        self.famous_max = 0

        return

    def set_difficulty_min(self, diff_min):
        self.diff_min = diff_min

    def set_difficulty_min(self, diff_max):
        self.diff_min = diff_max

    def set_concert_min(self, concert_min):
        self.diff_min = concert_min

    def set_concert_min(self, concert_max):
        self.diff_min = concert_max

    def set_famous_min(self, famous_min):
        self.diff_min = famous_min

    def set_famous_min(self, famous_max):
        self.diff_min = famous_max

    def get_difficulty_min():
        return self.diff_min

    def get_difficulty_max():
        return self.diff_max

    def get_concert_min():
        return self.concert_min

    def get_concert_max():
        return self.concert_max

    def get_famous_min():
        return self.famous_min

    def get_famous_max():
        return self.famous_max
