# mobsf-streamlit-scalable
# mobsf-streamlit-scalable
## ports
```
at 8000 flask app
at 8501 streamlit app
at 8888 mobsf 
```
## file uploading
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
flask app runs at 7000
mobsf at 8888->9999
streamlit 8501 automatic
```
## run mobsf usign run.bat 127.0.0.1:9999->mandatory
## status
```
until uplaoding of files and displaying them is done
```
## create route at server for uploaing files
```

```