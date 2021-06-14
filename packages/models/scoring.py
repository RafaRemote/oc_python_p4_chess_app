class ScoringModel:
    def __init__(self, obj):
        self.obj = obj

    def __call__(self):
        return(self.obj)