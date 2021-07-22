import os   
import sys  
import glob
import numpy as np 
import pandas as pd 

import streamlit as st 
from utils import *

app_name="Streamlit-GCP-Cloud-Run"

PAGE_CONFIG ={"page_title":app_name,"layout":"wide"}
st.set_page_config(**PAGE_CONFIG) 
bucket_name="ds-str-demo-bucket"
dir = './data'

def main():

    
    st.sidebar.write(":point_down: GCP Bucket Files")
    options = list_object(bucket_name)

    # Remove Current Files
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist:
        os.remove(f)

    selected_item = st.sidebar.selectbox("select the dataset from Google Cloud Storage",options,index=0)
    st.title("Streamlit is Awesome")
    st.markdown("""
            This is a dummy/toy streamlit app to created for showcasing deployment on Google Cloud Run.
            
            [Google Cloud Run](https://cloud.google.com/run) is a managed compute platform that enables you to run containers 
            that are invocable via requests or events. Cloud Run is serverless: it abstracts away all infrastructure management, 
            so you can focus on what matters most — building great applications.
                        
            The detail process steps are listed on the following GitHub repo:
            [GCP Deployment](https://github.com/dsightsonline/streamlit_gcp_cloud_run)
    """)
    
    st.subheader("Display Selected Data From Selected CSV File : "+selected_item)
    
    # Remove Current Files
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist:
        os.remove(f)
    object_name = selected_item+".csv"
    local_path = "./data/"+object_name
    download_from_bucket(bucket_name,object_name,local_path)
    
    data=data_read(local_path) 
    st.write(" ")   
    st.dataframe(data)

    st.subheader("Area Chart  of Selected Data")
    st.write(" ")
    chart_data= data[[x for x in list(data.columns)[:3]]]
    st.area_chart(chart_data)

if __name__=="__main__":
    main()


