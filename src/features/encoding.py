from abc import abstractmethod, ABC


class Encoding(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def encode(self, sequence: str):
        pass
