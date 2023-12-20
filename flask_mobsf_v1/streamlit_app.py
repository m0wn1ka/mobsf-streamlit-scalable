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

if st.button("Upload and scan"):
        # Perform file upload and scan
        for uploaded_file in uploaded_files:
            st.write("Uploading the file..."+uploaded_file.name)
            time.sleep(1)
            multipart_data = MultipartEncoder(fields={"file": (uploaded_file.name, uploaded_file, 'application/octet-stream')})
            headers = {'Content-Type': multipart_data.content_type}
            response = requests.post(f'{SERVER_URL}/api/v1/upload', data=multipart_data, headers=headers)
            if response.status_code == 200:
                resp = json.loads(response.text)
                st.write("Upload completed successfully...."+uploaded_file.name)
            else:
                st.write(f"Upload failed: {response.text}")
                st.stop()
                # <----------------uploading done------------->
                # <---------------scanning start--------------->
            st.write("scaning..."+uploaded_file.name)
            headers = {'Content-Type': 'application/json'}
            hash=json.loads(response.text)['hash']
            url=SERVER_URL+"/api/v1/scan"
            scan_response = requests.post(url,json={"hash":hash}, headers=headers) 
            if scan_response.status_code == 200:
                st.write("scannign is done")
            else:
                st.write("scanning fialied")
                st.stop()
                # <-----------------------scannignd end------------>
                # <----------json report start------------>
            st.write("json report generatioing.."+uploaded_file.name)
            headers = {'Content-Type': 'application/json'}
            hash=json.loads(response.text)['hash']
            st.write("used hash is "+hash)
            url=SERVER_URL+"/api/v1/report_jsonn"
            scan_response = requests.post(url,json={"hash":hash}, headers=headers) 
            if scan_response.status_code == 200:
                folder_name = "json_reports"
                file_name = os.path.join(os.getcwd(), folder_name, f"{uploaded_file.name}_report.json")

                    # Ensure the folder exists, create it if it doesn't
                os.makedirs(os.path.dirname(file_name), exist_ok=True)

                with open(file_name, "w") as out_file:
                    out_file.write(scan_response.text)
                    st.write("done writntng to file")
            # <-------scanning and savings end--------------->
                
                
              
