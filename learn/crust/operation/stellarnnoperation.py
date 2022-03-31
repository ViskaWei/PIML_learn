from abc import ABC, abstractmethod
from ..data.basestellarnn import StellarNN




class BaseStellarNNOperation(ABC):
    @abstractmethod
    def perform_on_StellarNN(self, NN: StellarNN):
        pass