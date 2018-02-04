## Bohdan weather telegram bot

Hello! I create this bot for fun and for my personal needs.

This is telegram bot-parser. 
It can find weather from this service:
[foreca.com](https://www.foreca.com)

#### Bot commands

| Command | Description |
| ------- | ----------- |
| /help   | display how can you use bot|
| /start  | the same |

For using bot you need to press "start" button and enter your city name

### Installing 

I use for this bot python 3.5 and libs from requirements.txt

OS - Linux Mint 18.3

Steps:

- create virtualenv:

```sh
$ virtualenv -p python3.5 .env_telegram_bot
```

- start use this virtual environment
 
 ```sh
$ source .env_telegram_bot/bin/activate
```

- install all dependencies
```sh
$ pip install -r requirements.txt
```

- create file my_constants.py with your telegram bot token
```
token = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
```

- run bot 
```
python telegram_bot.py
```

####Additional

I run this bot on my AWS as daemon.
I used for it cron:
```
crontab -e
```
and add my script execution
 
[stackoverflow - python in crontab](https://stackoverflow.com/questions/8727935/execute-python-script-on-crontab)

[stackoverflow - python as daemon](https://stackoverflow.com/questions/1603109/how-to-make-a-python-script-run-like-a-service-or-daemon-in-linux)

[Crontab – Quick Reference](http://www.adminschoice.com/crontab-quick-reference)

####Contact

You can contact with me:

[twitter](https://twitter.com/bohdankokovych)
