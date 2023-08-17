from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from os import path

from blockchainer.template import Transaction
from blockchainer.errors import LowBalance
from .signer import setup_verifier, sign



class Wallet:
    
    def __init__(self, filename, rand=False):
        
        # if file is given reaR̥d the key
        if not rand and path.exists(filename):
            self.key = ECC.import_key(open(filename, 'rt').read())
        elif rand:
            self.key = ECC.generate(curve='P-256')
        else:
            # generate key pair
            self.key = ECC.generate(curve='P-256')
            
            # save it
            with open(filename, 'wt') as f:
                f.write(self.key.export_key(format='PEM'))

        
        # public key
        self.public_key = self.key.public_key().export_key(format='DER').hex()[2:]

        # address
        self.address = str(SHA256.new(data=bytes(self.public_key, 'utf-8')).hexdigest())[:8]

        # setup verifier
        setup_verifier(self.key)
    
    
    def send(self, amount, address, utxo):
        # it generates a transaction that is passed to miner
        # for it to verify the tx and add it to pool
        # then we grab tx from pool to add them to blocks.
        # we first have to mine some empty blocks to generate some currency.

        # grab amount equal to total value of UTXO associtated with our addr.
        # usable_tx = [tx for tx in utxo.values() for out in tx['output'] if out['lock'] == self.address()]
        usable_tx = []

        # find transactions that contain outputs belonging to us
        for tx in utxo.values():
            for output in tx['output']:
                if output['address'] == self.address:
                    usable_tx.append(tx)

        # variables used in transaction building
        current_sum = 0
        my_tx = []
        my_output = []
        not_my_output = []
        spended = []

        # track output index
        i = 0

        # find usable outputs
        for tx in usable_tx:

            # break when amount is fullfilled
            if current_sum >= amount:
                break

            for out in tx['output']:

                if out['address'] == self.address:
                    if current_sum < amount:
                        current_sum += out['value']

                        # store outputs belonging to us
                        my_output.append(out)
                        spended.append(i)
                        i+=1
                else:
                    # store outputs not belonging to us
                    not_my_output.append(out)

            # add the transactions used into
            # this list
            self.miner.remove_tx(tx['hash_id'])
            my_tx.append(tx['hash_id'])
        
        if current_sum < amount:
            raise LowBalance(current_sum)

            
        tx = Transaction(my_tx, sign(self.address), amount, address, outputs=not_my_output)

        ch_amount = current_sum - amount

        # if its not 0, create change transaction
        if ch_amount > 0:
            tx.get_change(ch_amount, self.address)
        
        return tx


    # connect to miner back
    def connect(self, miner):
        self.miner = miner