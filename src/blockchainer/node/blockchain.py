import json
from Crypto.Hash import SHA256

from rich import pretty
from rich.console import Console
import time

from rich.live import Live
from rich.table import Table


class Blockchain:
    
    def __init__(self):

        # for storing the blockchain
        self.blockchain = []
        
        # store all the unspent transaction outputs
        self.utxo = {}

        # net value of crypto
        self.net_value = 0

    
    def last_blk_hash(self):
        # return hash of last block
        if self.blockchain:
            return self.blockchain[-1]['body']['hash']
        else:
            return 0
    

    # add block to blockchain
    def add_block(self, _block):
        hash_value = SHA256.new(data=bytes(json.dumps(_block['header']), 'utf-8')).hexdigest()[:12]
        if hash_value == _block['body']['hash']:
            self.blockchain.append(_block)
            self.net_value+=6.25

            # also populate the UTXO with the transactions
            for tx in _block['body']['tx']:
                self.utxo[tx['hash_id']] = tx


    def get_utxo(self):
        return self.utxo
    
    def rm_tx_from_utxo(self, tx_hash):
        del self.utxo[tx_hash]
    

    # print the blockchain
    def print_all(self):
        pretty.install()
        console = Console()

        # table = Table()
        # table.add_column('UTXO')

        # with Live(table, refresh_per_second=5):
        #     for tx in self.utxo.values():
        #         time.sleep(0.5)
        #         table.add_row(tx['hash_id'])
        
        # console.print("NET VALUE : "+str(self.net_value))

        console.print(self.blockchain)
        console.print(self.utxo)