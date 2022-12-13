from abc import ABC
from pandas import DataFrame, Series


class Reducer(ABC):
    @property
    def name(self) -> str:
        return 'none'

    def reduce(self, features: DataFrame, label: Series) -> DataFrame:
        pass

    def __eq__(self, other):
        return other is Reducer and other.name == self.name
