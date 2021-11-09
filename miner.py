# -*- coding: utf-8 -*-
"""
Copyright 2019-2021 Lummetry.AI (Knowledge Investment Group SRL). All Rights Reserved.


* NOTICE:  All information contained herein is, and remains
* the property of Knowledge Investment Group SRL.  
* The intellectual and technical concepts contained
* herein are proprietary to Knowledge Investment Group SRL
* and may be covered by Romanian and Foreign Patents,
* patents in process, and are protected by trade secret or copyright law.
* Dissemination of this information or reproduction of this material
* is strictly forbidden unless prior written permission is obtained
* from Knowledge Investment Group SRL.


@copyright: Lummetry.AI
@author: Lummetry.AI
@project: 
@description:
@created on: Tue Nov  9 09:01:03 2021
@created by: damia
"""

from block import Block
from chain import BlockOneChain

class BlockOneMiner:
  def __init__(self, blockchain: BlockOneChain):
    self.chain = blockchain
    return

  
  def P(self, s):
    if hasattr(super(), 'P'):
      super().P(s)
    else:
      print(s, flush=True)  

  def proof_of_work(self, block: Block):
    block.nonce = 0
    computed_hash = block.compute_hash()
    while not self.chain.is_difficulty_valid(block=block, proof=computed_hash):
      block.nonce += 1
      computed_hash = block.compute_hash()
    return computed_hash

  
  def mine(self):
    blockchain = self.chain
    if not len(blockchain.unconfirmed_transactions) > 0:
      return False
    self.P("Mining...")
    
    new_block = Block(
      index=blockchain.last_block.index + 1,
      transactions=blockchain.get_unconfirmed(as_dicts=True),
      timestamp=blockchain.get_timestamp(),
      previous_hash=blockchain.last_block.hash,
      )
    proof = self.proof_of_work(block=new_block)    
    
    blockchain.add_block(block=new_block, proof=proof)
    blockchain.reset_transactions()
    self.P("Done mining.")
    return new_block.index
  