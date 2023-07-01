import json

from Crypto.Hash import SHA256

from ..template import Transaction
from blockchainer.wallet.signer import verify_sign


class Miner:
    
    def __init__(self):
        self.pool = []


    def mine(self, block, address):
        self.block = block

        # add coinbase tx
        self.block['body']['tx'].append(Transaction.get_base_tx(6.25, address))

        # find merke root
        hash_found = self.PoW()
        self.block['body']['hash'] = hash_found
        # print(self.block)
        return self.block
    

    # bind miner to blockchain for proper use
    def bind(self, blockchain):
        self.blockchain = blockchain
        

    def PoW(self):

        while True:
            hash_value = self.get_hash()
            if str(hash_value)[:self.block['header']['difficulty_target']] == '00':
                return hash_value
            else:
                # change the nonce
                self.block['header']['nonce']+=1


    def get_hash(self):
        # return the block header hash
        block_str = json.dumps(self.block['header'])

        # hash it
        hash_val = SHA256.new(data=bytes(block_str, 'utf-8')).hexdigest()

        return hash_val

    # receive trasaction to pool
    def add_to_pool(self, tx):
        tx = tx.get_tx()
        sign = tx['sign']

        for tx_hash in tx['inputs']:

            if tx_hash in self.blockchain.utxo.keys():
                self.blockchain.rm_tx_from_utxo(tx_hash)
            else:
                print("WRONG INPUTS")
        # appended to pool
        self.pool.append(tx)

    # return pool transactions 10 at a time
    def flush_pool(self):

        flushed = self.pool[:10]
        self.pool = self.pool[10:]

        if len(self.pool) <= 10:
            return flushed
        else:
            return self.pool[:10]