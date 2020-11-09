import json
from pandas import DataFrame

json_schema_location = r"C:/Users/calvin/PycharmProjects/clickhouse-modelr/sample.json"


# Extract components from Json Schema
class Extractor:
    def __init__(self, database, table, table_type, table_engine, columns):
        self.database = database
        self.table = table
        self.table_type = table_type
        self.table_engine = table_engine
        self.columns = columns

    @classmethod
    def extractJson(cls, json_schema_location):
        json_file = open(json_schema_location)
        schema = json.load(json_file)
        database = schema['table']['database'].lower()
        table = schema['title'].lower()
        table_type = schema['table']['tableType']
        table_engine = schema['table']['tableEngine']
        columns = schema['properties']
        return cls(database, table, table_type, table_engine, columns)


# Construct columns: (col_name data_type codec(codec_engine))
class Columns:
    def __init__(self, columns):
        self.columns = columns

    @classmethod
    def constructColumns(cls, columns_dict: dict):
        column_df = DataFrame.from_dict(columns_dict, orient='index',
                                        columns=['type',
                                                 'is_primary_key',
                                                 'is_partition_key',
                                                 'is_sorting_key',
                                                 'is_sample_key',
                                                 'is_nullable',
                                                 'compression_codec',
                                                 'function',
                                                 'time_zone'])
        column_with_name = column_df.reset_index().rename(columns={'index': 'column_name'})

        return cls(column_with_name)


# Construct table: db.table
class Table:
    def __init__(self, table):
        self.table = table

    @classmethod
    def constructTable(cls, database_name, table_name):
        table = database_name + "." + table_name
        return cls(table)


# Construct engine:
class Engine:
    def __init__(self, engine):
        self.engine = engine

    @classmethod
    def constructEngine(cls,engine_name):
        engine = "ENGINE=" + engine_name + "()"
        return cls(engine)


class PrimaryKey:
    def __init__(self, primary_key):
        self.primary_key = primary_key

    @classmethod
    def constructPrimaryKey(cls, pkey_name):
        primary_key = "PRIMARY KEY " + pkey_name
        return cls(primary_key)


class PartitionKey:
    def __init__(self, partition_key):
        self.partition_key = partition_key

    @classmethod
    def constructPartitionKey(cls, partition_key):
        partition_key = "PARTITION BY " + partition_key
        return cls(partition_key)


class SortingKey:
    def __init__(self, sorting_key):
        self.sorting_key = sorting_key

    @classmethod
    def constructSortingKey(cls, sorting_key_str):
        sorting_key = "ORDER BY " + sorting_key_str
        return cls(sorting_key)





a = Extractor.extractJson(json_schema_location)
print(type(a.columns))

b = Columns.constructColumns(a.columns)
print(b.columns)

