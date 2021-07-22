## Step By Step Guide For Google Cloud Run Deployment of Streamlit App

### Step 1 : Complete App and Test in Python 

- Activate and Conda Env as per **README.md**
- Test the App: **streamlit run app.py** 
- If all correct, close the app.

<br/>

### Step 2 : Create Dockerfile, Image and Do Local Test

- Go to **data_app** folder.

<br/>

- ### CREATE DOCKER IMAGE 
- **docker build -t  st_demo:v1.0 .**

<br/>

- ### LOCAL TEST OF DOCKER IMAGE 
- Create a **bash** variable 
- *MYPORT =<9090>*
- **docker run --rm  --name mytest -p 8900:\${MYPORT} -e  PORT=\${MYPORT} st_demo:v1.0**
- Exposing continer port=9090 and Host Port=8900 
- Container port=9090 is passed as environment variable to the docker file CMD command. 
- This is design is GCP specific as per the requirment of gcp cloud run.
<br/>

- ### STOP RUNNING DOCKER ONCE TEST IS DONE
- **docker stop mytest**

<br/>

### Step 3 : Activate gcloud Command Line Tool  and Push Local Image to GCP
- To install the app on  Google Cloud, need to have account and gcloud tool installed in the system. 

<br/>

- ### CONFIGURE GLCOUD 
- **gcloud init** < Set Project,Billing,  Service Account and Region and Zone> 
- exmaple to set Region as Mumbai India...
- **gcloud config set compute/region asia-south1**
- **gcloud config set compute/zone asia-south1-b**

<br/>

- ###  ENABLE CONTAINER REGISTRY AND CLOUD RUN API 
- run the following command in glocud terminal.
- **gcloud services enable run.googleapis.com containerregistry.googleapis.com**

<br/>

- ###  PUSH LOCAL DOCKER IMAGE TO GOOGLE CLOUD REGISTRY 
- Following command will allow local docker to used by gcloud tool .
- **gcloud auth configure-docker**
- Following step will create tag of the local image as per gcp requirment.
- **docker st_demo:v1.0  gcr.io/< GCP PROJECT ID > /st_demo:v1.0**
- Push Local Image to GCP Repo 
- **docker push gcr.io/< GCP PROJECT ID > /st_demo:v1.0**

### Step 4 : Finally ! Deploy on Serverless Cloud Run
- Single Line Deployment!
- **gcloud run deploy < service name >  --image < gcp image name>   --platform managed --allow-unauthenticated --region < your region > --memory 2Gi --timeout=900**
- < service name >  : Service Name User Supplied 
- < gcp image name> : Image Pushed into GCP 
- < your region >   : Region was set at the Gcloud Init.
- All Done! Within 2 -3 will see a url like below!
- **https://strealit-demo-r6nrud3izq-el.a.run.app**
- **Voila ! It's Done**