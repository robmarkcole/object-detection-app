FROM python:3.8
LABEL maintainer="Robin Cole @robmarkcole"

EXPOSE 8501

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./src /src
ENTRYPOINT [ "streamlit", "run"]
CMD ["/src/app.py"]