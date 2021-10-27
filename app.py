# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 21:23:49 2021

@author: Madhav
"""
from blockchainmain import *
from flask import Flask , jsonify
app = Flask(__name__)

@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Congratulations, you just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200

@app.route('/get_complete_chain',methods=['GET'])
def get_complete_chain():
    responce = {'chain': blockchain.chain,
                'lenght of chain': len(blockchain.chain)}
    
    return jsonify(responce),200
    
@app.route('/check_if_valid',methods=['GET'])
def check_if_valid():
    valid = blockchain.check_chain_valid(blockchain.chain)
    if valid:
        responce = {'message': 'The chain is valid'}
        
    else:
        responce = {'message': 'The chain is invalid'}
        
    return jsonify(responce),200
        
app.run(host='0.0.0.0',port=5000)


































