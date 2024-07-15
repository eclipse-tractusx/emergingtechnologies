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


from blockchain.modules.transaction import Transaction


class TransactionComparatorByFee:
    """
    TransactionComparatorByFee is a utility class for comparing the fees of two transactions.
    It provides a static method to compare the base prices of transaction fees.
    """
    def __init__(self) -> None:
        pass

    @staticmethod
    def compare_transaction_fees(transaction_1: Transaction, transaction_2: Transaction) -> int:
        result = 0

        if (transaction_1.transaction_fee_base_price - transaction_2.transaction_fee_base_price) < 0:
            result = -1
        elif (transaction_1.transaction_fee_base_price - transaction_2.transaction_fee_base_price) > 0:
            result = 1

        return result
