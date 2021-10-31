#!/usr/bin/env bash
session="barcode"
SESSIONEXISTS=$(tmux list-sessions | grep $SESSION)
if [ "$SESSIONEXISTS" = "" ]
	tmux new-session -d -s $session
	tmux send-keys 'cd backend' C-m 'poetry run flask run' C-m
	tmux split-window -v
	tmux send-keys 'cd frontend' C-m 'yarn start' C-m
fi
tmux attach-session -t $SESSION:0
