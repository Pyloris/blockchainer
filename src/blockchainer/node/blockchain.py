



class Blockchain:
    """
    A Blueprint for the Blockchain database.
    - Provides API to interact with Blockchain
    
    - Blockchain is essentially a list of dictionaries(transactions).
    """
    
    def __init__(self):
        
        # empty blockchain
        self.blockchain = []
        
        # store all the unspent transaction outputs
        self.utxo = []

    




class Block:
    """
    A blueprint for a block that stores transactions.
    """
    
    def __init__(self):
        self.header = {}
        self.body = {}
        self.merkle_root = {}