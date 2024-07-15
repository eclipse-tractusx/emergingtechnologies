<!---
# ********************************************************************************
# Copyright (c) 2024 Contributors to the Eclipse Foundation
# Copyright (c) 2024 German Aerospace Center (DLR e.V.)
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# ********************************************************************************
-->

# Homomorphic Encryption

Homomorphic encryption is a cryptographic technique that allows computation on encrypted data without decrypting it first. This concept enables secure computation over sensitive data while maintaining privacy. It has applications in various fields such as cloud computing, data sharing, and secure multiparty computation.

## Introduction

In the landscape of modern cryptography, where security and privacy are paramount concerns, homomorphic encryption stands out as a revolutionary concept with profound implications. At its core, homomorphic encryption offers a tantalizing prospect: the ability to perform computations on encrypted data without the need to decrypt it first. This groundbreaking property has the potential to transform the way we handle sensitive information, enabling secure and private computation on data while it remains encrypted.

At its essence, homomorphic encryption provides a mechanism for performing operations on encrypted data in such a way that the results of those operations are consistent with the results of performing the same operations on the plaintext data. In simpler terms, it allows computations to be carried out on data while it remains in an encrypted state, preserving the confidentiality of the information throughout the entire process.

The significance of this capability cannot be overstated. Traditional encryption schemes necessitate decryption prior to performing any computational tasks, exposing sensitive data to potential security risks at various points in the process. However, homomorphic encryption eliminates this vulnerability by enabling computation directly on encrypted data, thereby safeguarding privacy and confidentiality without sacrificing functionality.

The development of homomorphic encryption represents a significant milestone in the quest for privacy-preserving technologies. By enabling computations on encrypted data, it empowers individuals and organizations to leverage the power of modern computing while ensuring the confidentiality of their sensitive information. This has profound implications across a myriad of domains, from healthcare and finance to telecommunications and beyond.

One of the key applications of homomorphic encryption lies in secure cloud computing. With traditional encryption methods, outsourcing computation to the cloud often entails exposing sensitive data to third-party service providers, raising concerns about privacy and data integrity. However, homomorphic encryption offers a solution to this dilemma by allowing computations to be performed on encrypted data within the cloud environment itself, shielding the data from prying eyes while still enabling useful processing.

Moreover, homomorphic encryption holds promise for advancing collaborative research and analysis in fields where data privacy is paramount. By enabling secure computation on encrypted data, researchers can collaborate on sensitive datasets without compromising the confidentiality of the information involved. This opens up new possibilities for cross-institutional collaboration and data sharing while ensuring compliance with strict privacy regulations.

Despite its transformative potential, homomorphic encryption is not without its challenges. The computational overhead associated with performing operations on encrypted data can be significant, potentially limiting its practical applicability in resource-constrained environments. Additionally, designing efficient homomorphic encryption schemes that strike the delicate balance between security and performance remains an active area of research.

## Preliminaries

Homomorphic encryption is a cryptographic technique that enables computations to be performed on encrypted data without decrypting it. Before delving into the specifics of homomorphic encryption, it's essential to understand some preliminary concepts.

### Symmetric Key Encryption

Symmetric key encryption, also known as secret key encryption, is a cryptographic scheme that uses the same key for both encryption and decryption. In this scheme, the sender and receiver must both know the secret key.

### Encryption Function

Let $E_k$ denote the encryption function with key $k$, and $m$ denote the plaintext message. The ciphertext $c$ is obtained as: $c = E_k(m)$

### Decryption Function

The decryption function $D_k$ with the same key $k$ retrieves the plaintext message $m$ from the ciphertext $c$:
$ m = D_k(c) $

### Public Key Encryption

Public key encryption, also known as asymmetric encryption, uses a pair of keys: a public key for encryption and a private key for decryption. The public key is made available to anyone, while the private key is kept secret.

### Encryption Function

Let $E_{\text{pub}}$ denote the encryption function with the public key, $m$ denote the plaintext message. The ciphertext $c$ is obtained as:
$ c = E_{\text{pub}}(m) $

### Decryption Function

The decryption function $D_{\text{priv}}$ with the private key retrieves the plaintext message $m$ from the ciphertext $c$:
$ m = D_{\text{priv}}(c) $

### Homomorphic Encryption

Homomorphic encryption enables computations to be performed on encrypted data. Let $E$ denote the encryption function, $D$ denote the decryption function, and $+$ denote the addition operation.

#### Additive Homomorphism

Homomorphic encryption is said to be additively homomorphic if for any plaintexts $m_1$ and $m_2$, and their corresponding ciphertexts $c_1$ and $c_2$, the sum of the ciphertexts decrypts to the sum of the plaintexts:
$ D(c_1 + c_2) = m_1 + m_2 $


#### Multiplicative Homomorphism

Homomorphic encryption is said to be multiplicatively homomorphic if for any plaintexts $m_1$ and $m_2$, and their corresponding ciphertexts $c_1$ and $c_2$, the product of the ciphertexts decrypts to the product of the plaintexts:
$ D(c_1 \cdot c_2) = m_1 \cdot m_2 $

These preliminary concepts lay the foundation for understanding homomorphic encryption, a powerful cryptographic tool with applications in privacy-preserving computation.


#### How It Works

Traditional encryption schemes require decryption before performing any computation on the data, which exposes it to potential security risks. In contrast, homomorphic encryption enables computation directly on encrypted data. The result of the computation is encrypted, and when decrypted, it matches the result of the computation performed on the plaintext.

##### Types of Homomorphic Encryption

1. **Partially Homomorphic Encryption (PHE):** Allows computation on encrypted data for only one operation, either addition or multiplication.
   
2. **Somewhat Homomorphic Encryption (SHE):** Enables a limited number of additions and multiplications on encrypted data.

3. **Fully Homomorphic Encryption (FHE):** Supports an unlimited number of additions and multiplications on encrypted data, making it more powerful but also more computationally intensive.

#### Applications

- **Privacy-Preserving Data Analysis:** Organizations can perform computations on encrypted data without exposing sensitive information. For example, medical researchers can analyze encrypted patient data without compromising privacy.

- **Secure Outsourcing of Computation:** Cloud service providers can perform computations on encrypted data, ensuring confidentiality while offering computational resources.

- **Secure Multiparty Computation:** Multiple parties can jointly compute a function over their encrypted inputs without revealing their individual data. This is useful in scenarios like auctions or voting systems.

#### Challenges

- **Performance Overhead:** Homomorphic encryption can introduce significant computational overhead due to the complexity of cryptographic operations.

- **Limited Functionality:** Fully homomorphic encryption schemes are still in the early stages of development and may not support all types of computations efficiently.

- **Key Management:** Managing keys securely and efficiently is crucial for the practical implementation of homomorphic encryption.

## Methodology 

Homomorphic encryption represents a revolutionary advancement in the realm of cryptography, offering a transformative solution to the perennial challenge of balancing data privacy with computational utility. In this methodology, we delineate a systematic approach to harnessing the power of homomorphic encryption within the context of data analysis, facilitated by the interactive capabilities of the Streamlit framework. By seamlessly integrating homomorphic encryption into the data space, we aim to enable secure and privacy-preserving computations while preserving the confidentiality of sensitive information.

### Contextualizing the Approach

Before delving into the intricacies of the methodology, it is imperative to contextualize the approach within the broader landscape of data privacy and security. In an era characterized by rampant data breaches and privacy infringements, the need for robust cryptographic solutions that safeguard sensitive information has never been more pronounced. Homomorphic encryption emerges as a beacon of hope, offering a paradigm-shifting framework wherein computations can be performed on encrypted data without compromising its confidentiality.

### Environmental Setup and Configuration

The journey begins with the meticulous setup and configuration of the computational environment. This entails the installation of requisite libraries and dependencies, including Streamlit and homomorphic encryption frameworks such as PySEAL or TenSEAL. By ensuring the seamless integration of these components, we lay the foundation for the subsequent stages of the methodology.

### Data Preprocessing and Encryption

Central to the methodology is the meticulous preparation and encryption of the dataset under analysis. Sensitive information, meticulously curated to reflect real-world scenarios, is subjected to robust encryption protocols, thereby obfuscating its contents from prying eyes. Through the judicious application of homomorphic encryption techniques, computations can subsequently be performed on the encrypted data without compromising its confidentiality.

### Interactive Computation and Analysis

A hallmark of the methodology is the development of an interactive computational interface using Streamlit, wherein users are empowered to perform a myriad of computations on the encrypted dataset. Leveraging the intuitive capabilities of Streamlit, users can seamlessly navigate through a plethora of analytical options, including mean, sum, or count operations, all while preserving the privacy and integrity of the underlying data.

### Decryption and Result Interpretation

Following the execution of computations on the encrypted dataset, the computed results are decrypted and presented to the user in a comprehensible format. This crucial step ensures that users can interpret the analytical outcomes with precision and accuracy, thereby deriving meaningful insights from the encrypted data while adhering to stringent privacy protocols.

### User Engagement and Feedback Mechanisms

Culminating the methodology is the seamless deployment of the Streamlit application to a web server, thereby facilitating widespread accessibility and utilization. By making the computational interface readily available to stakeholders across diverse domains, the methodology catalyzes the dissemination of homomorphic encryption techniques and fosters a culture of data-driven innovation and collaboration.

## Results

The implementation of homomorphic encryption within a data space using Streamlit yields a rich tapestry of results, elucidating the profound implications and transformative potential of this cryptographic technique in safeguarding data privacy while enabling sophisticated computational analysis. Delving deeper into these outcomes provides invaluable insights into the multifaceted impact of homomorphic encryption in the realm of data-driven decision-making:

### Enhanced Data Privacy

At the forefront of the results lies the unparalleled enhancement of data privacy afforded by homomorphic encryption. By encrypting sensitive information prior to computational analysis, the confidentiality and integrity of the underlying data are rigorously preserved. This robust privacy framework instills a sense of confidence and trust among users, mitigating the risk of privacy breaches and unauthorized access to sensitive information. Moreover, the adoption of homomorphic encryption bolsters compliance with stringent data privacy regulations, ensuring adherence to ethical and legal standards governing the handling of sensitive data.

### Seamless Computational Analysis

The integration of homomorphic encryption with Streamlit streamlines computational analysis on encrypted data, unlocking a myriad of analytical possibilities while preserving privacy. Users are empowered to navigate through a diverse array of analytical options, leveraging the intuitive interface of Streamlit to perform computations with ease and efficiency. From basic statistical operations such as mean and sum to more complex computations involving machine learning algorithms, the seamless fusion of cryptographic security and computational utility enables users to derive actionable insights from encrypted datasets with unprecedented accuracy and precision.

### Preservation of Data Integrity

A salient result of homomorphic encryption implementation is the preservation of data integrity throughout the analytical process. By performing computations directly on encrypted data, without the need for decryption, the integrity and authenticity of the underlying data are rigorously maintained. This ensures that the analytical outcomes remain faithful to the original dataset, mitigating the risk of data tampering or manipulation. As a result, users can make informed decisions with confidence, relying on the integrity of the analytical outcomes to drive strategic initiatives and inform business-critical decisions.

### Empowerment of Privacy-Preserving Data Analysis

Homomorphic encryption implemented within a Streamlit environment empowers users to engage in privacy-preserving data analysis with unparalleled efficacy. By providing a seamless interface for performing computations on encrypted data, Streamlit democratizes access to advanced cryptographic techniques, enabling users across diverse domains to harness the power of homomorphic encryption for secure and privacy-conscious data analysis. This democratization of cryptographic tools not only facilitates innovation and collaboration but also fosters a culture of data-driven decision-making that prioritizes privacy and security as fundamental tenets of data governance and stewardship.

### Facilitation of Collaborative Research and Innovation

The implementation of homomorphic encryption in a Streamlit-based data space fosters a conducive environment for collaborative research and innovation. Researchers and practitioners across disparate domains can seamlessly collaborate on encrypted datasets, leveraging the interactive capabilities of Streamlit to perform computations and derive insights while preserving data privacy. This collaborative ethos engenders a culture of knowledge-sharing and interdisciplinary collaboration, driving forward the frontiers of data science and cryptography in tandem. Moreover, the collaborative nature of homomorphic encryption implementation facilitates cross-sectoral partnerships and knowledge exchange, leading to the emergence of novel insights and solutions to complex societal challenges.

### Validation and Endorsement of Privacy-Preserving Technologies

The successful implementation of homomorphic encryption within a Streamlit environment serves as a validation and endorsement of privacy-preserving technologies in the realm of data analysis. By demonstrating the feasibility and efficacy of homomorphic encryption in real-world applications, the results obtained underscore the transformative potential of cryptographic techniques in safeguarding data privacy and enabling secure computational analysis. This validation not only bolsters confidence in the efficacy of privacy-preserving technologies but also catalyzes widespread adoption and integration across diverse sectors and industries. As organizations increasingly prioritize data privacy and security, the successful implementation of homomorphic encryption stands as a testament to the enduring promise of cryptographic innovation in safeguarding the confidentiality and integrity of sensitive information.

## Conclusion

In conclusion, the implementation of homomorphic encryption within a data space using Streamlit yields a myriad of profound results that underscore the transformative potential of cryptographic techniques in safeguarding data privacy while enabling sophisticated computational analysis. From enhanced data privacy and seamless computational analysis to the preservation of data integrity and facilitation of collaborative research, the outcomes obtained illuminate the multifaceted impact of homomorphic encryption on the future of data-driven decision-making. As organizations navigate the complex landscape of data privacy and security, the successful implementation of homomorphic encryption serves as a beacon of innovation, fostering a culture of trust, transparency, and accountability in the handling of sensitive information.

Homomorphic encryption offers a powerful tool for performing computations on sensitive data while preserving privacy. Despite challenges such as computational overhead and limited functionality, ongoing research and advancements in cryptographic techniques continue to improve its efficiency and practicality, paving the way for secure and privacy-preserving data processing in various domains. 
In conclusion, homomorphic encryption stands as a testament to the ingenuity of cryptographic research in addressing the ever-evolving challenges of privacy and security in the digital age. By enabling computation on encrypted data, it offers a path forward towards a future where privacy and functionality need not be mutually exclusive. As researchers continue to refine and innovate in this field, the potential applications of homomorphic encryption are boundless, promising a world where sensitive information can be processed securely and privately, unlocking new frontiers in data-driven innovation.

For more information, refer to the [Homomorphic Encryption Standardization](https://homomorphicencryption.org/) initiative.

## The HE demonstrator

Lorem ipsum

### Given folder structure. 
The provided Streamlit folder structure organizes the files and directories of a Streamlit application. Following is the folder structer explained. Please stick to the structure and avoid adding files to the root folder.

```
Streamlit Template/
├─ config/
├─ frontend/
│  ├─ components/
│  ├─ pages/
│  │  ├─ 01_Example page 1.py
│  │  ├─ 02_Example page 2.py
│  │  ├─ 10_About page.py
│  │  └─ static/
│  └─ Home.py
├─ src/
│  ├─ example library 1
│  │  └─ main.py
│  └─ example library 2
│     └─ main.py
├─ .gitignore
├─ docker-compose.yml
├─ Makefile
├─ README.md
├─ requirements.txt
└─ setup.py
```

Here's an explanation of each component:

- **config/:** This directory typically contains configuration files for your Streamlit application. These files may include settings for deployment, environment variables, or any other configuration parameters needed for your app.

- **frontend/:** This directory houses the frontend components of your Streamlit application.

    - **components/:** Contains reusable components or widgets that can be used across different pages or sections of your application. Here, the side bar is defined to use it all over the different pages.

    - **pages/:** Contains individual Python files representing different pages or sections of your application. Each file represents a separate page, such as "Example page 1.py", "Example page 2.py", and "About page.py". Additionally, there's a subdirectory named "static/" which might hold static assets like images, data files (CSV, JSON etc.), images or video files. Use a capital letter in order to use it in the streamlit sidebar as well. Use numbers to sort pages. Numbers will be filtered out for the streamlit sidebar.

    - **Home.py:** Represents the main entry point or homepage of your Streamlit application. This is where your application might start when launched.

- **src/:** This directory contains the source code of any custom libraries or modules that your Streamlit application utilizes.

    - **example library 1/** and **example library 2/**: These directories contain example libraries or modules used within your Streamlit application. Each directory typically contains a "main.py" file, which represents the main entry point for that library or module.
  
- **.gitignore:** This file specifies patterns for files that should be ignored by Git version control. It helps in excluding unnecessary files or directories from being tracked by Git.

- **docker-compose.yml:** This file is used for defining and running multi-container Docker applications. It specifies the services, networks, and volumes required for running the Streamlit application in a Docker environment.

- **Makefile:** This file contains directives and commands for automating tasks related to building, testing, and deploying the Streamlit application. It simplifies common development tasks by providing a set of predefined commands.

- **README.md:** This is a markdown file containing documentation, instructions, or general information about your Streamlit application. It serves as a guide for developers and users who want to understand or contribute to your project.

- **requirements.txt:** This file lists all the Python dependencies required for running your Streamlit application. It typically includes the names and versions of libraries that need to be installed using pip.

- **setup.py:** This file is used for packaging and distributing your Streamlit application as a Python package. It contains metadata about your project, such as its name, version, author, and dependencies.


### How to use the demonstrator

To run the demonstrator, you have two options. Use python directly on your running system or use docker for software independency. First lets checkout the repository:

```
cd folderOfYourChoice
git init
git remote add origin https://gitlab.dlr.de/ki-scd/general/dlr-ki-streamlit-demo-template.git
git fetch
git checkout origin/main
```

#### Option 1: Vanilla python
This demonstration template option is designed to showcase the usage and simplicity of Streamlit, using Python only. Whether you're a beginner looking to learn Streamlit or an experienced developer exploring its capabilities, this template provides a solid foundation for building and experimenting with code.

##### Requirements
- python 3.10 or later  
- virtualenv or venv  

##### Installation
```sh
# create virtual environment
python -m venv .venv
# create virtual environment
source .venv/bin/activate
# install
make install
```

##### Run App

```sh
make run
```

#### Option 2: Docker
This option is designed to provide you with a seamless environment for building and deploying an interactive demonstrator using Streamlit, without having any software installed, apart from Docker. By leveraging Docker, you ensure that you can easily set up and run this template on any platform without worrying about dependencies or environment setup.

##### Requirements
Docker with Engine 19.03.0+ or later

##### Installation
Not required if docker is used and already installed.

##### Run App
```sh
make docker
```

## References

**tbd**
