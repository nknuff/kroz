def STANDBY():
  global command
  command = input("\nWhat will you do?\n>")
room = 0
rug = True
screwdriver = False
razor = False
soap = False
print("Welcome to Kroz! The controls are as follows: \nnorth = moves north\neast = moves east\nsouth = moves south\nwest = moves west\nup = ascend\ndown = descend\ntake [item] = takes specified item\nuse [item] on [item] = uses specified item on specified item\nmove [item] = moves specified item\nI hope you enjoy your stay!\n--------------------------------------------")
while 1 == 1:
  #hotel room
  while room == 0:
    if room == 0:
      if rug == True:
        print("\nYou awake in what seems to be a hotel room. There is a door to the west as well as a door to the north.\n\nThere is a heavy shag rug under your feet and a window to the east.")
      elif rug == False:
        print("\nYou awake in what seems to be a hotel room. There is a door to the west as well as a door to the north.\n\nThere is a heavy shag rug that has been moved to reveal a trapdoor and a window to the east.")
      STANDBY()
    if command.lower() == ("e" or "east"):
      room = 1
    elif command.lower() == ("n" or "north"):
      room = 2 
    elif command.lower() == ("w" or "west"):
      print("\nThis door is locked.")
    elif command.lower() == ("s" or "south"):
      print("\nYou cannot go this way.")
    elif command.lower() == ("u" or "up"):
      print("\nYou cannot go this way.")
    elif command.lower() == ("move rug"):
      rug = False
      print("\nWith great effort you move the rug to reveal a trap door. Where could this lead?")
    elif command.lower() == ("d" or "down"):
      if rug == True:
        print("\nYou can't go through the floor... or can you?")
      elif rug == False:
        room = 6
    else:
      print("\nNo.")
  #window
  while room == 1:
    if room == 1:
      print("\nYou look out the window and into the courtyard. There is a fire escape leading down but the window is sealed shut. In the corner is a screwdriver.")
      STANDBY()
    if command.lower() == ("e" or "east"):
      print("\nI already told you the window is sealed shut.")
    elif command.lower() == ("w" or "west"):
      room = 0 
    elif command.lower() == ("n" or "north"):
      room = 2 
    elif command.lower() == ("u" or "up"):
      print("\nYou cannot go this way.")  
    elif command.lower() == ("s" or "south"):
      print("\nYou cannot go this way.")
    elif command.lower() == ("d" or "down"):
      print("\nYou cannot go this way.")
    elif command.lower() == ("take screwdriver"):
      screwdriver = True
      print("\nYou take the screwdriver. Pro tip, tools always come in handy.")
    else:
      print("\nNo.")
  #bathroom
  while room == 2:
    if room == 2:
      print("\nYou find yourself in a bathroom. You look in the mirror and think 'Wow I'm gorgeous.' On the counter is a bar of soap as well as a razor. To your north is another door.")
      STANDBY()
    if command.lower() == ("n" or "north"):
      room = 4
    elif command.lower() == ("s" or "south"):
      room = 0
    elif command.lower() == ("take soap"):
      soap = True
      print("\nYou take the bar of soap. Cleanliness is always important.")  
    elif command.lower() == ("take razor"):
      razor = True
      print("\nYou take the razor. Please be careful, I don't want you to hurt yourself")   
    elif command.lower() == ("u" or "up"):
      print("\nYou cannot go this way.")  
    elif command.lower() == ("w" or "west"):
      print("\nYou cannot go this way.")
    elif command.lower() == ("d" or "down"):
      print("\nYou cannot go this way.")
    elif command.lower() == ("e" or "east"):
      print("\nYou cannot go this way.")
    else:
      print("\nNo.")