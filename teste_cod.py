import unittest
from aula2 import BlockChain

class Teste_blockchain(unittest.TestCase):
    
    def test_new_block(self):
        
        self.chain = [123456]
        self.current_transactions = [123]
        self.validations_nodes = set()        

        bloco_de_retornando = BlockChain.new_block(self, 'proof_blabla', previous_hash='123456')
        bloco_ok = {'inbox': 1, 'previous_hash': '123456', 'proof': 'proof_blabla', 'transactions': [123]}

        #Teste 1, valida criação de bloco
        self.assertEqual(bloco_de_retornando, bloco_ok)             

    def check_empty_transaction(self):

        #Teste 2, valida limpar transaction
        self.assertTrue(self.current_transactions == []) 
       

if __name__ == '__main__':
    unittest.main()