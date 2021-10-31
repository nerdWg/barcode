#!/usr/bin/env bash

trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM

PACT_LOCATION="../frontend/pact/pacts/frontend-backend.json"
FLASK_PORT=41809
export FLASK_ENV=development

poetry run flask run --port $FLASK_PORT > /dev/null 2> /dev/null &
FLASK_PID=$!

poetry run pact-verifier --provider-base-url=http://localhost:$FLASK_PORT --pact-url=$PACT_LOCATION
kill $FLASK_PID
