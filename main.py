from rpginfo import RPGInfo
from room import Room
from character import Hero, Enemy
from info import dining_room, kitchen, ballroom, hero, dave, catrina, cheese, book

spooky_castle = RPGInfo("The Spooky Castle")
spooky_castle.welcome()
RPGInfo.info()
RPGInfo.author = "Medhansh Rath"

current_room = kitchen
backpack = []

hero.describe()

print("There are " + str(Room.number_of_rooms) + " rooms to explore.")
print("")

while hero.health != 0 and Hero.enemies_to_defeat != 0:
  current_room.get_details()

  item = current_room.get_item()
  if item is not None:
    item.describe()

  inhabitant = current_room.get_character()
  if inhabitant is not None:
    inhabitant.describe()

  command = input("> ")

  if command in ["north", "south", "east", "west"]:
    current_room = current_room.move(command)
    print("\033[2J\033[H")

  elif command == "talk":
    print("\033[2J\033[H")
    if inhabitant is not None:
      inhabitant.talk()
  
  elif command == "fight":
    if inhabitant is not None and isinstance(inhabitant, Enemy):
      print("")
      print("What will you fight with?")
      print("")
      fight_with = input()
      if fight_with in backpack:
        if hero.fight(inhabitant, fight_with) == True:
          print("Hooray, you won the fight!")
          print("\033[2J\033[H")
          current_room.set_character(None)
        else:
          print("Oh dear, you lost the fight.")
          print("\033[2J\033[H")
      else:
        print("You don't have a " + fight_with)
        print("\033[2J\033[H")
    else:
      print("There is no one here to fight with")
      print("\033[2J\033[H")

  elif command == "dance":
    inhabitant.dance()
    print("\033[2J\033[H")
  
  elif command == "take":
    if current_room.item is not None:
      print("")
      print("You put the " + item.get_name() + " in your backpack.")
      print("\033[2J\033[H")
      backpack.append(item.get_name())
      current_room.set_item(None)

if Hero.enemies_to_defeat == 0:
  print("Congratulations, you have vanquished the enemy horde!")
  print("")
else:
  print("That's the end of the game")
  print("")

RPGInfo.credits()