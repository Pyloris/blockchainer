# we will be using sha256 to hash the blocks
from hashlib import sha256

# we will use json to convert header to string and from string
# back to python datastructure


# block structure
block = {
    "header":{   
                "version":0.0.1,
                "prev_hash":"",
                "Merkle Root":"",
                "Timestamp":"",
                "Nonce":0,
                "target":0
                },
    "transactions":[]
}



# a simple implementation of blockchain
class BlockChain:
    def __init__(self):
        # blocks stored sequentially
        self.blocks = []

    def create_block(self, transactions:list):
        if len(self.blocks) == 0:
            # create genisis Block
            self.new_block = Block(0, 0, 0, transactions)
        else:
            # create block with previous hash in it
            self.new_block = Block(len(self.blocks), 0, self.blocks[-1].block_hash, transactions)
        return self.new_block

    def add_block(self, block):
        self.blocks.append(block)