from base.crust.baseprocess import BaseProcess
from ..operation.stellarnnoperation import BaseStellarNNOperation

class StellarNNProcess(BaseProcess):
    def __init__(self) -> None:
        self.operation_list: list[BaseStellarNNOperation] = None

        
    