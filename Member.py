class Member():
  def __init__(self, id, nickname):
    self.id = id
    self.nickname = nickname
    
    
  def __repr__(self):
    return self.nickname
