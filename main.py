from clickhouse.Extractor import Extractor
from clickhouse.Table import Table
from clickhouse.Columns import Columns
from clickhouse.Engine import Engine
from clickhouse.PrimaryKey import PrimaryKey
from clickhouse.PartitionKey import PartitionKey
from clickhouse.SortingKey import SortingKey
from clickhouse.SampleKey import SampleKey


json_schema_location = r"C:/Users/calvin/PycharmProjects/clickhouse-modelr/sample.json"

a = Extractor.extractJson(json_schema_location)


f = Table.constructTable(a.table_type, a.database, a.table)
print(f.table)

b = Columns.constructColumns(a.columns)
print(b.columns)

e = Engine.constructEngine(a.table_engine)
print(e.engine)

h = PartitionKey.constructPartitionKey(b.partition_keys)
print(h.partition_key)

d = PrimaryKey.constructPrimaryKey(b.primary_key)
print(d.primary_key)

c = SortingKey.constructSortingKey(b.sorting_keys)
print(c.sorting_key)

g = SampleKey.constructSampleKey(b.sample_key)
print(g.sample_key)
