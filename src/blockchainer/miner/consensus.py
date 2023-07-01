from Crypto.Hash import SHA256
import json


# find block hash
def get_block_hash(block):
    # convert block header to string
    block_header = json.dumps(block['header'])

    # hash it
    hash_value = SHA256.new(data=bytes(block_header, 'utf-8')).hexdigest()

    return hash_value



# proof of work algorithm
def PoW(block):

    while True:
            hash_value = get_block_hash(block)
            if str(hash_value)[:block['header']['difficulty_target']] == '0'*block['header']['difficulty_target']:
                return hash_value
            else:
                # change the nonce
                block['header']['nonce']+=1