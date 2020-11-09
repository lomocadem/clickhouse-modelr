import json


json_schema_location = r"C:/Users/calvin/PycharmProjects/clickhouse-modelr/sample.json"
json_file = open(json_schema_location)
json_schema = json.load(json_file)
