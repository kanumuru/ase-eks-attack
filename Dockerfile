FROM ubuntu:latest
RUN apt-get update -y \
  && apt install -y python3-pip  python3-dev python3-distutils  python3-setuptools python3-venv curl 
# RUN  pip3 install awscli -y
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
RUN cd app
CMD [ "python3","app/app.py"]

