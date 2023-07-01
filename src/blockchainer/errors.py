# exception for low balance
class LowBalance(Exception):
    "Raised when trying to spend more than available outputs"

    def __init__(self, total, message='You cannot Spend more than you own :('):
        self.total = total
        self.message = message

        super().__init__(self.message)



# exception when signature to spend output is wrong
class WrongSignature(Exception):
    "Raised when signature is wrong while verifying by Miner"

    def __init__(self, sign, message='Signature provided is not right: cannot spend the output ::'):
        self.sign = sign
        self.message = message

        super().__init__(self.message)