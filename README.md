# Novoos-AFK-Bot
Novoos bot which notifies others that you are AFK.


# Telegram Novoos AFK Bot

Let everyone know you are Away From Keyboard


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file
. Rename sample_config.env to config.env 

`API_ID`

`API_HASH`

`SESSION`

`REDIS_URI`

`REDIS_PASSWORD`


## Features

- type .afk [Reason] to anyone private message. Example .afk Busy
- AFK mode will be activated it will auto reply to anyone's PM
- AFK mode will automatically disabled if you reply any message or send message on PM
- You can run it locally or deploy on heroku


## Local Deployment

To deploy this project run

* fill config.env file

```bash
  pip install -r requirements.txt
```

```bash
  python3 main.py 
```

## Deploy to Cloud

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Novoos/Novoos-AFK-Bot)

## Author

- [@Novoos](https://www.github.com/Novoos)
* Telegram : [@NovoosEcosystem](https://t.me/NovoosEcosystem)





