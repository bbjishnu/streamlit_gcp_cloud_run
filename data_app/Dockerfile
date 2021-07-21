FROM python:3.7

RUN useradd −u 8877 stlrunner

USER stlrunner

ENV PORT=

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --user --no-cache-dir -r  requirements.txt 

COPY app.py . 


CMD streamlit run app.py --server.port=${PORT}  --browser.serverAddress="0.0.0.0"

