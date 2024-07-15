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


import random
from blockchain.provchainmodules.eventlisteners import EventListeners
from blockchain.modules.transaction import Transaction
from blockchain.logic.dependencymanager import DependencyManager
from blockchain.logger.processlogger import ProcessLogger
from blockchain.utils.sha3helper import SHA3Helper


class BlockchainListener(EventListeners):
    
    def __init__(self):
        self.logger = ProcessLogger("BlockchainListener")
        pass
    
    def update(self, prov_data):
        random_fee_price = random.randrange(0, 100, 1)
        
        depend_manager = DependencyManager()
        transactions = depend_manager.get_pending_transactions()
        transaction = Transaction(prov_data.sender_name, "Receiver", 1.1, 1, random_fee_price, 0.1, SHA3Helper.digest_to_hex(prov_data.prov_hash))
        transactions.add_pending_transactions(transaction)
        self.logger.log_info(f"Passed transaction {SHA3Helper.digest_to_hex(transaction.tx_id)} to dependeny manager for PROV entrance: {SHA3Helper.digest_to_hex(prov_data.prov_hash)}")
        return super().update(prov_data)
    