# mobsf-streamlit-scalable

## ports
```
flask app  at 8000
mobsf at 8888->9999
streamlit 8501 automatic
```
## what it achieves
- we can analyze a apk file using mobsf(mobile security framework) one at a time
- when we need it to scale at a large scale we can use this api
- At fronend one can drag and drop huge amount of apks and analysis will happen automatically
- a json ouput file will be generated for all of them
  


## input
- large amount of apks to analyze
## output
- after uplaoding files ,json response will be saved in json_Reporsts folder

## usage
- run mobsf api at port 9999
- run python3 run_all_apps.py
- open localhost:8501   (streamlit user interface)
- upload apks to analyze
- see output in a reports folder
- run mobsf usign run.bat 127.0.0.1:9999
## working images
![image](https://github.com/m0wn1ka/mobsf-streamlit-scalable/assets/127676379/d306d729-80e1-4b83-9ee4-b39d6bb63e7f)
![image](https://github.com/m0wn1ka/mobsf-streamlit-scalable/assets/127676379/b3cabfb5-b672-4608-8d14-0f010a5eb176)
![image](https://github.com/m0wn1ka/mobsf-streamlit-scalable/assets/127676379/f9044703-6f0a-45e2-980f-42676c100613)




