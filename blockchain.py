blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


amount = float(input('what is your transaction amount: '))
add_value(amount)
amount = float(input('what is your transaction amount: '))
add_value(amount, get_last_blockchain_value())
amount = float(input('what is your transaction amount: '))
add_value(amount, get_last_blockchain_value())
print(blockchain)
