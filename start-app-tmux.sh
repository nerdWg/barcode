#!/usr/bin/env bash
SESSION="barcode"
SESSIONEXISTS=$(tmux list-sessions | grep $SESSION)
if [ "$SESSIONEXISTS" = "" ]; then
  tmux new-session -d -s $SESSION
  tmux send-keys 'cd backend' C-m 'FLASK_ENV=development poetry run flask run' C-m
  tmux split-window -v
  tmux send-keys 'cd frontend' C-m 'yarn start' C-m
fi
tmux attach-session -t $SESSION:0
