from datetime import datetime



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
    
    Block Header Structure:
    {
        'previous block hash',
        'merkle root',
        'timestamp' - creation time in unix epoch,
        'difficulty target' - no of zeros at start of hash
        'Nonce' - counter for PoW algorithm
    }
    
    Block
    {
        'hash': 4589f83934, - hash of current block header
        'header fields included here',
        'tx': [
            'tx1',
            'tx2'
        ]
    }
    """
    
    def __init__(self, transactions: list, blockchain):
        self.header = {}
        self.body = {}
        self.blockchain = blockchain
        self.transactions = transactions
        
        
    def create_block(self):
        
        # create the header
        self.header['previous_block_hash'] = self.blockchain.get_tx_hashes()[-1]
        self.header['timestamp'] = datetime.timestamp()
        self.header['difficulty_target'] = 2
        self.header['merkle_root'] = self.get_merkle_root()
        self.header['nonce'] = 0

        
        # create body
        self.body['hash'] = self.get_header_hash()
        self.body['tx'] = self.transactions
        
        
        
    def get_header_hash(self):
        # combine all the header values and convert them to raw bytes of specified lengths
        # use double sha256 to find the hash
        pass
    
    
    def get_merkle_root(self):
        pass