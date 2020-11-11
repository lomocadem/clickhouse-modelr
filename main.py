from clickhouse.Constructor import Constructor


json_schema_location = r"C:/Users/lomocadem/PycharmProjects/clickhouse-modelr/sample.json"

ddl = Constructor.constructDDL(json_schema_location)
print(ddl.ddl_string)
