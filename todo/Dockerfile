FROM python:3.9


RUN mkdir /src
WORKDIR /src


RUN apt-get update && apt-get upgrade -y


COPY requirements.txt ./
RUN pip3 install --no-cache -r requirements.txt


ADD . /src


COPY scripts/startup.sh /startup.sh


RUN chmod +x /startup.sh


ENTRYPOINT ["/startup.sh"]
EXPOSE 8000