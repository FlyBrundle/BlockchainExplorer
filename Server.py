import hashlib
import time
import random
import string
import base64
from wallet import Wallet
from blockchain import Block, Blockchain


app = Flask(__name__)
app.config['SECRET_KEY'] = 'codex'

wallet = Wallet()
block = BlockChain()
block_ind = Block()
sender = 1
recipient = 2

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def hello():
    # sent = 50
    # block.transactions(wallet.wallet_address, recipient, sent)
    # block.add_block()
    # wallet.coins -= sent
    # transaction data
    
    return render_template('home.html',
                           block_chain = sorted(block.block_chain, reverse = True), 
                           value = block.last_block,
                           coins = wallet.coins,
                           wallet = wallet.wallet_address,
                           height = len(block.block_chain),
                           time = block_ind.time.strftime('%m %d, %y, %H:%M:%S')
                            )

# this signifies which page is being routed
# /about in url
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/send', methods = ['GET', 'POST'])
def send():
    ''' Page to send test coins to a sepcified address. '''
    sent = 50
    block.transactions(wallet.wallet_address, recipient, sent)
    wallet.coins -= sent
    form = SubmitForm()

    if request.method == 'GET':
        sent = 50
        block.transactions(wallet.wallet_address, recipient, sent)
        block.add_block()
        wallet.coins -= sent
        
    return render_template('send.html',
                           form = form,
                           value = block.last_block,
                           coins = wallet.coins,
                           wallet = wallet.wallet_address,
                           height = block.block_chain.index(block.block_chain[-1]),
                           amount = sent)

# not being run from a module
if __name__ == '__main__':
    app.run(port = 4996)
