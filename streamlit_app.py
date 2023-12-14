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
                st.write("uploaded succeded  "+response.text)
            else:
                st.write(f"Upload failed: {response.text}")
                st.stop()
            # st.write("analysing")
            # headers = {'Content-Type': 'application/json'}
            # hash=json.loads(response.text)['hash']
            # scan_response = requests.get(f'{SERVER_URL}/api/v1/scan/{hash}', headers=headers) 
            # if scan_response.status_code == 200:
            #     st.write("scannign is done")
            # else:
            #     st.write("scanning fialied")
            st.write("scanning")
            headers = {'Content-Type': 'application/json'}
            hash=json.loads(response.text)['hash']
            st.write("used hash is "+hash)
            url=SERVER_URL+"/api/v1/report_jsonn"
            scan_response = requests.post(url,json={"hash":hash}, headers=headers) 
            st.write(scan_response.text)
            #st.write(scan_response)
            if scan_response.status_code == 200:
                st.write("scannign is done")
                # file_name="json_reports"+uploaded_file.name+".josn"
                # out_file = open("filname", "w") 
  
                # json.dump(scan_response, out_file, indent = 6) 
  
                # out_file.close()
            else:
                st.write("scanningfds fialied")
                
              
