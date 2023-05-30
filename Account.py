import requests as r
from Group import Group
from Chat import Chat

LINK = "https://api.groupme.com/v3"

class Account():
	def __init__(self, token):
		self.token = token
		self.groups = []
		self.chats = []
		self.get_groups()
		self.get_chats()

	def get_groups(self, num=1):
		params = {
			'token': self.token,
			'page': num,
			'per_page': 200
		}
		json_resp = r.get(f"{LINK}/groups", params).json()
		groups_data = json_resp['response']

		for group in groups_data:
			self.groups.append(Group(group))

	def get_chats(self):
		json_resp = r.get(f"{LINK}/chats?token={self.token}").json()
		chats_data = json_resp['response']

		for chat in chats_data:
			self.chats.append(Chat(chat))

	def menu(self, start=0, end=5, factor=5):
		if start < 0 or end < 0:
			start = 0
			end = factor
    
		for index, item in enumerate(self.groups[start:end]):
			print(f"{index+1}) {item}")

		val = input("Enter a command: ").strip()
		
		if val.isdigit():
			i = int(val) - 1 
			return self.groups[start+i]

		if val.startswith("next") or val == "":
			commands = val.split(' ')
			if len(commands) == 2 and commands[1].isdigit():
				factor = int(commands[1])
			val = self.menu(end, end + factor, factor)
			return val
		
		if val.startswith("back"):
			commands = val.split(' ')
			if len(commands) == 2 and commands[1].isdigit():
				factor = int(commands[1])
			val = self.menu(start - factor, start, factor)
			return val

		print(f"unrecognized input: {val}")
		val = self.menu(start, end, factor)
