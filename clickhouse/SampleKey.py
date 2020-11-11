class SampleKey:
    def __init__(self, sample_key: str):
        self.sample_key = sample_key

    @classmethod
    def constructSampleKey(cls, sample_key: str):
        concat = f"SAMPLE BY {sample_key}"
        return cls(concat)