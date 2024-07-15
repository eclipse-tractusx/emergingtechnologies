# Demonstrator Data Quality (DLR)

***

## Description
This demonstrator provides a simple framework for setting up general data quality evaluation via Python
An exemplary completeness evaluation is provided in a Streamlit app, showing the effect of degraded quality
on completeness measures.
The Python framework sets up basic classes for implementing further quality characteristics and measures on
(structured) data.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Authors
Lars Steffens, Ronja Langrock, Andreas Wolff, Dr. Michael Karl<br>
[Deutsches Zentrum für Luft- und Raumfahrt eV (DLR)](https://www.dlr.de/en)<br>
[Institute for AI Safety and Security](https://www.dlr.de/en/ki), Department [Safety-Critical Data Infrastructures](https://www.dlr.de/en/ki/about-us/departments/safety-critical-data-infrastructure)

## Basic documentation of the repository, its content and its structure
The repository in the src folder consists of the streamlit frontend code as well as the backend code.
Images used by the frontend are stored in the resources folder. 

## Installation instructions
The demonstrator needs a Python 3.11 installation, using an environment to be set up via
```
pip install -r requirements.txt
```
The demonstrator code is started via
```
streamlit run .\src\main.py
```
to run as an app in the browser.

## Usage examples and intended use of your product
The frontend code can be used as a guideline to utilize the backend package functionality. 

### Backend Classes: Data

**Data Source:** A data source returns a data object. Provided is numerical data and data from csv files.

**Data:** data object, implemented as an encapsulated pandas data frame.

**Processing:** Any functionality that operates on data a data object and returns another data object. For instance
a process that deliberately degradates data in a specific way. 

<img src="src/resources/schematics_data.jpg" width="50%" alt="backend: data, data sources, and data processing" />

### Backend Classes: Quality
**Quality Measure:** A class encapsulating a data quality measure function on a data object.
It generates a Quality Report object.

**Quality Characteristic:** A class describing a data quality characteristic.
It combines one or several Quality Measures and combines their resulting reports into one for the quality characteristic.

**Quality Model:** A class describing a quality model.
It combines one or several Quality Characteristics and combines their resulting reports into one complete report
describing the data as a whole.

**Report:** A class encapsulating the quality report of the evaluation.

<img src="src/resources/schematics_data_quality.jpg" width="50%" alt="backend: quality model, quality characteristics, measures, and report" />

## License information
Copyright (c) 2024 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Apache License, Version 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.
Copyright (c) 2024 Lars Steffens, German Aerospace Center (DLR e.V.)

## Contact information
Lars Steffens (lars.steffens@dlr.de)