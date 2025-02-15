FROM python:3.12-slim

WORKDIR project

COPY . /project

# RUN apt-get update -y && \
#    apt-get upgrade -y && \
#    apt-get install -y build-essential


CMD ["tail", "-f", "/dev/null"]