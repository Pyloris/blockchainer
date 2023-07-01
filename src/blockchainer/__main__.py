from .node.blockchain import Blockchain
from blockchainer.miner import Miner
from blockchainer.wallet import Wallet
from .template import Block


def blockchain():

    blockchain = Blockchain()

    wallet = Wallet('key.file')
    
    miner = Miner()
    miner.bind(blockchain)

    block = Block(blockchain.last_blk_hash(), []).get_block()

    mined = miner.mine(block, wallet.address)
    blockchain.add_block(mined)

    tx = wallet.send(1, '582948', blockchain.get_utxo())

    miner.add_to_pool(tx)

    block = Block(blockchain.last_blk_hash(), miner.flush_pool()).get_block()
    mined = miner.mine(block, wallet.address)
    blockchain.add_block(block)

    tx = wallet.send(4, '782439', blockchain.get_utxo())

    miner.add_to_pool(tx)

    block = Block(blockchain.last_blk_hash(), miner.flush_pool()).get_block()
    mined = miner.mine(block, wallet.address)
    blockchain.add_block(block)

    tx = wallet.send(5, '948493', blockchain.get_utxo())
    miner.add_to_pool(tx)

    tx = wallet.send(5, '232423', blockchain.get_utxo())
    miner.add_to_pool(tx)


    block = Block(blockchain.last_blk_hash(), miner.flush_pool()).get_block()
    mined = miner.mine(block, wallet.address)
    blockchain.add_block(mined)


    blockchain.print_all()