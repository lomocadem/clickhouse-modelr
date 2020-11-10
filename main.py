from clickhouse.Extractor import Extractor
from clickhouse.Constructor import *


json_schema_location = r"C:/Users/lomocadem/PycharmProjects/clickhouse-modelr/sample.json"

a = Extractor.extractJson(json_schema_location)

print("CREATE TABLE")

f = Table.constructTable(a.database, a.table)
print(f.table)

b = Columns.constructColumns(a.columns)
print(b.columns)
print(b.primary_key)
print(b.partition_keys)
print(b.sorting_keys)
print(b.sample_key)

e = Engine.constructEngine(a.table_engine)
print(e.engine)

d = PrimaryKey.constructPrimaryKey(b.primary_key)
print(d.primary_key)

c = SortingKey.constructSortingKey(b.sorting_keys)
print(c.sorting_key)