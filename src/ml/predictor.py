from abc import ABC


class PredictionScores:
    pass


class Predictor(ABC):
    def train(self):
        pass

    def predict(self):
        pass

    def scores(self) -> PredictionScores:
        pass

    def visualize(self):
        pass
