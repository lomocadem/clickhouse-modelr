class SortingKey:
    def __init__(self, sorting_key: str):
        self.sorting_key = sorting_key

    @classmethod
    def constructSortingKey(cls, sorting_keys: list):
        joint_keys = ", ".join(sorting_keys)
        concat = f"ORDER BY ({joint_keys})"
        return cls(concat)