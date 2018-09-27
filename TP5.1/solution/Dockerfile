FROM centos:7
LABEL maintainer="nelson.goncalves@thalesgroup.com"
RUN yum install -y epel-release
RUN yum install -y python-pip
RUN pip install flask
ADD src /src
EXPOSE 5000
CMD python /src/server.py
