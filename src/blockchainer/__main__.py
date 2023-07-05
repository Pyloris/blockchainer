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

    tx = wallet.send(1, '582948', miner.blockchain.get_utxo())

    miner.add_to_pool(tx)

    block = Block(miner.blockchain.last_blk_hash(), miner.flush_pool()).get_block()
    mined = miner.mine(block)
    miner.blockchain.add_block(block)

    tx = wallet.send(4, '782439', miner.blockchain.get_utxo())

    miner.add_to_pool(tx)

    block = Block(miner.blockchain.last_blk_hash(), miner.flush_pool()).get_block()
    mined = miner.mine(block)
    miner.blockchain.add_block(block)

    tx = wallet.send(5, '948493', miner.blockchain.get_utxo())
    miner.add_to_pool(tx)

    tx = wallet.send(5, '232423', miner.blockchain.get_utxo())
    miner.add_to_pool(tx)


    block = Block(miner.blockchain.last_blk_hash(), miner.flush_pool()).get_block()
    mined = miner.mine(block)
    miner.blockchain.add_block(mined)


    miner.blockchain.print_all()