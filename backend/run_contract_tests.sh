#!/usr/bin/env bash

PACT_LOCATION="../frontend/pact/pacts/frontend-backend.json"
FLASK_PORT=8989

FLASK_APP=backend poetry run flask run --port $FLASK_PORT > /dev/null 2> /dev/null &
FLASK_PID=$!

poetry run pact-verifier --provider-base-url=http://localhost:$FLASK_PORT --pact-url=$PACT_LOCATION
KILL $FLASK_PID
