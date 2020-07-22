FROM python

user root
WORKDIR /usr/src
COPY requirements.txt ./
RUN echo "+++++++++++++++++++++++++++++++++++++++++++++++"
RUN apt-get update && apt-get install -y python3 python3-pip
RUN echo "+++++++++++++++++++++++++++++++++++++++++++++++"
RUN pip3 install -r requirements.txt
RUN mkdir -p new
COPY . ./new
WORKDIR /usr/src/new
