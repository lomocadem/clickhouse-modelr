from clickhouse.Extractor import *
from clickhouse.Constructor import *


json_schema_location = r"C:/Users/lomocadem/PycharmProjects/clickhouse-modelr/sample.json"

a = Extractor.extractJson(json_schema_location)

b = Columns.constructColumns(a.columns)
print(b.columns)
print(b.primary_key)
print(b.partition_keys)
print(b.sorting_keys)
print(b.sample_key)