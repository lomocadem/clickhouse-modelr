class PrimaryKey:
    def __init__(self, primary_key):
        self.primary_key = primary_key

    @classmethod
    def constructPrimaryKey(cls, pkey_name):
        primary_key = f"PRIMARY KEY {pkey_name}"
        return cls(primary_key)