FROM python:3.8
LABEL maintainer="Robin Cole @robmarkcole"

EXPOSE 8501

RUN mkdir -p /home/streamlit
WORKDIR /home/streamlit

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /home/streamlit

ENTRYPOINT [ "streamlit", "run"]
CMD ["src/app.py"]