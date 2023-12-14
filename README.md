# mobsf-streamlit-scalable
#  uploading
```
from port 8501 user uploads 100apks 
and that will be checked whether uploaded or not
how to upload multilple files in stramlit
https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader
need to change limit of 200mb for uploading 
and set bool to true to accept multiple files
uploading is done

```
```
then on a for loop one after anothr requests.post will be sent to port 8000(flask app)
in flask app we send post/get requests to mosf (8888)
the responese will go to mobsf->flask app->streamlit
```
## ports
```
flask app runs at 8000
mobsf at 8888->9999
streamlit 8501 automatic
```
## run mobsf usign run.bat 127.0.0.1:9999->mandatory
## status
```
until uplaoding of files and displaying them is done
```
## create route at server for uploaing files
## status
```
after uplaoding files ,json response will be saved in json_Reporsts folder
```
# how to use
```
->run mobsf api at port 9999
then run python3 run_all_apps.py
goto localhost:8501(streamlit ui)
uplaod fiels
see o/p in a reports folder
```
# sample images
![image](https://github.com/m0wn1ka/mobsf-streamlit-scalable/assets/127676379/d306d729-80e1-4b83-9ee4-b39d6bb63e7f)
![image](https://github.com/m0wn1ka/mobsf-streamlit-scalable/assets/127676379/b3cabfb5-b672-4608-8d14-0f010a5eb176)
![Uploading image.png…]()



