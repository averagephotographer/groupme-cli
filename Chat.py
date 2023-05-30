import os
from Member import Member
import requests as r
LINK = "https://api.groupme.com/v3"
TOKEN = os.getenv('TOKEN')

class Chat():
    def __init__(self, data):
        other_name = data['other_user']['name']
        other_id = data['other_user']['id']
        self.other_user = Member(other_id, other_name)

    def __repr__(self):
        return str(self.other_user)
    
    def get_messages(self):
        json_resp = r.get(f"{LINK}/groups/{self.id}/messages?token={TOKEN}").json()
        messages_data = json_resp['response']
        for message in messages_data['messages']:
            self.messages.append(message)
