import os
from Account import Account

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')

user = Account(TOKEN)

def print_chats():
   for chat in user.chats:
      print(chat)

group = user.menu()
print(group)
group.get_messages()

group.display()
