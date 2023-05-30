import os
from Member import Member
from Message import Message
import requests as r
LINK = "https://api.groupme.com/v3"


class Group():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.most_recent_message = self.get_most_recent(data['messages'])
        self.members = []
        self.messages = []
        self.get_members(data['members'])
    
    def __repr__(self):
        return self.name
    
    def get_messages(self):
        params = {
            "token": os.getenv('TOKEN'),
            "per_page": 200
        }
        json_resp = r.get(f"{LINK}/groups/{self.id}/messages", params).json()
        messages_data = json_resp['response']
        for message in messages_data['messages']:
            self.messages.append(Message(message))

    def get_most_recent(self, messages_data):
        text = messages_data['preview']['text']
        sender = messages_data['preview']['nickname']

    def get_members(self, member_data):
        for member in member_data:
            id = member['id']
            nickname = member['nickname']

            self.members.append(Member(id, nickname))

    def display(self, start=0, end=5, range=5):
        if start < 0 or end < 0:
            start = 0
            end = range

        to_display = self.messages[start:end]

        if len(to_display) == 0:
            # get more messages
            pass
        
        for message in to_display[::-1]:
            print(message)
        
        val = input("Enter a command: ").strip()

        if val.startswith("next") or val == "":
            commands = val.split(' ')
            if len(commands) == 2 and commands[1].isdigit():
                range = int(commands[1])
            val = self.display(end, end + range, range)
            return val
        
        if val.startswith("back"):
            commands = val.split(' ')
            if len(commands) == 2 and commands[1].isdigit():
                range = int(commands[1])
            val = self.display(start - range, start, range)
            return val

        print(f"unrecognized input: {val}")
        val = self.display(start, end, range)
