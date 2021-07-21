import os   
import sys  
import numpy as np 
import pandas as pd 

import streamlit as st 

app_name="Streamlit-GCP-Cloud-Run"

PAGE_CONFIG ={"page_title":app_name,"layout":"wide"}
st.set_page_config(**PAGE_CONFIG) 

def main():

    st.sidebar.write(":point_down: GCP Bucket Files")
    selected_item = st.sidebar.selectbox("select the dataset",["A","B","C"],index=1)
    st.title("Streamlit is Awesome")
    st.markdown("""
            This is a dummy/toy streamlit app to created for showcasing deployment on Google Cloud Run.
            
            [Google Cloud Run](https://cloud.google.com/run) is a managed compute platform that enables you to run containers 
            that are invocable via requests or events. Cloud Run is serverless: it abstracts away all infrastructure management, 
            so you can focus on what matters most — building great applications.
                        
            The detail process steps are listed on the following GitHub repo:
            [GCP Deployment](https://github.com/dsightsonline/streamlit_gcp_cloud_run)
    """)
   
    st.write(selected_item)
    st.subheader(":point_down: Display Selected Files")
    st.write("")
    df = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

    # st.dataframe(df.style.highlight_max(axis=0))
    st.dataframe(df)

    st.subheader("Display Chart of Selected Data")
    chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
    st.area_chart(chart_data)

if __name__=="__main__":
    main()


