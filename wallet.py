import hashlib
import time
import random
import string
import base64

class Wallet:
    def __init__(self):
        self.create_address()
        # set coins on initiation
        self.coins = 100000
        

    def create_address(self):
        test = '1'
        addr = '05' + hashlib.sha256(test.encode()).hexdigest()
        check_sum = hashlib.sha256(addr.encode()).hexdigest()
        check_sum2 = hashlib.sha256(check_sum.encode()).hexdigest()
        check_sum_bytes = check_sum2[:3]

        # convert back to base64
        self.wallet_address = check_sum2
