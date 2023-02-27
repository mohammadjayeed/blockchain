blockchain = []


def get_last_blockchain_value():
    """returns the last value of the current blockchain"""
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """appends a transaction amount and the last transaction amount that happened in the blockchain.

    Arguments:
        :transaction_amount: the amount that should be added.
        :last_transaction: the last transaction amount (defaults to [1]).
    """
    blockchain.append([last_transaction, transaction_amount])

def get_user_input():
    """returns the input of the user as a float"""
    return float(input("what is your transaction amount: "))

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

transaction_amount = get_user_input()
add_value(transaction_amount)
def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)

def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index-1] :
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid



while True:
    print('please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        transaction_amount = get_user_input()
        add_value(transaction_amount, last_transaction=get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >=1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid, please pick a value from the list!')

    print('Choice registered!')
    if not verify_chain():
        print('invalid blockchain')
        break



