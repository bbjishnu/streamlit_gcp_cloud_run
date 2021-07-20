## streamlit_gcp_cloud_run
This repo will provide a detailed guideline to deploy a [Streamlit](https://streamlit.io/) Data application in [Google Cloud](https://cloud.google.com/) Serverless Container Platfrom [Cloud Run](https://cloud.google.com/run).

This document has been updated with recent releases of Streamlit and GCP Cloud Run. Those who are already ahead of the curve on this topic, may take note of the fact GCP Cloud Run  has added **web socket** application support in its latest release.

### Background
This repo is organized as follows:

- **data_app** folder contains application code,requirements.txt, Dockerfile and other relevant files for development and deployment. 
- **step_by_step_guide.md** will list the steps from streamlit app creation and  testing, docker image creation, local testing  to gcp deployment. 

### Installation Process

- git clone git@github.com:dsightsonline/streamlit_gcp_cloud_run.git
- go to directory data_app
- assuming conda installed if NOT install conda from [Anaconda](https://www.anaconda.com/products/individual)
- conda create --name < my_env > python=3.x  **# create a conda env**
- conda activate my_env                      **# activate conda env**   
- pip install -r  requirments.txt            **# requirements.txt would be in data_app path**
- streamlit run app.py                       **# app will start!!, will proceed to deployent.**

### GCP Deployment 
Read the **step_by_step_guide.md** in the root path and follow along. 

### Contact 

email: bbjishnu@dsightsonline.com 
