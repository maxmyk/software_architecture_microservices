#!/bin/bash

run_script() {
  python3 "$1" $2 $3 $4 $5 $6 $7 $8 $9 &
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
run_script "facade-service/app.py" 5000 3 5001 5002 5003 2 5004 5005
run_script "logging-service/app.py" 5001 first 5701
run_script "logging-service/app.py" 5002 second 5701
run_script "logging-service/app.py" 5003 third 5701
run_script "messages-service/app.py" 5004 3 5001 5002 5003
run_script "messages-service/app.py" 5005 3 5001 5002 5003
wait
