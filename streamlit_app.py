import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json
import webbrowser
import time
from datetime import date
import os
st.title("hi there")
SERVER_URL="http://127.0.0.1:8000"
uploaded_files = st.file_uploader("Choose  files",accept_multiple_files=True)

if st.button("Upload"):
        # Perform file upload and scan
        for uploaded_file in uploaded_files:
            st.write("Uploading the file..."+uploaded_file.name)
            time.sleep(1)
            multipart_data = MultipartEncoder(fields={"file": (uploaded_file.name, uploaded_file, 'application/octet-stream')})
            headers = {'Content-Type': multipart_data.content_type}
            response = requests.post(f'{SERVER_URL}/api/v1/upload', data=multipart_data, headers=headers)
            if response.status_code == 200:
                st.write("Upload completed successfully.")
                resp = json.loads(response.text)
                st.write("uploaded succeded "+response.text)
            else:
                st.write(f"Upload failed: {response.text}")
    