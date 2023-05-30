import os
from Account import Account

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')

me = Account(TOKEN)

def print_chats():
   for chat in me.chats:
      print(chat)

group = me.menu()
str_len = int(len(group.__repr__()))
print(group)
print("#"*str_len*2)
group.get_messages()

group.display()
