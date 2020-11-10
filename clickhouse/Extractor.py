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
    def __init__(self, columns):
        self.columns = columns

    @staticmethod
    def constructNullable(d_type, is_nullable):
        if is_nullable:
            data_type = f"Nullable({d_type})"
        else:
            data_type = d_type
        return data_type

    @staticmethod
    def constructCodec(codec_name):
        if isinstance(codec_name, str):
            codec = ""
        else:
            codec = f"CODEC({codec_name})"
        return codec

    @staticmethod
    def constructTimezone(time_type, timezone):
        if isinstance(timezone, str):
            time_with_tz = time_type
        else:
            time_with_tz = f"{time_type}('{timezone}')"
        return time_with_tz

    @classmethod
    def constructColumnsDict(cls, columns_dict: dict):
        col_list = list()
        for key, value in columns_dict.items():
            for col_key, col_value in value.items():
                if "compression_codec" in col_key:
                    col_list.append(col_value)
                else:
                    pass
        return cls(col_list)

    @classmethod
    def constructColumns(cls, columns_dict: dict):
        # Convert column dict to dataframe
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
        # Rename column_name
        column_with_name = column_df.reset_index().rename(columns={'index': 'column_name'})

        column_list = list()
        t_list = list()
        # Construct columns DDL
        for index, row in column_with_name.iterrows():
            column_name = row['column_name']
            codec = Columns.constructCodec(row['compression_codec'])
            time = Columns.constructTimezone(row['type'], row['time_zone'])
            data_type = Columns.constructNullable(row['type'], row['is_nullable'])
            each = f"{column_name} {data_type} {codec}"
            # each = f"{row['column_name']} {row['type']} CODEC({row['compression_codec']})"
            column_list.append(each)
            t = row['compression_codec']
            t_list.append(t)
        return cls(t_list)


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


b = Columns.constructColumnsDict(a.columns)
print(b.columns)
print(type(b.columns))
