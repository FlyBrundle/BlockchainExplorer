import hashlib
import time
import random
import string
import base64
try:
    from wallet import Wallet
    from blockchain import Block, Blockchain
except ImportError:
    print('Could not import. Check to see if the modules are properly installed.')

app = Flask(__name__)
app.config['SECRET_KEY'] = # secret key

wallet = Wallet()
block = BlockChain()
block_ind = Block()
sender = wallet.address 
recipient = 2 # just for testing purposes

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def hello():
    ''' Router for the home page ''' 
    
    return render_template('home.html',
                           block_chain = sorted(block.block_chain, reverse = True), 
                           value = block.last_block,
                           coins = wallet.coins,
                           wallet = wallet.wallet_address,
                           height = len(block.block_chain),
                           time = block_ind.time.strftime('%m %d, %y, %H:%M:%S')
                            )

@app.route('/about')
def about():
    ''' Router for the about page ''' 
    return render_template('about.html')

@app.route('/send', methods = ['GET', 'POST'])
def send():
    ''' Router for the send page. '''

    # process block if the button is pressed
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
