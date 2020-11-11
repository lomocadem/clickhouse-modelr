# Construct engine:
class Engine:
    def __init__(self, engine):
        self.engine = engine

    @classmethod
    def constructEngine(cls, engine_name):
        engine = f"ENGINE={engine_name}()"
        return cls(engine)