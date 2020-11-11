# Construct table: db.table
class Table:
    def __init__(self, table):
        self.table = table

    @classmethod
    def constructTable(cls, table_type, database_name, table_name):
        table = f"CREATE {table_type} {database_name}.{table_name}"
        return cls(table)