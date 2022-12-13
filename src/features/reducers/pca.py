from ..reducer import Reducer
from pandas import DataFrame, Series
from sklearn.decomposition import PCA as _PCA


class PCA(Reducer):
    def __init__(self, n_components: int = 2):
        self._n_components = n_components

    @property
    def name(self) -> str:
        return 'pca'

    def reduce(self, features: DataFrame, label: Series) -> DataFrame:
        return _PCA(n_components=self._n_components).fit_transform(features, label)
