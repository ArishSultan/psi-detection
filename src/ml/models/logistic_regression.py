from ..predictor import Predictor
import sklearn.linear_model as lm


class LogisticRegression(Predictor):
    def __init__(self, penalty: str):
        self._model = lm.LogisticRegression(penalty=penalty)

    def train(self):
        pass
