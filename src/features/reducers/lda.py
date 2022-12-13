from ..reducer import Reducer
from pandas import DataFrame, Series
from sklearn.decomposition import LatentDirichletAllocation as _LatentDirichletAllocation


class LatentDirichletAllocation(Reducer):
    def __init__(self, n_components: int = 2, max_iter: int = 5, learning_method='batch'):
        self._max_iter = max_iter
        self._n_components = n_components
        self._learning_method = learning_method

    @property
    def name(self) -> str:
        return 'pca'

    def reduce(self, features: DataFrame, label: Series) -> DataFrame:
        return _LatentDirichletAllocation(
            max_iter=self._max_iter,
            n_components=self._n_components,
            learning_method=self._learning_method,
        ).fit_transform(features, label)
