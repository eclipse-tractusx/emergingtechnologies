# Data Provenance based on Blockchain (DLR)

Data provenance is a record of the history of data that describes, among other things, which processes it has gone through and which actors have carried out these processes. Ensuring data provenance is of crucial importance for the integrity and trustworthiness of information in digital systems. In this context, blockchain technology is a promising solution to securely store and verify provenance data. This project demonstrates a possibility how to secure provenance data with the immutability of the blockchain technology and will be used to demonstrate the effectiveness of this solution and discuss its potential impact on the security and reliability of digital infrastructures.

## Table Of Content

- [Requirements](#requirements)
- [Description](#description)
    - [Basic Blockchain](#basic-blockchain)
    - [Provenance Chain Concept](#provenance-chain-concept)
    - [Structure of the demonstrator](#structure-of-the-demonstrator)
- [Further Steps](#further-steps)
- [References](#references)

## Requirements

Python >= 3.11

Install the `requirement.txt`. 

For that create an virtual environment. In this example `Virtualenv` is used.

```bash
virtualenv --python=python3.11 venv
```
Activate the virtual environment and install the requirements.
```bash
pip install -r requirement.txt
```
Last step: install this package also into the environment.
```bash
pip install -e .
```   

## Description

This section explains the concept of the provenance chain for a decentralized ecosystem and outlines the structure of the basic blockchain used to secure provenance data.

### Basic Blockchain

The basic blockchain is structured like the example of [[2]](#2). The 'Transaction' class is the most basic component of the blockchain. It contains all needed attributes of a transaction which can be modified depending on the required needs. Every time a transaction is created it gets collected in the queue of the 'Pending Transaction'. Is the threshold of the queue reached a miner gets active and creates a block. Every block needs a blockheader, so the block creats a blockheader and get filled with the transaction and the miner starts to solve a cryptographic puzzle. Is the puzzle solved the block is added to the chain. 


![Structure of the basic blockchain](/images/basic_blockchain.png)
*Structure of the basic blockchain [[2]](#2)*

### Provenance Chain Concept

Liang et al. [[1]](#1) suggest a ProvChain for cloud-based systems. Therefore here it is introduced the concept for the storage of provenance data on a blockchain in a decentralized data ecosystem, which to our understanding it is the first time such concept is addressed. Provenance data is to be recorded by operations on the data within this data ecosystem. These operations can be carried out by users as well as by services that process data. An observer structure is used to record provenance data when operations are carried out and this data is forwarded to both the blockchain and the provenance database.

[Fig. 2]: /images/ds_provchain.png
![Data Space ProvChain][Fig. 2]
*Concept to collect provenance data in a decentralized data ecosystem*

**Architecture**

- **User**: A user is a participant in the decentralized data ecosystem who can own data or obtain data from other users. Operations that a user performs on data are recorded with provenance data and stored on the blockchain and the database.

- **Decentralized data ecosystem**: The decentralized data ecosystem assumes that data is not stored and collected centrally on a server structure, but that it is stored by the users and can be offered to other users and exchanged with each other via suitable software, e.g. a connector.

- **Provenance database**: The provenance database is stored
decentrally in the data ecosystem and contains all prove-
nance data entries as plain text entries.

- **Blockchain**: The blockchain is a private blockchain that is
integrated into the decentralized data ecosystem. Users of the decentralized data ecosystem can also act as miners here and contribute to creating value and securing the provenance of data.

[Fig. 2] shows a possible scenario. The user Alice creates a file and offers it in the decentralized data ecosystem. Bob requests this file and receives a copy of it. Bob edits the file in his possession within the data ecosystem. For each of these steps; creation, transfer of the copy and modification of the file, the required provenance data is collected. Two parallel processes are then initiated:
1) The provenance data with all its arguments is transmitted
to the database.
2) A hash is created from the collected provenance data
and transmitted to the blockchain as a transaction.
Both the database and the blockchain can be viewed by
users to ensure trust and traceability. By saving the hash
of the provenance data on the blockchain, the provenance
data can be verified again at any time. This hash is also
protected from subsequent manipulation by the immutability
of the blockchain.

## Structure of the demonstrator

The test program involves two users, Alice and Bob, interacting with a file system (see [Fig. 3]). The primary objective is to track and record the provenance data of each action performed by these users, secure this data by creating a hash, and then send this hash as a transaction to the blockchain.

[Fig. 3]: /images/demonstrator_git.png
![Demonstrator][Fig. 3]
*Process flow of the demonstrator*

### Process Flow

1) File Creation by Alice:
    - Alice initiates the process by creating a file.
    - As soon as the file is created, the provenance data related to this action is collected. This data includes information such as the timestamp of creation, the user who created the file (Alice), and other relevant metadata about the file.

2) File Modification by Bob:
    - Bob modifies the file created by Alice.
    - Similar to the creation action, the provenance data for Bob's modification is collected. This includes the timestamp of modification, the user performing the modification (Bob), and details of the changes made.

### Provenance Data Collection

For each action (creation and modification), provenance data is gathered. This data helps in maintaining a detailed history of the file's lifecycle and ensures transparency and accountability.

### Hash Creation

Once the provenance data is collected, a hash is generated from this data. Hashing is a cryptographic technique that converts the provenance data into a unique, fixed-size string of characters, which acts as a digital fingerprint of the data.

### Blockchain Transaction

The generated hash is then sent to the blockchain as a transaction. By storing the hash on the blockchain, the integrity and immutability of the provenance data are ensured. Any attempt to alter the provenance data would result in a different hash, making it easy to detect tampering.

This process ensures that all actions taken by users on the file are securely recorded and can be verified for authenticity and integrity using blockchain technology.

## Further steps

To enhance the system's functionality and security, the following steps should be pursued: 

1) Decentralized Provenance Database: Develop a solution to implement the provenance database in a decentralized manner. This would ensure that no single entity has control over the data, aligning with the principles of decentralization and enhancing the robustness of the system against single points of failure.

2) Data Privacy Solutions: Identify and implement solutions that prevent direct access to the provenance entries by unauthorized parties. This could involve encryption techniques or permissioned access models to ensure that only authorized users can view or interact with the provenance data, thereby protecting sensitive information while maintaining transparency and accountability.

## References
<a id="1">[1]</a> 
Liang et al. (2017). 
ProvChain: A Blockchain-Based Data Provenance Architecture in Cloud Environment with Enhanced Privacy and Availability. 
2017 17th IEEE/ACM International Symposium 2017, 468–477.

<a id="2">[2]</a> 
Fertig, Tobias; Schütz, Andreas (2019). 
Blockchain für Entwickler.
Rheinwerk Verlag, ISBN: 978-3-8362-6390-0.
