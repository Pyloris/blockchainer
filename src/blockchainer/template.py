from datetime import datetime

from Crypto.Hash import SHA256
import random

import json


# ################## Transaction
class Transaction:

    def __init__(self, inputs, signature, amount, receiver, outputs=[], spended=[]):
        self.transaction = {}
        self.transaction['inputs'] = inputs

        self.transaction['u_inputs'] = spended

        self.transaction['sign'] = signature[:12]

        # generate change as well
        self.transaction['output'] = [{
            'value':amount,
            'address':receiver[:12]
        }, *outputs]
        
        self.transaction['hash_id'] = self.get_tx_hash()


    # get a coinbase transaction for rewarding
    @classmethod
    def get_base_tx(cls, reward, address):
        tx = {}
        tx['inputs'] = [{'tx_type':'coinbase', 'nonce':str(random.randint(0,100000))}]
        tx['output'] = [{
            'value':reward,
            'address':address[:12]
        }]

        str_tx = json.dumps(tx)

        tx['hash_id'] = str(SHA256.new(data=bytes(str_tx, 'utf-8')).hexdigest())[:12]

        return tx

    def get_tx_hash(self):
        # concat all the inputs & outputs
        all_tx = self.transaction['inputs'] + self.transaction['output']

        concat_tx = '\n'.join(map(json.dumps, all_tx))

        # hash the transactions
        hash_value = str(SHA256.new(data=bytes(concat_tx, 'utf-8')).hexdigest())[:12]

        return hash_value
    
    def get_tx(self):
        # this method returns transaction itself
        return self.transaction
    
    def get_change(self, value, address):
        self.transaction['output'][0]['value'] - value
        self.transaction['output'].append({
            'value':value,
            'address':address[:12]
        })




# ################ BLOCK

class Block:
    
    def __init__(self, prev_block_hash, transactions, difficulty=2):

        # create the block
        self.header = {
            'previous_block_hash':str(prev_block_hash)[:12],
            'timestamp' : datetime.timestamp(datetime.now()),
            'difficulty_target' : difficulty,
            'merkle_root' : self.get_merkle_root(),
            'nonce' : 0
        }

        self.body = {
            'tx': transactions
        }

    def get_block(self):
        return {'header':{**self.header}, 'body':{**self.body}}
    
    
    def get_merkle_root(self):
        # find the merkle root of the transactions
        return '57304'