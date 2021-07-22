FROM python:3.7.2

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r  requirements.txt 


ENV PORT=


COPY app.py . 
COPY utils.py . 
COPY data  ./data/

CMD streamlit run app.py --server.port=${PORT}  --browser.serverAddress="0.0.0.0"

