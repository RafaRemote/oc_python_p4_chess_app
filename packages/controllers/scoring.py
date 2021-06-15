from packages.models.scoring import ScoringModel

class ScoringController:
    def __init__(self, obj):
        self.obj = obj

    def __call__(self):
        update_scoring_model = ScoringModel(self.obj)
        update_scoring_model()


