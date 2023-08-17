from blockchainer.template import Transaction
from blockchainer.wallet.signer import verify_sign
from blockchainer.node.blockchain import Blockchain
from blockchainer.errors import ReferenceNotFound
from .consensus import PoW



class Miner:
    
    def __init__(self):
        self.pool = []

        # local copy of blockchain
        self.blockchain = Blockchain()


    def mine(self, block):
        self.block = block
        # add coinbase tx
        self.block['body']['tx'].append(Transaction.get_base_tx(6.25, self.wallet.address))

        # find hash of block
        hash_found = PoW(block)
        self.block['body']['hash'] = hash_found[:12]
        
        # print(self.block)
        return block

    # receive trasaction to pool
    def add_to_pool(self, tx):
        self.pool.append(tx)
    

    # remove transaction from utxo
    def remove_tx(self, tx_hash):

            if tx_hash in self.blockchain.utxo.keys():
                self.blockchain.rm_tx_from_utxo(tx_hash)
                print("[REMOVED] "+tx_hash)
            else:
                raise ReferenceNotFound(tx)
        

    # return pool transactions 10 at a time
    def flush_pool(self):

        if len(self.pool) <= 10:
            flushed = self.pool.copy()
            self.pool.clear()
        else:
            flushed = self.pool[:10]
            self.pool = self.pool[10:]

        return flushed
        
    
    def wallet(self, wallet):
        self.wallet = wallet
        wallet.connect(self)