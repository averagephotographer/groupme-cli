from Member import Member
from datetime import datetime

class Message():
    def __init__(self, message_data):
        self.id = message_data['id']
        self.text = message_data['text']
        self.favorited_by = message_data['favorited_by']
        self.created_at = message_data['created_at']

        sender_name = message_data['name']
        sender_id = message_data['sender_id']
        self.sender = Member(sender_id, sender_name)

    def __repr__(self):
        datetime_obj=datetime.fromtimestamp(self.created_at)
        return str(f"{self.sender} - {datetime_obj.date()} {datetime_obj.time()}\n{self.text}\n")
