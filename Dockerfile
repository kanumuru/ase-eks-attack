FROM ubuntu:latest
RUN apt-get update -y \
  && apt install -y python3-pip  python3-dev python3-distutils  python3-setuptools python3-venv curl 
# RUN  pip3 install awscli -y
COPY . .
RUN pip3 install -r requirements.txt
RUN apt-get update -y
RUN  apt install curl -y
RUN curl -sL https://aka.ms/InstallAzureCLIDeb |  bash
RUN curl -fsSL https://get.docker.com -o get-docker.sh 
RUN sh get-docker.sh
RUN cd app
CMD [ "python3","app/app.py"]

