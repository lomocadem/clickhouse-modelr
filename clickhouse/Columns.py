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

    @staticmethod
    def constructColumnsList(columns_dict: dict):
        col_list = list()
        # Construct columns list
        for key, value in columns_dict.items():
            col_name = key
            col_data_type = Columns.constructNullable(value)
            col_codec = Columns.constructCodec(value)
            if col_codec is None:
                concat = f"{col_name} {col_data_type}"
            else:
                concat = f"{col_name} {col_data_type} {col_codec}"
            col_list.append(concat)
        joint_keys = ",\n".join(col_list)
        concat = f"({joint_keys})"
        return concat

    @classmethod
    def constructColumns(cls, columns_dict: dict):
        columns_list = Columns.constructColumnsList(columns_dict)
        primary_key_name = Columns.findPrimaryKey(columns_dict)
        partition_key_name = Columns.findPartitionKey(columns_dict)
        sorting_key_list = Columns.findSortingKey(columns_dict)
        sample_key_name = Columns.findSampleKey(columns_dict)

        return cls(columns_list, primary_key_name, partition_key_name, sorting_key_list, sample_key_name)
