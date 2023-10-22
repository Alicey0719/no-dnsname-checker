FROM python:3.12.0

WORKDIR /opt/app

ADD requirements.txt ./requirements.txt
ADD app/ .
# ADD flask-server /flask-server
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

ENTRYPOINT [ "python", "app.py" ] 

EXPOSE 52412