import os   
import sys
import numpy as np
import pandas as pd 

from google.cloud import storage

bucket_name="ds-str-demo-bucket"

def upload_data(source_file_name, bucket_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

data_1 = pd.DataFrame(
    
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)

data_2 = pd.DataFrame(
    
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)

data_3 = pd.DataFrame(
    
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)

data_1.to_csv('data_one.csv',index=False)
data_2.to_csv('data_two.csv',index=False)
data_3.to_csv('data_three.csv',index=False)

upload_data('data_one.csv',bucket_name,"data_one.csv")
upload_data('data_two.csv',bucket_name,"data_two.csv")
upload_data('data_three.csv',bucket_name,"data_three.csv")

def list_object(bucket_name):

    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)
    # for blob in blobs:
    #     print(blob.name[:-4])
    options = [blob.name[:-4] for blob in blobs]   
    return options 

# print(list_object(bucket_name) )       