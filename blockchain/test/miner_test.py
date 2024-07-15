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


import time
import threading
import unittest

from blockchain import DependencyManager
from blockchain import Block, Transaction
from blockchain import SHA3Helper
from blockchain import MinerListener, Miner
from blockchain import ProcessLogger

logger = ProcessLogger("Test")
class MinerTest(unittest.TestCase):
    
    def setUp(self):
        self.depend_manager = DependencyManager()
        self.transactions = self.depend_manager.get_pending_transactions()

        for i in range(100):
            sender = f"testSender{i}"
            receiver = f"testReceiver{i}"
            amount = i * 1.1
            nonce = i
            transactionFee = 0.0000001 * i
            transactionFeeLimit = 10.0

            # transaction is a PendingTransaction instance
            self.transactions.add_pending_transactions(
                Transaction(
                    sender.encode(),
                    receiver.encode(),
                    amount,
                    nonce,
                    transactionFee,
                    transactionFeeLimit
                )
            )
            
        logger.log_info(f"Amount of transaction in queue: {self.transactions.get_pending_transaction_len()}")

    def test_miner(self):
        self.miner = Miner()
        self.miner.register_listener(self)
        logger.log_info("Miner loaded!")

        thread = threading.Thread(target = self.miner.run, daemon=True)
        thread.start()
        
        
        self.depend_manage = DependencyManager()
        
        while self.depend_manage.get_pending_transactions().pending_transactions_available():
            #logger.log_debug(f"Transaction available: {self.depend_manage.get_pending_transactions().pending_transactions_available()} - Pending Transactions: {self.depend_manage.pending_transactions.pending_transactions.qsize()}")
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                logger.log_info("Thread interrupted by user.")
        
        self.miner.stop_mining()
        
        thread.join()   # wait until thread terminates

        logger.log_info(f"Länge der Blockchain: {len(self.depend_manage.get_blockchain())}")
        logger.log_info(f"Block: {self.depend_manage.get_blockchain()[0]}")

    def notify_new_block(self, block):
        logger.log_info(f"New block mined - Block Hash: {SHA3Helper.digest_to_hex(block.get_block_hash())}")


if __name__ == '__main__':
    unittest.main()
