FROM postgres:16

ENV POSTGRES_USER=appuser \
    POSTGRES_PASSWORD=secret \
    POSTGRES_DB=appdb

COPY init.sql /docker-entrypoint-initdb.d/
