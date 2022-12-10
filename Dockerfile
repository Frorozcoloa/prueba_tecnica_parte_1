FROM python:3.10
RUN pip install -U pip
RUN pip install pip-tools
WORKDIR app
COPY requierements.in requierements.in
RUN pip install -r requierements.txt