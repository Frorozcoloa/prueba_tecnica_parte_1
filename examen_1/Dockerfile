FROM python:3.10

RUN  apt-get update && apt-get upgrade -y
RUN apt-get install sqlite3
RUN pip install -U pip
RUN pip install pip-tools
WORKDIR app
COPY requierements.in requierements.in
RUN pip-compile requierements.in
RUN pip install -r requierements.txt

