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

# General imports
import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
from streamlit.components.v1 import html
from streamlit_javascript import st_javascript
import os,binascii


# Local imports
import components.layout

# External imports
import src.exampleLibrary1.main as xy

# Initial page config
st.set_page_config(
     page_title='Homomorphic Encrypted Calculator',
     layout="wide",
     initial_sidebar_state="expanded",
)

components.layout.add() # Adds logo and user name to sidebar

##########################
# Main body of page
##########################

st.title("Homomorphic Encrypted Calculator")

st.write("This homomorphic encrypted calculator allows users to perform calculations on encrypted data without decrypting it first inside a given data space. The users input will immediately encrypted and the calculator processes the operations on the encrypted data, yielding encrypted results. This ensures privacy and security of sensitive data while still allowing computations to be performed on it.")

col1, col2, col3 = st.columns(3)
with col1:
               
     st.write("---")
     
     st.subheader('Calculator')

     # input 1
     num1 = st.number_input(label="Enter first number")
     
     # input 2
     num2 = st.number_input(label="Enter second number")
     
     st.write("Operation")
     
     operation = st.radio("Select an operation to perform:",
                         ("Add", "Subtract", "Multiply (currently not supported)", "Divide (currently not supported)"))

     #### TEST Java Script

     # html("""
     # <script>
     #      console.log("Hello world!"); 
     #      alert("Hello world!"); 
     # </script>
     # """)

     # return_value = st_javascript("""await fetch("https://reqres.in/api/products/3").then(function(response) {
     #      return response.json();
     # }) """)

     # st.markdown(f"Return value was: {return_value}")
     # print(f"Return value was: {return_value}")

     #### TEST ENDE



     ans = 0
     
     def calculate():
          if operation == "Add":
               ans = num1 + num2
          elif operation == "Subtract":
               ans = num1 - num2
          elif operation == "Multiply":
               #ans = num1 * num2
               ans = "Operation currently not supported"
          elif operation=="Divide" and num2!=0:
               #ans = num1 / num2
               ans = "Operation currently not supported"
          else:
               #st.warning("Division by 0 error. Please enter a non-zero number.")
               #ans = "Not defined"
               st.warning("Operation currently not supported")
          
          
          if st.session_state.connectedClicked == True:
               st.success(f"Answer = {ans}")
          else:
               st.warning("Not connected to data space")

          st.session_state.varsEnc = [binascii.b2a_hex(os.urandom(15)), binascii.b2a_hex(os.urandom(15)), binascii.b2a_hex(os.urandom(15))]
          
     if st.button("Calculate result"):
          calculate()
     
with col2:

     st.write("---")

     st.subheader('Data in data space')

     if 'varsEnc' not in st.session_state:
          st.session_state.varsEnc = False
     else:
          if st.session_state.connectedClicked == True:
               st.write(st.session_state.varsEnc[0])
               st.write(st.session_state.varsEnc[1])
               st.write(st.session_state.varsEnc[2])
          else:
               st.warning("Not connected to data space")


with col3:
     
     st.write("---")

     st.subheader('Dataspace connection')

     if 'connectedClicked' not in st.session_state:
          st.session_state.connectedClicked = False

     if 'disconnectedClicked' not in st.session_state:
          st.session_state.disconnectedClicked = False

     def click_greenButton():
          st.session_state.connectedClicked = True
          st.session_state.disconnectedClicked = False

     def click_redButton():
          st.session_state.disconnectedClicked = True
          st.session_state.connectedClicked = False

     # Define custom CSS for buttons 
     st.markdown("""
          <style>.element-container:has(#greenButton) + div button {
               /* APPLY YOUR STYLING HERE */
               background-color: #04AA6D;
               color: white;
          }</style>
     """, unsafe_allow_html=True)
     # Apply CSS on Button
     st.markdown('<span id="greenButton"></span>', unsafe_allow_html=True)
     st.button('Connect to dataspace', on_click=click_greenButton)

     # Define custom CSS for buttons 
     st.markdown("""
          <style>.element-container:has(#redButton) + div button {
               /* APPLY YOUR STYLING HERE */
               background-color: red;
               color: white;
          }</style>
     """, unsafe_allow_html=True)
     # Apply CSS on Button
     st.markdown('<span id="redButton"></span>', unsafe_allow_html=True)
     st.button('Disconnect to dataspace', on_click=click_redButton)

     if st.session_state.connectedClicked == True:
          # The message and nested widget will remain on the page
          st.text('Status: 🟩 Connected')
     elif st.session_state.disconnectedClicked == True:
          st.text('Status: 🟥 Disconnected ')
     else:
          st.text('Press "Connect to dataspace"')

