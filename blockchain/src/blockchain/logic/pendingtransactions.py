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


import queue

from blockchain.modules.transaction import Transaction
from blockchain.modules.block import Block
from blockchain.utils.transactioncomparatorbyfee import TransactionComparatorByFee
from blockchain.logger.processlogger import ProcessLogger


class PendingTransaction:
    """
    The class is used to manage outstanding transactions, since not all transactions can be
    processed immediately by solving the cryptographic puzzle. It uses Priority Queues to sort
    and save temporarily the transactions.
    """
    def __init__(self) -> None:
        self.__pending_transactions = queue.PriorityQueue()
        #self.__comparator = TransactionComparatorByFee()
        self.logger = ProcessLogger("PendingTransaction")

    def add_pending_transactions(self, transaction: Transaction):
        """
        Add transaction to priority queue.
        """
        self.logger.log_info(f"Adding transaction: {transaction.get_tx_id_as_string()}")
        self.__pending_transactions.put((transaction.transaction_fee_base_price, transaction)) #* Entries are typically tuples of the form:  (priority number, data) 
   
    def get_transactions_for_the_next_block(self) -> list:
        """
        Collect the transaction that will be processed in the next block.
        """
        next_transactions = list()
        #TODO: Add transaction capacity. Add maybe a dummy counter for test.
        transaction_counter = 1     #* set to 1 for Prov demo
        self.logger.log_debug(f"Length of pending transaction queue: {self.__pending_transactions.qsize()}")
        
        while transaction_counter > 0 and not self.__pending_transactions.empty():
            #TODO: Check for alternative for get(). get() deletes item from queue, shoudn't happen here.
            next_transactions.append(self.__pending_transactions.get())
            transaction_counter -= 1

        return next_transactions

    def clear_pending_transactions(self, block: Block):
        """
        Clear the pending transactions list from the already processed  transactions. 
        """
        self.clear_transactions_from_block(block.transactions)


    def clear_transactions_from_block(self, transactions: list):
        #TODO: Queue should be deleted here. Not in get_transactions_for_the_next_block() method.
        for transaction in transactions:
            self.logger.log_debug(f"Fee: {transaction[1].transaction_fee_base_price} Transaction: {transaction}")
            self.logger.log_debug(f"Pending Transactions: {self.__pending_transactions} Length: {self.__pending_transactions.qsize()}") 
            self.__pending_transactions.queue.remove((transaction[1].transaction_fee_base_price, transaction[1]))
        
    def pending_transactions_available(self) -> bool:
        """
        Check if pending transaction queue is empty. 
        """
        return not self.__pending_transactions.empty()
    
    def get_pending_transaction_len(self) -> int:
        """
        Get the lenght of the pending transaction queue.
        """
        return self.pending_transactions.qsize()
        
    @property
    def pending_transactions(self):
        return self.__pending_transactions
    
    @pending_transactions.setter
    def pending_transactions(self, value: queue.PriorityQueue):
        self.__pending_transactions = value
        if value != queue.PriorityQueue:
            raise AttributeError("The attribute pending_transaction has to be a queue.PriorityQueue object!")
        