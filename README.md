# object-detection-app
Simple object detection app with streamlit

## Run with Docker
From the root dir:
```
    docker build -t robmarkcole/object-detection-app .
    docker run -p 8501:8501 robmarkcole/object-detection-app:latest
```
Then visit [localhost:8501](http://localhost:8501/)

## Development
Using [devcontainer](https://code.visualstudio.com/docs/remote/containers), see basic python [example repo](https://github.com/microsoft/vscode-remote-try-python) and [more advanced repo](https://github.com/microsoft/python-sample-tweeterapp). Use [this streamlit docker template](https://github.com/MrTomerLevi/streamlit-docker). Note you cannot docker run at the same time as the devcontainer as the ports clash. 