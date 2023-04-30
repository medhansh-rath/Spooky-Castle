from room import Room
from character import Hero, Friend, Enemy
from item import Item

#https://i.pinimg.com/originals/54/89/1c/54891c030ba74d7e0a9faecddf03c5e2.jpg
#https://www.british-history.ac.uk/vch/hunts/vol3/pp75-86
#https://www.british-history.ac.uk/rchme/hunts/pp167-176

portico = Room("Portico")
portico.set_description("A large portico with Doric columns and a large flight of steps.")

white_hall = Room("White Hall")
white_hall.set_description("The White Hall has Ionic pilasters flanking the doors, a deep cornice and a coved ceiling.")

drawing_room = Room("Drawing Room")
drawing_room.set_description("The former billiard room.")

courtyard = Room("Courtyard")
courtyard.set_description("A large open space to relax.")

dining_room = Room("Dining Room")
dining_room.set_description("A large room with ornate golden decorations on each wall.")

green_drawing_room = Room("Green Drawing Room")
green_drawing_room.set_description("A drawing room, but green.")

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance.")

master_bedroom = Room("Master Bedroom")
master_bathroom = Room("Master Bathroom")
master_balcony = Room("Master Balcony")

guest_bedroom = Room("Guest Bedroom")
guest_bathroom = Room("Guest Bathroom")
guest_balcony = Room("Guest Balcony")

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