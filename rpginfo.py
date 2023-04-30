class RPGInfo():

  author = "Anonymous"

  def __init__(self, game_title):
    self.title = game_title
   
  def welcome(self):
    print("Welcome to " + self.title)
    print("")
  
  @staticmethod
  def info():
    print("Made using the OOP RPG game creator (c) me")
    print("")

  @classmethod
  def credits(cls):
    print("Thank you for playing!")
    print("")
    print("Created by " + cls.author + ".")