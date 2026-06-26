FROM apache/hop-web:latest

USER root

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv dos2unix

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install --no-cache-dir -r /tmp/requirements.txt --break-system-packages

USER hop