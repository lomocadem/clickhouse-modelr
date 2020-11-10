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
    def constructNullable(column_dict: dict):
        if column_dict["is_nullable"]:
            final_type = f"Nullable(" + column_dict["type"] + ")"
        else:
            final_type = column_dict["type"]
        return final_type

    @staticmethod
    def constructCodec(column_dict: dict):
        try:
            return "CODEC(" + column_dict["compression_codec"] + ")"
        except:
            pass

    @staticmethod
    def findPrimaryKey(columns_dict: dict):
        # Construct Primary key
        for key, value in columns_dict.items():
            if value["is_primary_key"]:
                return key
            else:
                pass

    @staticmethod
    def findPartitionKey(columns_dict: dict):
        # Construct Partition key
        for key, value in columns_dict.items():
            if value["is_partition_key"]:
                return key
            else:
                pass

    @staticmethod
    def findSortingKey(columns_dict: dict):
        sorting_key_list = list()
        # Construct Sorting key
        for key, value in columns_dict.items():
            if value["is_sorting_key"]:
                sorting_key_list.append(key)
            else:
                pass
        return sorting_key_list

    @staticmethod
    def findSampleKey(columns_dict: dict):
        # Construct Sample key
        for key, value in columns_dict.items():
            if value["is_sample_key"]:
                return key
            else:
                pass

    @classmethod
    def constructColumns(cls, columns_dict: dict):
        col_list = list()

        # Construct columns list
        for key, value in columns_dict.items():
            col_name = key
            col_data_type = Columns.constructNullable(value)
            col_codec = Columns.constructCodec(value)
            concat = f"{col_name} {col_data_type} {col_codec}"
            col_list.append(concat)
        primary_key_name = Columns.findPrimaryKey(columns_dict)
        partition_key_name = Columns.findPartitionKey(columns_dict)
        sorting_key_list = Columns.findSortingKey(columns_dict)
        sample_key_name = Columns.findSampleKey(columns_dict)

        return cls(col_list, primary_key_name, partition_key_name, sorting_key_list, sample_key_name)


# Construct table: db.table
class Table:
    def __init__(self, table):
        self.table = table

    @classmethod
    def constructTable(cls, database_name, table_name):
        table = f"{database_name}.{table_name}"
        return cls(table)


# Construct engine:
class Engine:
    def __init__(self, engine):
        self.engine = engine

    @classmethod
    def constructEngine(cls, engine_name):
        engine = f"ENGINE={engine_name}()"
        return cls(engine)


class PrimaryKey:
    def __init__(self, primary_key):
        self.primary_key = primary_key

    @classmethod
    def constructPrimaryKey(cls, pkey_name):
        primary_key = f"PRIMARY KEY {pkey_name}"
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