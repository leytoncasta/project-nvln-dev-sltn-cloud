FROM postgres:latest

ENV POSTGRES_DB=to_do_list
ENV POSTGRES_USER=adminuser
ENV POSTGRES_PASSWORD=mypassword

COPY ./tables.sql /docker-entrypoint-initdb.d/