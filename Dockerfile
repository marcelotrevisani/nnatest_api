FROM python:3.7-alpine
MAINTAINER Marcelo Duarte Trevisani

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D nna
RUN chown -R nna:nna /vol/
RUN chmod -R 755 /vol/web

ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN mkdir /nnatest_api
WORKDIR /nnatest_api
COPY ./nnatest_api /nnatest_api

ARG RELEASE="false"
COPY ./requirements.txt /requirements.txt
COPY ./requirements_dev.txt /requirements_dev.txt
RUN mkdir -p /tmp/arca && wget -c https://github.com/marcelotrevisani/example_test_mock/archive/0.1.1.tar.gz -O /tmp/arca/arca.tar.gz
RUN tar -xvf /tmp/arca/arca.tar.gz -C /tmp/arca
RUN pip install /tmp/arca/example_test_mock-0.1.1/.
RUN if [ "${RELEASE}" = "true" ] ; then pip install -r /requirements.txt ; else pip install -r /requirements_dev.txt ; fi

RUN apk del .tmp-build-deps

USER nna
