# telegram-bot
Connecting telegram to mysql database and making a log for user messages and a report system.

What is this?
This app is a simple telegram bot, abilities:
-This bot saves users menssages to a DB
-It also manage a report system handled by users
-And can do some maths

What i need:
-You need [docker](https://docs.docker.com/desktop/) app installed
-You need a bot and a token [telegram](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
-This repository inside a folder named XXX (whatever name..)
-Then you need to write the token's bot inside /app/config.json

How make it works:
- Open command shell (cmd on win, sh on linux)
- go to repo directory
- write:
  docker-compose up -d
  docker exec -it XXX_python_1
  cd app
  python3 Main.py
  
How to use it:
  Add your bot to a chat and enjoy!
  commands -> /report USER | /numreports USER | /num USER | /do MATHEMATIC EXPRESSION
