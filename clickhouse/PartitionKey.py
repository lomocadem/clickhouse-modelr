class PartitionKey:
    def __init__(self, partition_key: str):
        self.partition_key = partition_key

    @classmethod
    def constructPartitionKey(cls, partition_key: str):
        concat = f"PARTITION BY {partition_key}"
        return cls(concat)