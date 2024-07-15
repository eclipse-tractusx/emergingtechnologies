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


from blockchain.logic.pendingtransactions import PendingTransaction
from blockchain.logic.blockchain import Blockchain
from blockchain.logger.processlogger import ProcessLogger


class DependencyManager:
    """
    DependencyManager is a class that manages the dependencies for pending transactions,
    the blockchain, and the miner. It ensures that only one instance of each dependency exists and
    provides methods to get or inject these dependencies.

    Attributes:
        pending_transactions (PendingTransaction): The instance managing pending transactions.
        blockchain (Blockchain): The blockchain instance.
        miner (Miner): The miner instance.
        instance (DependencyManager): The singleton instance of this class.
        logger (ProcessLogger): Logger instance for logging dependency manager activities.
    """
    pending_transactions = None
    blockchain = None
    miner = None
    instance = None #* attribute for singleton function
    
    logger = ProcessLogger("DependencyManager")

    #* singleton funcionality for test purposes
    def __new__(cls):
        if not cls.instance:
            cls.instance = super(DependencyManager, cls).__new__(cls)
        return cls.instance
    
    @staticmethod
    def get_pending_transactions() -> PendingTransaction:
        """
        Retrieves the pending transactions instance, creating it if it doesn't exist.
        """
        if DependencyManager.pending_transactions is None:
            DependencyManager.pending_transactions = PendingTransaction()
            DependencyManager.logger.log_info(f"{DependencyManager.pending_transactions} created PendingTransaction.")
        
        return DependencyManager.pending_transactions

    @staticmethod
    def inject_pending_transaction(pending_transaction: PendingTransaction):
        """
        Injects an external pending transactions instance.
        """
        DependencyManager.pending_transactions = pending_transaction

    @staticmethod
    def get_blockchain() -> Blockchain:
        """
        Retrieves the blockchain instance, creating it if it doesn't exist.
        """
        if DependencyManager.blockchain is None:
            DependencyManager.blockchain = Blockchain()
        
        return DependencyManager.blockchain

    def inject_blockchain(blockchain: Blockchain):
        """
        Injects an external blockchain instance.
        """
        DependencyManager.blockchain = blockchain

    def get_miner():
        """
        Retrieves the miner instance, creating it if it doesn't exist.
        """
        from blockchain.threads.miner import Miner
        if DependencyManager.miner is None:
            DependencyManager.miner = Miner()
        
        return DependencyManager.miner
