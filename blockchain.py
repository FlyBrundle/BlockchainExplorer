import hashlib
import time
import random
import string
import base64
from wallet import Wallet

class Block(object):
    def __init__(self, index, prev_hash, data, time):
        '''
        Constructor for the block objects

        :param index: Hash index
        ;param prev_hash: hash of the previous block
        :param data: Transaction data
        :param time: Timestamp indicating when the block was processed

        '''
        self.index = index
        self.prev_hash = prev_hash
        self.data = data
        self.time = time

    def __str__(self):
        ''' Displays block data '''
        return '{}-{}-{}-{}'.format(self.index, self.prev_hash, self.data, self.time)

    @property
    def calculate_hash(self):
        hash_string = '{}{}{}{}'.format(self.index,self.prev_hash,self.data,self.time)
        return hashlib.sha256(hash_string.encode()).hexdigest()

class BlockChain(object):
    def __init__(self, nodes = set()):
        ''' Constructor for our blockchain. Using only the nodes paramter for the time being
        
        :param nodes: Set of possible running nodes
        '''
        self.block_chain = []
        self.transaction_data = []
        self.nodes = nodes
        # we want to construct the genesis block immediately
        # on initilization
        self.construct_genesis()
        self.wallet = Wallet()

    def transactions(self, sender, recipient, quantity):
        ''' Builds the transaction data and then produces a hash '''
        self.transaction_data.append({
            'sender' : sender,
            'recipient' : recipient,
            'quantity' : quantity
        })
        
        return self.transaction_data

    # constructs the gensis block
    def construct_genesis(self):
        ''' Constructs genesis block '''
        # i can apparently set keyword arguments without one being in the function directly
        block = Block(
            index = 0,
            prev_hash = 0,
            data = [],
            time = time.time()
        )

        # adds the hashed data from the Block class to the blockchain list
        self.block_chain.append(block.calculate_hash)

    #constructs non-genesis blocks
    def construct_block(self):
        ''' If len is greater than 1, construct a normal block '''
        block = Block(
            index=len(self.block_chain),
            prev_hash=self.last_block,
            data=self.transaction_data,
            time=time.time()
        )

        # adds the hashed data from the Block class to the blockchain list
        self.block_chain.append(block.calculate_hash)

    # determines which block is added to the chain
    def add_block(self):
        ''' Adds a block to the chain '''
        return self.construct_genesis() if len(self.block_chain) == 0 else self.construct_block()

    def validate_block(self):
        ''' Validates a block by compring the last block to the current hash '''
        validations = [(self.last_block != Block.calculate_hash)]
        if any(validations):
            return False

    @property
    def last_block(self):
        # returns the last block in the chain to process as the prev hash
        return self.block_chain[-1]
