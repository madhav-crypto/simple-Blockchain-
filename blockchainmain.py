# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 19:44:14 2021

@author: Madhav
"""

import json
import hashlib
import datetime

class Blockchain():
    
    def __init__(self):
        
        self.chain = []
        self.create_block(proof=1,previous_hash='0')
        
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
        
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    
    def get_previous_block(self):
        return self.chain[-1]
    
    def check_chain_valid(self,chain):
        block_ind = 1
        previous_block = chain[0]
        
        while block_ind < len(chain):
            block = chain[block_ind]
            if self.hash(previous_block) != block['previous_hash']:
                return False
            
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_code = hashlib.sha256(str(proof**2-previous_proof**2).encode()).hexdigest()
            if hash_code[:4] != '0000':
                return False
            
            previous_block = block
            block_ind += 1
            
        return True
    
blockchain = Blockchain()



            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    