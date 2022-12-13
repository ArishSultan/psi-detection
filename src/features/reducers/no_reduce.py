from ..reducer import Reducer
from pandas import DataFrame, Series


class NoReduce(Reducer):
    @property
    def name(self) -> str:
        return ''

    def reduce(self, features: DataFrame, label: Series) -> DataFrame:
        features['label'] = label

        return features
