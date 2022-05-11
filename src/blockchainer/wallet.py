'''
Generate private-public key pair
'''

from fastecdsa import curve, ecdsa, keys
from os import path



class Wallet:
    
    """
        TRANSACTIONS AND GENERATE/STORE PUB/PRIV KEYS

        USAGE:
            1. Create the Object
                wallet = Wallet()

            2. Use the provided methods
    """

    def __init__(self, filepath):
        # if file path is provided then we can
        # load keys from it
        # otherwise we will generate a new key pair

        # file path to keys
        self.filepath = filepath


        # generate pub/priv key pair
        if path.isfile(self.filepath):

            # import keys from the file
            self.priv_key = keys.import_key(self.filepath)
            self.pub_key = keys.get_public_key(self.priv_key, curve=curve.secp256k1)
        else:

            # generate new keys
            self.priv_key = keys.gen_private_key(curve=curve.secp256k1)
            self.pub_key  = keys.get_public_key(self.priv_key, curve=curve.secp256k1)



    # method to compress the pub_key 
    def compress_pubkey(self):

        """
            Compressed key has a prefix of 0x43 which
            is hex for C (compressed).
            
            Only x coordinate is stored in the compressed key
        """

        compressed_key = str(hex(self.pub_key.x)).replace("0x", "0x43")

        # return the compressed key
        return compressed_key