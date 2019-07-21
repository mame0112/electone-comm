import json

from util.logger import Logger


class DataProcessorParser:
    log = Logger("DataProcessorParser")

    def __init__(self):
        self.log.debug('Initialize')

    def parsePropertyListToJson(self, diff_list, concert_list, famous_list):
        self.log.debug('parsePropertyListToJson')

        diff_json = self.create_property_json(diff_list)
        concert_json = self.create_property_json(concert_list)
        famous_json = self.create_property_json(famous_list)

        output = {}
        output['difficulty'] = diff_json
        output['concert'] = concert_json
        output['famous'] = famous_json

        self.log.debug(output)

        return output

    def create_property_json(self, property_list):
        self.log.debug('create_property_json')

        property_json = {}

        for i in range(len(property_list)):
            contents = property_list[i]

            # Create data for each difficulty
            content_for_each_property = []

            for j in range(len(contents)):
                item_json = {}
                content = contents[j]
                item_json['title'] = content.title
                item_json['description'] = content.description
                item_json['thumbnail_uri'] = content.thumbnail_uri
                item_json['video_id'] = content.video_id
                self.log.debug(content.title)

                content_for_each_property.append(item_json)

            # Put create data to key
            property_json[str(i)] = content_for_each_property

        return property_json
