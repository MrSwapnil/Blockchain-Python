from components.utils import convert_obj_to_string, print_blockchain
from components.Blockchain import Blockchain
from components.utils import DIFFICULTY
from components.Customer import Customer
from components.Block import Block


blockchain = Blockchain()
def block_chain():
    print_blockchain('Difficulty is ' + str(DIFFICULTY))

    add_customer_to_blockchain(1, "A", "Hof")
    add_customer_to_blockchain(2, "B", "Mannheim")
    add_customer_to_blockchain(3, "C", "Hamburg")
    add_customer_to_blockchain(4, "D", "Berlin")

    if blockchain.validate_block_chain():
        print_blockchain('Blockchain is valid')

    blockchain.show_data()

def add_customer_to_blockchain(customer_id, customer_name, customer_address):

    customer = Customer(customer_id, customer_name, customer_address)
    obj_customer = (convert_obj_to_string(customer))
    previous_hash = "0"  if len(blockchain.blocks) == 0 else blockchain.blocks[-1].hash
    blockchain.add_block(Block(obj_customer,previous_hash))

if __name__ == '__main__':
    block_chain()

