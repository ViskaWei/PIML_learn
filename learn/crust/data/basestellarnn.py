
from abc import ABC, abstractmethod
from .basenn import NzNN

class BaseStellarNN(ABC):
    required_attributes = [""]

class StellarNN(NzNN, BaseStellarNN):
    def __init__(self, train, test):
        super().__init__(train["data"], train["sigma"], train["label"], \
                        test["data"], test["sigma"], test["label"])
        