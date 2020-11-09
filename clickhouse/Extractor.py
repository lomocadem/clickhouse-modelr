import json


def JsonReader(json_schema_location):
    json_file = open(json_schema_location)
    schema = json.load(json_file)
    return schema


class Extractor:
    def __init__(self, json_schema_location):
        self.schema = JsonReader(json_schema_location)
        self.database = self.schema['table']['database'].lower()
        self.table = self.schema['title'].lower()
        self.table_type = self.schema['table']['tableType']
        self.table_engine = self.schema['table']['tableEngine']
        self.columns = self.schema['properties']

