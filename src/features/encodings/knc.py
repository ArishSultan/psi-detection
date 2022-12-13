from typing import Any

from .kmer import encode_kmer
from ..encoding import Encoding


def encode_knc(sequence: str, k: int = 2) -> tuple[Any, ...]:
    return encode_kmer(sequence, k, upto=False, normalize=True)


class KNC(Encoding):
    def __init__(self, k: int = 2):
        if k < 1:
            raise 'K should be greater than 0'

        self._k = k

    @property
    def name(self):
        if self._k == 1:
            return 'nac'
        elif self._k == 2:
            return 'dnc'
        elif self._k == 3:
            return 'tnc'
        return f'knc_{self._k}'

    def encode(self, sequence: str, label: bool = False):
        return encode_knc(sequence, self._k)
