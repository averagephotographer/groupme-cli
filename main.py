import os
from Account import Account

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')

user = Account(TOKEN)

group = user.menu()
print(group)

group.display()
