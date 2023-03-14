FROM ubuntu:18.04
RUN apt update -y 
RUN apt-get install python3 -y
RUN apt-get install git -y
RUN apt install -y python3-pip  python3-dev  python3-setuptools python3-venv curl 
COPY . .
RUN git clone https://github.com/cr0hn/dockerscan
# RUN export LC_ALL=C.UTF-8 && python3 dockerscan/setup.py install
RUN pip3 install markupsafe==1.1.1
RUN pip3 install Flask==0.12
RUN apt-get update -y
#RUN curl -sL https://aka.ms/InstallAzureCLIDeb |  bash
RUN curl https://releases.rancher.com/install-docker/20.10.sh | sh
RUN cd app
CMD [ "python3","app/app.py"]
