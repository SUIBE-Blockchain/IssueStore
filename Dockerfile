FROM python:3.7-alpine

COPY ./requirements.txt /usr/src/requirements.txt

RUN pip install -r /usr/src/requirements.txt

COPY ./IssueStore /usr/src/IssueStore

COPY ./docker-entrypoint.sh /usr/src/docker-entrypoint.sh

RUN chmod 777 /usr/src/docker-entrypoint.sh

WORKDIR /usr/src

EXPOSE 8080

CMD ["./docker-entrypoint.sh"]
