import json
import numpy as np
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
    def __init__(self, columns: str,
                 primary_key: str,
                 partition_key: str,
                 sorting_keys: list,
                 sample_key: str):
        self.columns = columns
        self.primary_key = primary_key
        self.partition_keys = partition_key
        self.sorting_keys = sorting_keys
        self.sample_key = sample_key

    @staticmethod
    def constructNullable(d_type, is_nullable):
        pass

    @staticmethod
    def constructCodec(column_dict: dict):
        pass

    @staticmethod
    def constructTimezone(time_type, timezone):
        pass

    @classmethod
    def constructColumnsDict(cls, columns_dict: dict):
        col_list = list()
        # Construct columns DDL
        for key, value in columns_dict.items():
            column_name = key
            for col_key, col_value in value.items():
                pass

        return cls(col_list)


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
    def constructEngine(cls, engine_name):
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
    def __init__(self, partition_key: str):
        self.partition_key = partition_key

    @classmethod
    def constructPartitionKey(cls, partition_key: str):
        concat = f"PARTITION BY {partition_key}"
        return cls(concat)


class SortingKey:
    def __init__(self, sorting_key: str):
        self.sorting_key = sorting_key

    @classmethod
    def constructSortingKey(cls, sorting_keys: list):
        joint_keys = ", ".join(sorting_keys)
        concat = f"ORDER BY ({joint_keys})"
        return cls(concat)


class SampleKey:
    def __init__(self, sample_key: str):
        self.sample_key = sample_key

    @classmethod
    def constructSampleKey(cls, sample_key: str):
        concat = f"SAMPLE BY {sample_key}"
        return cls(concat)



a = Extractor.extractJson(json_schema_location)


b = Columns.constructColumnsDict(a.columns)
print(b.columns)
print(type(b.columns))
