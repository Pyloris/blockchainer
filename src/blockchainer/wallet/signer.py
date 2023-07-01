from Crypto.Hash import SHA256
from Crypto.Signature import DSS

import binascii

# not yet setup
verifier = None

# setup verifier
# call from wallet main module
def setup_verifier(priv_key):
        global verifier
        verifier = DSS.new(priv_key, 'fips-186-3')


def sign(addr):
        addr = SHA256.new(data=bytes(addr, 'utf-8'))

        signed = verifier.sign(addr)

        # conver to hex
        signed = binascii.hexlify(signed).decode()

        return signed


def verify_sign(sign, addr):
        # hash to generate data to verify against
        hash_addr = SHA256.new(data=bytes(addr, 'utf-8'))

        try:
            verifier.verify(hash_addr, sign)
            return True
        except ValueError:
            return False