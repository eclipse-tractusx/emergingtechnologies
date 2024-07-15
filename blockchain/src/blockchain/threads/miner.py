/********************************************************************************
* Copyright (c) 2024 Contributors to the Eclipse Foundation
* Copyright (c) 2024 German Aerospace Center (DLR e.V.)
*
* See the NOTICE file(s) distributed with this work for additional
* information regarding copyright ownership.
*
* This program and the accompanying materials are made available under the
* terms of the Apache License, Version 2.0 which is available at
* https://www.apache.org/licenses/LICENSE-2.0.
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
* WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
* License for the specific language governing permissions and limitations
* under the License.
*
* SPDX-License-Identifier: Apache-2.0
********************************************************************************/


from threading import Thread
from blockchain.logic.blockchain import Blockchain
from blockchain.logic.dependencymanager import DependencyManager
from blockchain.modules.block import Block
from blockchain.utils.sha3helper import SHA3Helper
from blockchain.logger.processlogger import ProcessLogger


class Miner(Thread):
    def __init__(self):
        super().__init__()
        self.logger = ProcessLogger("Miner")
        self.listeners = []
        self.mining = True
        self.cancel_block = False
        self.block = None

    def run(self):
        self.logger.log_info("Miner started!")

        while self.is_mining():
            self.block = self.get_new_block_for_mining()

            while not self.cancel_block and self.does_not_fulfill_difficulty(self.block.get_block_hash()):
                try:
                    self.block.increment_nonce()
                except ArithmeticError as e:
                    self.logger.log_info(f"Restarting mining. {e}")
                    self.restart_mining()

            if self.cancel_block:
                self.block = None
                self.cancel_block = False
            else:
                self.block_mined(self.block)
            
        

    def get_new_block_for_mining(self):
        pending_transactions = DependencyManager.get_pending_transactions()
        blockchain = DependencyManager.get_blockchain()
        transactions = pending_transactions.get_transactions_for_the_next_block()

        return Block(transactions, blockchain.get_previous_hash())

    def does_not_fulfill_difficulty(self, digest):
        blockchain = DependencyManager.get_blockchain()
        
        return not blockchain.fulfills_difficulty(digest)

    def restart_mining(self):
        pending_transactions = DependencyManager.get_pending_transactions()
        transactions = pending_transactions.get_transactions_for_the_next_block()

        self.block.transactions(transactions)

    def block_mined(self, block: Block):

        if block.transactions:
            for transaction in block.transactions:
                transaction[1].block_id = block.get_block_hash()
                self.logger.log_info(
                    f"{transaction[1].get_tx_id_as_string()}; {SHA3Helper.digest_to_hex(transaction[1].block_id)}"
                )

        DependencyManager.get_blockchain().add_block(block)
        #DependencyManager.get_pending_transactions().clear_pending_transactions(block) #TODO: Look if really obsolete because priortyQueue.get() already deletes itemes from queue
        self.logger.log_info("Block mined!")
        
        for listener in self.listeners:
            listener.notify_new_block(block)

    def is_mining(self):
        return self.mining

    def set_mining(self, mining: bool):
        self.mining = mining

    def stop_mining(self):
        self.logger.log_info("Stopping mining.")
        self.mining = False

    def set_cancel_block(self, cancel_block: bool):
        self.logger.log_info("Canceling block.")
        self.cancel_block = cancel_block

    def set_cancel_block(self):
        self.cancel_block = True
        
    def register_listener(self, listener):
        self.listeners.append(listener)
    