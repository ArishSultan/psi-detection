from pandas import DataFrame, concat, Series

from ...features import Reducer
from ..transformer import DataTransformerStep, DataTransformerResult


class FeatureReduction(DataTransformerStep):
    def __init__(self, reducers: list[Reducer]):
        self._reducers = reducers

    def _apply(self, result: DataTransformerResult) -> DataTransformerResult:
        new_result = DataTransformerResult()

        for key, value in result.iter():
            for reducer in self._reducers:
                if len(reducer.name) > 0:
                    new_key = f'{key}>{reducer.name}'
                else:
                    new_key = key

                new_result.set(
                    new_key,
                    reducer.reduce(value.drop(['label', 'set'], axis=1), value['label'])
                )

        return new_result


def _generate_column_names(length: int):
    return [f'x{x + 1}' for x in range(length)]
