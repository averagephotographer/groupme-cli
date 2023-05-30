import os
from Account import Account

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')

me = Account(TOKEN)

def print_chats():
   for chat in me.chats:
      print(chat)


    
# def menu(options, start=0, end=5, factor=5):
#     if start < 0 or end < 0:
#         start = 0
#         end = factor
    
#     # print options
#     for index, item in enumerate(options[start:end]):
#         print(f"{index+1}) {item}")

#     val = input("Enter a command: ").strip()
    
#     if val.isdigit():
#         i = int(val) - 1 
#         return options[start+i]

#     if val.startswith("next") or val == "":
#         commands = val.split(' ')
#         if len(commands) == 2 and commands[1].isdigit():
#             factor = int(commands[1])
#         val = menu(options, end, end + factor, factor)
#         return val
    
#     if val.startswith("back"):
#         commands = val.split(' ')
#         if len(commands) == 2 and commands[1].isdigit():
#             factor = int(commands[1])
#         val = menu(options, start - factor, start, factor)
#         return val

#     print(f"unrecognized input: {val}")
#     val = menu(options, start, end, factor)



group = me.menu()
str_len = int(len(group.__repr__()))
print(group)
print("#"*str_len*2)
group.get_messages()

group.display()
