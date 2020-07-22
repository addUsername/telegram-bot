# telegram-bot
Connecting telegram to mysql database and making a log for user messages and a report system.

## Prerequisites

-You need [docker](https://docs.docker.com/desktop/) app installed
-You need a bot and a token [telegram](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
-This repository inside a folder named XXX (whatever name..)
-Then you need to write the token's bot inside /app/config.json

## Instaling
- Open command shell (cmd on win, sh on linux)
- go to repo directory
- write:
``` Shell
  docker-compose up -d
  
  docker exec -it XXX_python_1
  ```
  ``` Shell
  cd app
  python3 Main.py
  ```
  <img src="gif.gif">
  
## Running
- Add your bot to a chat and enjoy!

  commands -> /report USER | /numreports USER | /num USER | /do MATHEMATIC EXPRESSION
