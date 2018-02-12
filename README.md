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
| /language | choose language(EN, RU)|

For using bot you need to press "start" button and enter your city name

### Installing 

I use for this bot python 3.5 and libs from requirements.txt

OS - Linux Mint 18.3

DB - MongoDB

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

- create file in project's root directory my_constants.py with your telegram bot token
```
token = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
```

- install mongodb. I use mongo for data storage about user language choose

```sh
sudo apt-get install mongodb
```

- mongo config:
```
host:localhost,
port:27017,
database: telegram_weather_db,
collection: mycollection
```

- run bot :
```
python telegram_bot.py
```

#### Additional

I run this bot on my AWS as daemon.

```
(.env_telegram_bot) $ python telegram_bot.py &
```
(& - ampersand symbol in the end)


On my local machine I used for it supervisor:
```sh
sudo apt-get install supervisor
sudo service supervisor start
```

Supervisor config(in /etc/supervisor/conf.d/telegram_bot.conf)

```
[program:telegram_bot]
priority=10
command=/home/ubuntu/my_program/bohdan_weather_bot/.env_telegram_bot/bin/python /home/ubuntu/my_program/bohdan_weather_bot/telegram_bot.py
user=root
autostart=true
autorestart=true
startsecs = 5
stderr_logfile = /home/ubuntu/my_program/bohdan_weather_bot/logs/err_logs
stdout_logfile = /home/ubuntu/my_program/bohdan_weather_bot/logs/out_logs
```
 
[stackoverflow - python in crontab](https://stackoverflow.com/questions/8727935/execute-python-script-on-crontab)

[stackoverflow - python as daemon](https://stackoverflow.com/questions/1603109/how-to-make-a-python-script-run-like-a-service-or-daemon-in-linux)

[Crontab – Quick Reference](http://www.adminschoice.com/crontab-quick-reference)

#### Contact

You can contact with me:

[twitter](https://twitter.com/bohdankokovych)
