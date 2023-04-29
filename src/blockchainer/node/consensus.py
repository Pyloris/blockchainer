import asyncio
from .miner import Miner



class Concensus:
    
    def __init__(self, n_workers, block):
        self.n_workers = n_workers
        self.block = block
    
    def start(self):
        pass