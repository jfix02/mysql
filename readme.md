
___

# Database MySql


**MySQL - a free management system for relational databases, which was created by TXH to increase the processing speed of large databases**

## Installation

Use the package manager pip to install foobar.

```bash
⋅ pip install mysql-connector-python     
⋅ pip install pyTelegramBotAPI    
⋅ pip install python-telegram-bot --upgrade   
```

## Usage

```python
from concurrent.futures import process


import telebot
import mysql.connector

#Imports all 

bot = telebot.TeleBot("5525873985:AAGcvcmMYqXH3i-8cZYSeqzAGsv_xJSEVLI")

#token

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
      database='base'
)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.