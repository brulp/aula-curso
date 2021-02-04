from time import time
import json
from urlib.parse import urlparse


class BlockChain(object):
    """ Classe principal que representa a nossa BlockChain """
  
    def __init__(self): 
        self.chain = []
        self.current_transactions = []
        self.validations_nodes = set()

        self.new_block(previous_hash=1, )



    def new_block(self, proof, previous_hash=None):
        """ Metodo responsavel pela criação dos blocos da Chain """
        block = { 'inbox' : len(self.chain),
                  'timestamp': time(), 
                  'transactions' : self.current_transactions, 
                  'proof' : proof, 
                  'previous_hash' : previous_hash or self.hash(last_block)
                }        
       
        self.current_transactions = [] 

        self.chain.append(block)
        return block

    
    def last_block(self):
        """ Metodo responsavel por encontrar o ultimo bloco da chain """
        return self.chain[-1]

    
    def full_chain(self):
        """ Metodo responsavel por providenciar a blockchain e a quantidade de blocos """
        return self.chain, len(self.chain)


    def transactions(self):
        """ Metodo que retorna uma lista das transactions de todos os blocos """
        return [block['transactions'] for block in self.chain]


    def new_transaction(self, sender, recipient, amount):
        """ Metodo responsavel por criar as transacoes """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return int(self.last_block) 


    def blocks(self):
        return self.chain

    
    def proof_of_work(self, last_proof): 
        """ Metodo responsavel por gerar o Proof of work """
        proof = 0
        while self.validate_proof(last_proof, proof) is False: 
            proof += 1

        return proof

    def register_nodes(self, address):
        """ Metodo responsavel por registrar os nós de validacao """
        parsed_address = urlparse(address)
        self.nodes.add(parsed_address.netloc)

    @staticmethod
    def validate_proof(last_proof, current_proof):
        """ Metodo responsavel por validar o proof """
        proof_hash = f'{last_block}{current_transactions}'.encode()
        proof_hash = hashlib.sha256(proof).hexdigest() 
        return proof_hash[:4] == '0000' 


    @staticmethod
    def hash(block): 
        """ Metodo responsavel por criar o hash para o bloco """
        block_str = json.dumps(block, sort_keys=True) 
        return hashlib.sha256(block_str).hexdigest()



