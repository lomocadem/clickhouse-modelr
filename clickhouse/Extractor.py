import json


# Extract components from Json Schema
class Extractor:
    def __init__(self, database, table, table_type, table_engine, columns):
        self.database = database
        self.table = table
        self.table_type = table_type
        self.table_engine = table_engine
        self.columns = columns

    @classmethod
    def extractJson(cls, schema_path):
        json_file = open(schema_path)
        schema = json.load(json_file)
        database = schema['table']['database'].lower()
        table = schema['title'].lower()
        table_type = schema['table']['tableType']
        table_engine = schema['table']['tableEngine']
        columns = schema['properties']
        return cls(database, table, table_type, table_engine, columns)
