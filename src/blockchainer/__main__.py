from .node.blockchain import Blockchain
from blockchainer.miner import Miner
from blockchainer.wallet import Wallet
from .template import Block


def blockchain():

    wallet = Wallet('key.file')
    
    miner = Miner()

    miner.wallet(wallet)

    block = Block(miner.blockchain.last_blk_hash(), []).get_block()

    mined = miner.mine(block)
    miner.blockchain.add_block(mined)

    recepients = ['45285738', '483900238', '4234848293']

    for rec in recepients:
        tx = wallet.send(1, rec, miner.blockchainer.get_utxo())
        miner.add_to_pool(tx.get_tx())
        

    miner.blockchain.print_all()