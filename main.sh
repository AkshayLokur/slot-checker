#!/bin/bash
printf '%s\t' "$(date +'%Y%m%d-%H:%M:%S.%3N')"
printf "Slot checker run start...\n\n"
source /Users/akshaylokur/Work/study/slot-checker/venv/bin/activate
python /Users/akshaylokur/Work/study/slot-checker/main.py
printf '%s\t' "$(date +'%Y%m%d-%H:%M:%S.%3N')"
printf "Slot checker run finished.\n\n"
deactivate