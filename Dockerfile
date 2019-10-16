FROM puckel/docker-airflow:1.10.4

USER root

RUN curl -fsSL -o go1.13.1.linux-amd64.tar.gz https://dl.google.com/go/go1.13.1.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf go1.13.1.linux-amd64.tar.gz
RUN rm go1.13.1.linux-amd64.tar.gz

ENV GOPATH=/usr/local/go/bin
ENV PATH=${GOPATH}:${PATH}
ENV PATH=${GOPATH}/bin:${PATH}

RUN apt-get update && apt-get -y install git
RUN go get -u github.com/amacneil/dbmate

USER airflow