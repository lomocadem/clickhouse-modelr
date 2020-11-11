from clickhouse.Extractor import Extractor
from clickhouse.Cluster import Cluster
from clickhouse.Table import Table
from clickhouse.Columns import Columns
from clickhouse.Engine import Engine
from clickhouse.PrimaryKey import PrimaryKey
from clickhouse.PartitionKey import PartitionKey
from clickhouse.SortingKey import SortingKey
from clickhouse.SampleKey import SampleKey


class Constructor:
    def __init__(self, ddl_string):
        self.ddl_string = ddl_string

    @classmethod
    def constructDDL(cls, json_schema_file):
        a = Extractor.extractJson(json_schema_file)
        table = Table.constructTable(a.table_type, a.database, a.table)
        cluster = Cluster.constructCluster(a.cluster)
        columns = Columns.constructColumns(a.columns)
        engine = Engine.constructEngine(a.table_engine)
        primary_key = PrimaryKey.constructPrimaryKey(columns.primary_key)
        partition_key = PartitionKey.constructPartitionKey(columns.partition_keys)
        sorting_key = SortingKey.constructSortingKey(columns.sorting_keys)
        sample_key = SampleKey.constructSampleKey(columns.sample_key)

        # Construct DDL
        ddl = f"{table.table}\n{cluster.cluster}\n{columns.columns}\n" \
              f"{engine.engine}\n{primary_key.primary_key}\n{partition_key.partition_key}\n" \
              f"{sorting_key.sorting_key}\n{sample_key.sample_key}"

        return cls(ddl)


