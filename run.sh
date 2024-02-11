#!/bin/bash

run_script() {
  python3 "$1" &
  last_pid=$!
  background_pids+=($last_pid)
}

trap_ctrl_c() {
  echo "Stopping background processes"
  for pid in "${background_pids[@]}"; do
    kill "$pid" || true
  done
  wait
  echo "Done"
  exit 0
}

trap trap_ctrl_c INT

background_pids=()
run_script "facade-service/app.py"
run_script "logging-service/app.py"
run_script "messages-service/app.py"
wait
