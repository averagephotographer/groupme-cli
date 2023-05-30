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
			'per_page': 10
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

	def menu(self, start=0, end=5, range=5):
		if start < 0 or end < 0:
			start = 0
			end = range

		to_display = self.groups[start:end]

		while len(to_display) == 0:
			curr_len = len(self.groups)
			# get more messages
			print("getting more groups")
			page = curr_len//10 + 1
			self.get_groups(page)
			next_len = len(self.groups)

			if next_len == curr_len:
				print("no more groups")
				return self.menu(curr_len - 6, curr_len - 1, 5)			
			to_display = self.groups[start:end]
    
		for index, item in enumerate(to_display):
			print(f"{index+1}) {item}")

		val = input("Enter a command: ").strip()
		
		if val.isdigit():
			i = int(val) - 1 
			return self.groups[start+i]

		if val.startswith("next") or val == "":
			commands = val.split(' ')
			if len(commands) == 2 and commands[1].isdigit():
				range = int(commands[1])
			val = self.menu(end, end + range, range)
			return val
		
		if val.startswith("back"):
			commands = val.split(' ')
			if len(commands) == 2 and commands[1].isdigit():
				range = int(commands[1])
			val = self.menu(start - range, start, range)
			return val

		print(f"unrecognized input: {val}")
		val = self.menu(start, end, range)
