FROM centos:7
MAINTAINER nelson.goncalves@thalesgroup.com

RUN yum install -y epel-release
RUN yum install -y python-pip
RUN pip install flask redis
ADD src /src

EXPOSE 5000

CMD python /src/server.py
