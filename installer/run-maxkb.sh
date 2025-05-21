#!/bin/bash
rm -f /opt/aisisstant/app/tmp/*.pid
# Start postgresql
docker-entrypoint.sh postgres -c max_connections=${POSTGRES_MAX_CONNECTIONS} &
sleep 10
# Wait postgresql
until pg_isready --host=127.0.0.1; do sleep 1 && echo "waiting for postgres"; done

# Start MaxKB
python /opt/aisisstant/app/main.py start