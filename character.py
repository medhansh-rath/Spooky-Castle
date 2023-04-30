class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.health = 100

    # Describe this character
    def describe(self):
      health = self.get_health
      if health() != 0:  
        print( self.name + " is here!" )
        print( self.description )
        print("")

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    def set_health(self, health):
      self.health = health

    def get_health(self):
      return self.health

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print(self.name + " says: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Hero(Character):

  enemies_to_defeat = 0

  def __init__(self, char_name, char_description):
    super().__init__(char_name, char_description)

  def describe(self):
    print("You are " + self.name + ". " + self.description)
    print("")
  
  def fight(self, inhabitant, combat_item):
    print("")
    if combat_item == inhabitant.weakness:
        print("You fend " + inhabitant.name + " off with the " + combat_item + ".")
        inhabitant.set_health(0)
        Hero.enemies_to_defeat = Hero.enemies_to_defeat - 1
        print("")
        return True
    else:
        print(inhabitant.name + " crushes you, puny adventurer")
        print("")
        self.set_health(0)
        return False

class Enemy(Character):

  def __init__(self, char_name, char_description):
    super().__init__(char_name, char_description)
    self.weakness = None
    Hero.enemies_to_defeat = Hero.enemies_to_defeat + 1

  def steal(self):
        print("You steal from " + self.name)
  
  def set_weakness(self, weakness_item):
    self.weakness = weakness_item

  def get_weakness(self):
    return self.weakness

class Friend(Character):
  def __init__(self, char_name, char_description):
    super().__init__(char_name, char_description)
    self.feeling = None

  def hug(self):
    print(self.name + " hugs you back!")

  def dance(self):
    print("You and " + self.name + " waltz along to an old but lively tune.")
    print("You spin " + self.name + " round and then you both suddenly burst laughing.")
    print(self.name + " says: " +"That was the most fun I've had in a long time! Thanks a lot!")
    print("")