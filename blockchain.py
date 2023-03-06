blockchain = []
open_transaction = []
owner = 'Jayeed'
genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transaction':[],

}
blockchain.append(genesis_block)
def get_last_blockchain_value():
    """returns the last value of the current blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def hashed_block(block):
    return '-'.join([str(block[key]) for key in block])

def add_transaction(recipient,sender=owner,amount=1.0):
    """appends a transaction amount and the last transaction amount that happened in the open transaction.

    Arguments:
        :sender: the sender
        :recipient: the recipient
        :amount: the amount to be sent
    """
    transaction = {'sender':sender,'recipient':recipient,'amount':amount}
    open_transaction.append(transaction)


def mine_block(transaction):
    
    last_block = blockchain[-1]
    hashed = hashed_block(last_block)
    block = {

        'previous_hash': hashed,
        'index': len(blockchain),
        'transaction': transaction,
        

    }
    blockchain.append(block)


def get_user_input():
    """returns the input of the user as a float"""
    recipient = input("who is the recipient? ")
    tx_amount = input("what is the transaction amount: ")
    return (recipient,tx_amount)

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

# transaction_amount = get_user_input()
# add_value(transaction_amount)

def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)

def verify_chain():
    
    for index, block in enumerate(blockchain):
        if index == 0:
            # print('here')
            continue
        elif block['previous_hash'] != hashed_block(blockchain[index-1]):
            print('here')
            return False
    return True



while True:
    print('please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('3: Mine the blocks')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        recipient, tx_amount = get_user_input()
        add_transaction(recipient=recipient, amount=tx_amount)
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >=1:
            blockchain[1] = {
                'previous_hash': '',
                'index': 0,
                'transaction':[{'sender': 'Saif', 'recipient': 'Kerry', 'amount': '10.20'}],

            }
    elif user_choice == 'q':
        break
    elif user_choice == '3':
        transaction = open_transaction.copy()
        mine_block(transaction)
    else:
        print('Input was invalid, please pick a value from the list!')

    print('Choice registered!')
    if not verify_chain():
        print('invalid blockchain')
        print_blockchain_elements()
        break



