from room import Room
from character import Hero, Friend, Enemy
from item import Item

dining_room = Room("Dining Room")
dining_room.set_description("A large room with ornate golden decorations on each wall.")

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance.")

kitchen.link_room(dining_room, "south")
dining_room.link_room(kitchen, "north")
ballroom.link_room(dining_room, "east")
dining_room.link_room(ballroom, "west")

hero = Hero("Michael", "A seemingly ordinary boy.")

dave = Enemy("Dave", "A smelly zombie.")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_room.set_character(dave)

catrina = Friend("Catrina", "A friendly skeleton.")
catrina.set_conversation("Why hello there. Wanna dance?")
ballroom.set_character(catrina)

cheese = Item("cheese","A large and smelly block of cheese.")
kitchen.set_item(cheese)

book = Item("book", "A really good book entitled 'Knitting for dummies'.")
dining_room.set_item(book)