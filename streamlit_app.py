import streamlit as st
from google import google


### COPYPASTE CREDENTIAL SECTION
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ".googleapi_creds"
### end google creds

st.sidebar.header("Google search results")
search = st.sidebar.text_input("Enter query")
page_num = st.sidebar.number_input(label="page number", value=1, min_value=1, max_value=8)


results = google.search(search, page_num)

for res in results:
    st.write(res)



