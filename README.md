
# Slot checker for WAANGOO :)

## Pre-requisite softwares/utilities on machine
- python 3
- pip
- virtualenv
- Chrome browser
- Chrome browser driver
	- https://sites.google.com/a/chromium.org/chromedriver/downloads
- Cron scheduler

## Configuration
1. `git clone git@github.com:AkshayLokur/slot-checker.git`
2. `cd slot-checker`
3. `virtualenv venv`
4. `pip install -r requirements.txt`
5. `crontab -e`
6. Add following entry to crontab and save: 
`*/5 * * * * /Users/akshaylokur/Work/study/slot-checker/main.sh`

You are all set! Utility should bip a sound when slots are available!

Enjoy :)