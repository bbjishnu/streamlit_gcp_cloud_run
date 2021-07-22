import os   
import sys 
import pandas as pd
from google.cloud import storage
from google.cloud.storage.bucket import _blobs_page_start
import streamlit as st


def download_from_bucket(bucket_name,object_name,local_name):

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(object_name)
    blob.download_to_filename(local_name)

def list_object(bucket_name):

    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)
    # for blob in blobs:
    #     print(blob.name[:-4])
    options = [blob.name[:-4] for blob in blobs]   
    return options 
@st.cache(show_spinner=False)    
def data_read(fname):
    data =pd.read_csv(fname)
    return data
