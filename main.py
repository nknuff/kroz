import time
import random
#to-do list!
#finsih room dialouge
#add and balance all items (add more red herings maybe?)

def STANDBY():
  global command, turn
  if room != 101:
    command = input("\nWhat will you do?\n>")
    turn = turn + 1
    if command.lower() == "use razor on soap":
      if (razor == True) and (soap == True):
        if key == False:
          SOAPKEY()
    if command.lower() == "i":
      if screwdriver:
        print("screwdriver")
      if razor:
        print("razor")
      if soap:
        print("soap")
      if key:
        print("key")
      if rock:
        print("rock")
      if cutlass:
        print("cutlass")
      if longsword:
        print("longsword")
      if katana:
        print("katana")
      if crowbar:
        print("crowbar")
      if banana:
        print("banana")
      if crowbar:
        print("crowbar")
      if elife:
        print("extra life")
      if pickaxe:
        print("pickaxe")
      if geode:
        print("geode")
      if gem:
        priint("gem")
def QUIT():
  exit()
def RESET():
  #variable declaration
  global room, rug, screwdriver, razor, soap, key, rock, string, cutlass, longsword, katana, panel, crowbar, banana, monkey, screen, room0, room1, window, room2, room4, room3, hallwayCounter, room6, room7, vent, room5, room8, room9, room10, room11, room12, room13, room14, room15, room16, room17, room18, room19, room20, room21, room22, room23, room24, room25, room26, room27, room28, room29, room30, room31, room32, room33, portalUse, turn, gate, elife, pickaxe, geode, gem, caveman, pig, basilisk, rancor, icicles
  #item setup
  rug = True
  screwdriver = False
  razor = False
  soap = False
  key = False
  rock = False
  string = True
  cutlass = False
  longsword = False
  katana = False
  panel = True
  crowbar = False
  banana = False
  screen = True
  window = True
  vent = True
  gate = True
  elife = False
  pickaxe = False
  geode = False
  gem = False
  icicles = True
  #room setup
  room = 0
  room0 = False
  room1 = False
  room2 = False
  room3 = False
  room4 = False
  room5 = False
  room6 = False
  room7 = False
  room8 = False
  room9 = False
  room10 = False
  room11 = False
  room12 = False
  room13 = False
  room14 = False
  room15 = False
  room16 = False
  room17 = False
  room18 = False
  room19 = False
  room20 = False
  room21 = False
  room22 = False
  room23 = False
  room24 = False
  room25 = False
  room26 = False
  room27 = False
  room28 = False
  room29 = False
  room30 = False
  room31 = False
  room32 = False
  room33 = False
  #int setup
  hallwayCounter = 0
  portalUse = 5
  turn = 0
  #mob setup
  monkey = True
  caveman = True
  pig = True
  basilisk = True
  rancor = True
def YOUDIED():
  global elife
  if elife == False:
    print("\nCongrats you died. Maybe try being better?\nWould you like to try again?")
    restart = input("y or n > ")
    if restart == "y":
      RESET()
    elif restart == "n":
      print("What a party pooper.")
  elif elife == True:
    print("\nSadly, you died. But luckily, you have an extra life! Lucky duck! You spawn back where you died, ready to face the world again!")
    time.sleep(3)
    elife = False
def SOAPKEY():
  global key
  key = True
  print("\nNow you are a smart cookie. Inside the soap is a small key.")
def PORTAL():
  global room, portalUse
  print("\nvwoooop! You go through the portal and are transported to a random room!")
  room = int(random.random() * 33)
  portalUse = portalUse - 1
  print("\nYou have "+str(portalUse)+" portal uses left.")
RESET()
print("Welcome to Kroz! The controls are as follows: \nnorth = moves north\neast = moves east\nsouth = moves south\nwest = moves west\nup = ascend\ndown = descend\ntake [item] = takes specified item\nuse [item] = uses specified item\nuse [item] on [item] = uses specified item on specified item\nmove [item] = moves specified item\ninspect [item] = inspects specified item\ni = see inventory\nI hope you enjoy your stay!\n--------------------------------------------")
while 1 == 1:
  while room == 0:
    if room == 0:
      print("\nMove = " + str(turn))
      print("\nHOTEL ROOM 47")
      if rug == True:
        if room0 == False:
          print("You awake in what seems to be a hotel room. There is a door to the west as well as a door to the north.\nThere is a heavy shag rug under your feet and a window to the east.")
          room0 = True
        elif room0 == True:
          print("There is a door to the west as well as a door to the north.\nThere is a heavy shag rug under your feet and a window to the east.")
      elif rug == False:
        if room0 == False:
          print("You awake in what seems to be a hotel room. There is a door to the west as well as a door to the north.\nThere is a heavy shag rug that has been moved to reveal a trapdoor and a window to the east.")
          room0 = True
        elif room0 == True:
          print("There is a door to the west as well as a door to the north.\nThere is a heavy shag rug that has been moved to reveal a trapdoor and a window to the east.")
      STANDBY()
    if command.lower() == "east" or command.lower() == "e":
      room = 1
    elif command.lower() == "north" or command.lower() == 'n':
      room = 2 
    elif command.lower() == "west" or command.lower() == "w":
      room = 3
    elif command.lower() == "south" or command.lower() == "s":
      print("\nYou cannot go this way.")
    elif command.lower() == "up" or command.lower() == "u":
      print("\nYou cannot go this way.")
    elif command.lower() == ("move rug"):
      rug = False
      print("\nWith great effort you move the rug to reveal a trap door. Where could this lead?")
    elif command.lower() == "d" or command.lower() == "down":
      if rug == True:
        print("\nYou can't go through the floor... or can you?")
      elif rug == False:
        room = 6
    else:
      print("\nNo.")
  #sunroom 1
  while room == 1:
    if room == 1:
      print("\nMove = " + str(turn))
      print("\nSUNROOM")
      if room1 == False:
        if screwdriver == False:
          print("You walk through a pair of french doors to reveal a cozy sunroom filled with houseplants.\nThere is a window on the east side of the room, and the doors you came into to the west.\nIn the corner is a screwdriver.")
          room1 = True
        elif screwdriver == True:
          print("You walk through a pair of french doors to reveal a cozy sunroom filled with houseplants.\nThere is a window on the east side of the room, and the doors you came into to the west.")
          room1 = True
      elif room1 == True:
        if screwdriver == False:
          print("There is a window on the east side of the room, and the doors you came into to the west.\nIn the corner is a screwdriver.")
        elif screwdriver == True:
          print("There is a window on the east side of the room, and the doors you came into to the west.")
      STANDBY()
    if command.lower() == "east" or command.lower() == 'e':
      if window == True:
        print("\nThere is a window here.")
      elif window == False:
        room = 17
    elif command.lower() == "west" or command.lower() == "w":
      room = 0 
    elif command.lower() == "north" or command.lower() == 'n':
      print("\nYou cannot go this way.") 
    elif command.lower() == "up" or command.lower() == "u":
      print("\nYou cannot go this way.")  
    elif command.lower() == "south" or command.lower() == "s":
      print("\nYou cannot go this way.")
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "take screwdriver":
      screwdriver = True
      print("\nYou take the screwdriver. Pro tip, tools always come in handy.")
    elif command.lower() == "inspect window" or command.lower() == "i window" or command.lower() == "open window":
      if window == True:
        print("\nThe window seems unopenable by any means other than a solid object such as a rock...")
      if window == False:
        print("\nBe careful climbing through you could cut yourself on the sharp glass. Maybe you should use a cloth or something to protect yourself.")
    elif command.lower() == "use rock on window":
      if rock == True and window == True:
        print("\nYou throw the rock at the window shattering it.")
        rock = False
        window = False
      elif rock == False and window == True:
        print("\nGo find Dwayne and try again.")
      elif rock == False and window == False:
        print("\nThe window is open and you do not have a rock or apparently a brain.")
      elif rock == True and window == False:
        print("\nThe window is already open. Also how did did get this line of dialouge it is logically impossible to get i am proud of u <3.")
    else:
      print("\nNo.")
  #bathroom 2
  while room == 2:
    if room == 2:
      print("\nMove = " + str(turn))
      print("\nBATHROOM")
      if room2 == False:
        print("You find yourself in a bathroom. You look in the mirror and think 'Wow I'm gorgeous.' On the counter is a bar of soap as well as a razor. To your north is another door.")
        room2 = True
      elif room2 == True:
        if soap == False and razor == False:
          print("On the counter is a bar of soap as well as a razor. To your north is another door.")
        elif soap == True and razor == False:
          print("On the counter is a razor. To your north is another door.")
        elif soap == False and razor == True:
          print("On the counter is a bar of soap. To your north is another door.")
        elif soap == True and razor == True:
          print("There is nothing on the counter. To your north is another door.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      room = 4
    elif command.lower() == "s" or command.lower() == "south":
      room = 0
    elif command.lower() == ("take soap"):
      soap = True
      print("\nYou take the bar of soap. Cleanliness is always important.") 
    elif command.lower() == ("take razor"):
      razor = True
      print("\nYou take the razor. Please be careful, I don't want you to hurt yourself")   
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      print("\nYou cannot go this way.")
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      print("\nYou cannot go this way.")
    elif command.lower() == "use razor on soap":
      SOAPKEY()
    else:
      print("\nNo.")
  #hallway 3
  while room == 3:
    if room == 3:
      print("\nMove = " + str(turn))
      print("\nHALLWAY")
      if hallwayCounter >= 21:
        print("\nYour vision goes dark as your reality ceases to exist. You have broken the space-time continum. I suppose this qualifies at escaping?")
        time.sleep(3)
        hallwayCounter = 0
        room = 101
      if hallwayCounter == 5:
        print("\nI told you this hallway was endless please go another direction.")
      if hallwayCounter == 10:
        print("\nPlease turn around this is getting out of hand.")
      if hallwayCounter == 15:
        print("\nYour vision start to get blurry and you begin to see stars.")
      if hallwayCounter == 20:
        print("\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
      if room3 == False and room !=101:
        print("You enter a hallway that seems to extend forever in both directions. However there is another door on the other side of the hallway.")
        room3 = True
      elif room3 == True and room !=101:
        print("The hallway seemingly extends forever in both directions. There are doors to the east and west however.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north" and room != 101:
      hallwayCounter = hallwayCounter + 1
      room = 3
    elif (command.lower() == "s" or command.lower() == "south") and room != 101:
      hallwayCounter = hallwayCounter + 1
      room = 3
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      room = 7
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      room = 4 
    else:
      if room != 101:
        print("\nNo.")
  #dark/sword room 4
  while room == 4:
    if room == 4:
      print("\nMove = " + str(turn))
      print("\nHOTEL ROOM 48")
      if room4 == False:
        if string == True:
          print("You enter a room of complete darkness, and cannot tell your right from your left.")
        elif string == False:
          print("A single light bulb hanging by a wire illuminates the room. You enter a room that looks more or less like yours. The only difference is the presence of a display case of sorts filled with swords from all around the globe. You can see doors in every direction except east.")
          room4 = True
      elif room4 == True:
        print("There is a case displaying swords in the corner. There are doors in every direction except east.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      if string == True:
        print("\nYou cannot go this way.") 
      elif string == False:
        room = 5
    elif command.lower() == "s" or command.lower() == "south":
      if string == True:
        room = 3 
      elif string == False:
        room = 2
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      if string == True:
        room = 5
      elif string == False:
        room = 3
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      if string == True:
        room = 2
      elif string == False:
        print("\nI literally said there is no door here.")
    elif command.lower() == "inspect swords" or command.lower() == "i swords" or command.lower() == "inspect case" or command.lower() == "i case":
      if (longsword == True) or (katana == True) or (cutlass == True):
        print("\nYou already have a sword your greedy pig.")
      else:
        print("\nYou approach the sword case to take a closer look. You see 3 different types of swords: a longsword, a katana, and a cutlass. There is a sign on the case that reads the following: 'Choose one, but choose wisely'")
        sword = input("\nWhat blade will you choose?\n>")
        if sword.lower() == "longsword":
          longsword = True
          print("\nAh the longsword. Heavy in damage but slow in attack. Wise choice.")
        elif sword.lower() == "katana":
          katana = True
          print("\nThe samurai's weapon. Perfectly balenced in both damage and speed, as all things should be.")
        elif sword.lower() == "cutlass":
          cutlass = True
          print("\nThe sword of the seas. This one favors speed and agility over damage.")
        else:
          print("\nPick a sword or you might regret it.")
    else:
      print("\nNo.")
  #closet 5
  while room == 5:
    if room == 5:
      print("\nMove = " + str(turn))
      print("\nCLOSET")
      if string == True:
        print("You stumble through a door and into a small, tight closet. You can feel a string in front of you and an exposed brick wall to your north.")
      if string == False:
        print("You are in a small, tight closet. You can feel a string in front of you and an exposed brick wall to your north.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      print("\nYou cannot go this way.")
    elif command.lower() == "s" or command.lower() == "south":
      room = 4
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      print("\nYou cannot go this way.")
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      print("\nYou cannot go this way.")
    elif command.lower() == ("use string"):
      string = False
      print("\nYou pull on the string. You hear a click from the other room.") 
    else:
      print("\nNo.")
  #dungeon entrance 6
  while room == 6:
    if room == 6:
      print("\nMove = " + str(turn))
      print("\nDUNGEON ENTRANCE")
      if room6 == True:
        print("Torches light several passages to the west, east, and south. There is also the ladder you came down on.")
        if monkey == False:
          print("\nOne of the heads, which is shaped like a monkey, seems to emit a strange glow.")
      if room6 == False:
        print("You descend down a rickety old ladder into a damp, chilly chamber. The heads of several horrifying creatures are encased in stone and mounted on the walls. Moss and ferns inhabit this narrow chamber, and torches light several passages to the east, west, and south.")
        if monkey == False:
          print("\nOne of the heads, which is shaped like a monkey, seems to emit a strange glow.")
        room6 = True
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      print("\nYou cannot go this way.")
    elif command.lower() == "s" or command.lower() == "south":
      room = 26
    elif command.lower() == "u" or command.lower() == "up":
      room = 0  
    elif command.lower() == "w" or command.lower() == "west":
      room = 29
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      room = 18
    elif command.lower() == "inspect heads" or command.lower() == "i heads" or command.lower() == "i creatures" or command.lower() == "inspect creatures":
      print("\nThere are five total stone heads, each of a different creture. There is a monkey, a ---, a ---, a ---, and a ---. \nUpon further inspection, the heads seem to have some kind of mechanism behind them. I wonder hwo to activate it...")
    else:
      print("\nNo.")
  #movie theater 7
  while room == 7:
    if room == 7:
      print("\nMove = " + str(turn))
      print("\nMOVIE THEATER")
      if room7 == False:
        print("You enter a movie theater playing an old black and white film on a screen to the west. As you walk around the empty theater, you get the feeling that someone is watching you. The only door you see is the door you came in from. However, there is an air vent to the north and what appears to be a sewer grate in the floor.")
        room7 = True
      elif room7 == True:
        print("You still can't shake the feeling that someone is watching you. There is an air vent to the north, a sealed grate in the floor, a door to the east, and a screen to the west.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      if vent == True:
        print("\nThere is a vent here.")
      elif vent == False:
        room = 9
    elif command.lower() == "s" or command.lower() == "south":
      print("\nYou cannot go this way.")
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      if screen == True:
        print("\nThere is a screen here. I believe it is playing Modern Times.")
      elif screen == False:
        room = 8
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      room = 3 
    elif command.lower() == "inspect vent" or command.lower() == "i vent":
      print("\nThe vent is firmly screwed in place. Maybe a tool would help open this.")
    elif command.lower() == "inspect grate" or command.lower() == "i grate":
      print("\nThe grate is sealed shut and there is no apparent way to open it. Maybe from the other side...")
    elif command.lower() == "use screwdriver on vent":
      if screwdriver == True:
        print("\nLucky you, you have a screwdriver and swiftly open the vent. I told you that tools come in handy.")
        vent = False
      else:
        print("\nDon't try to use things you don't have. Cheater.")
    elif command.lower() == "inspect screen" or command.lower() == "i screen":
      print("\nYou walk up to the screen. There seems to be a room on the other side.")
    elif command.lower() == "use razor on screen": 
      if razor == True and screen == True:
        screen = False
        print("\nYou slice open the fabric film screen to reveal another room to the west.")
      elif razor == True and screen == False:
        print("\nYou seem to have already done this.")
      else:
        print("\nYou dont have a razor silly.")
    else:
      print("\nNo.")
  #Portal Room 8
  while room == 8:
    if room == 8:
      print("\nMove = " + str(turn))
      print("\nPORTAL ROOM")
      if room8 == False:
        print("You squeeze through the whole you made with your razor into a clean, white room. The only item in the room is what looks like a portal on the opposite end.")
      if room8 == True:
        print("A portal lies to your west. It seems happy to see you.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      print("\nYou cannot go this way.")
    elif command.lower() == "s" or command.lower() == "south":
      print("\nYou cannot go this way.")
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      PORTAL()
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      room = 7
    else:
      print("\nNo.")
  #south vent 9 
  while room == 9:
    if room == 9:
      print("\nMove = " + str(turn))
      print("\nSOUTH VENT")
      if room9 == False:
        print("You enter a small, tight air duct, with barely enough room to crawl through. The duct continues to the north, and you can hear a strange noise coming from that direction.")
        room9 = True
      elif room9 == True:
        print("The duct continues to the north, and you can hear a strange noise coming from that direction.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      room = 10
    elif command.lower() == "s" or command.lower() == "south":
      room = 7
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      print("\nYou cannot go this way.")
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      print("\nYou cannot go this way.")
    else:
      print("\nNo.")
  #vent intersection 10
  while room == 10:
    if room == 10:
      print("\nMove = " + str(turn))
      print("\nVENT INTERSECTION")
      if room10 == False:
        print("You approach a 4 way intersection in the vent system, with vents leading in every direction. The strange noise is louder now, and is still coming from the north.")
        room10 = True
      elif room10 == True:
        print("Air ducts head in every direction. The strange noise is louder now, and is still coming from the north.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      room = 11
    elif command.lower() == "s" or command.lower() == "south":
      room = 9
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      room = 13
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      room = 12
    else:
      print("\nNo.")
  #north vent 11
  while room == 11:
    if room == 11:
      print("\nMove = " + str(turn))
      print("\nNORTH VENT")
      if room11 == False:
        print("The noise is overpowering now, and as you reach the edge of the duct, you can see that it coming from a massive underground river. The duct ends on the face of the cliff so you are left with two options: Go back the way you came, or jump into the river below.")
        room11 = True
      else:
        print("The river below seems to be the source of the sound. You can either go back the way you came, or jump into the river below.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north" or command.lower() == "jump":
      room = 19
    elif command.lower() == "s" or command.lower() == "south":
      room = 10
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      print("\nYou cannot go this way.")
    elif command.lower() == "d" or command.lower() == "down":
      room = 19
    elif command.lower() == "e" or command.lower() == "east":
      print("\nYou cannot go this way.")
    else:
      print("\nNo.")
  #east vent 12
  while room == 12:
    if room == 12:
      print("\nMove = " + str(turn))
      print("\nEAST VENT")
      if room12 == False:
        print("You are still in an air duct. It seems to go to the west and then turns north. There seems to be a loose panel to the south.")
        room12 = True
      else:
        print("You can go back to the west or north. There seems to be a loose panel to the south.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      room = 15
    elif command.lower() == "s" or command.lower() == "south":
      if panel == True:
        print("\nThere a loose panel in the way.") 
      elif panel == False:
        room = 14
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      room = 10
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      print("\nYou cannot go this way.")
    elif command.lower() == ("use crowbar on panel"):
      if crowbar == True and panel == True:
        panel = False
        print("\nYou pry open the loose panel to reveal a room to the south.")
      elif crowbar == False and panel == True:
        print("\nYou do not have a crowbar. Go find one.")
      elif crowbar == True and panel == False:
        print("\nYou already did this.")
    elif command.lower() == "i panel" or command.lower() == "inspect panel":
      print("\nThe loose panel is too hard to move with you hands, maybe a tool would help?")
    else:
      print("\nNo.")
  #west vent 13
  while room == 13:
    if room == 13:
      print("\nMove = " + str(turn))
      print("\nWEST VENT")
      if room13 == False:
        print("Another air duct. It continues to the west and back to the east.")
        room13 = True
      else:
        print("The air duct continues to the west and back to the east.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      print("\nYou cannot go this way.")
    elif command.lower() == "s" or command.lower() == "south":
      print("\nYou cannot go this way.") 
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      room = 16
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      room = 10
    else:
      print("\nNo.")
  #rock room 14
  while room == 14:
    if room == 14:
      print("\nMove = " + str(turn))
      print("\nRock Room")
      if room14 == False:
        if monkey == True:
          print("You enter a room filled with rocks. On top of the rocks sits a monkey that glares at you menacingly. The only exit is to the north.")
        elif monkey == False:
          print("You enter a room filled with rocks. On top of the rocks sits a monkey that is monching on a banana. The only exit is to the north.")
        room14 = True
      else:
        if monkey == True:
          print("\nThe monkey on the pile of rocks glares at you menacingly. The only exit is to the north.")
        elif monkey == False:
          print("\nThe monkey is monching on a banana on the pile of rocks. The only exit is to the north.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      room = 12
    elif command.lower() == "s" or command.lower() == "south":
      print("\nYou cannot go this way.") 
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      print("\nYou cannot go this way.")
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      print("\nYou cannot go this way.")
    elif command.lower() == ("take rock"):
      if monkey == True:
        print("\nYou reach out to grab a rock. The second you touch the rock the monkey rips out your throat. Don't steal his stuff he worked hard for those rocks.")
        YOUDIED()
      elif monkey == False:
        print("\nThe monkey allows you to take the rock as a thank you for the banana.")
        rock = True
        banana = False
    elif command.lower() == "use banana on monkey":
      if banana == True:
        monkey = False
        print("\nYou pry open the loose panel.")
      elif banana == False:
        print("\nYou do not have this item.")
    else:
      print("\nNo.")
  #greenhouse 15
  while room == 15:
    if room == 15:
      print("\nMove = " + str(turn))
      print("\nGREENHOUSE")
      if room15 == False:
        print("You emrge into a lush greenhouse filled with all types of plants and trees. There is a ladder propped up against one of the trees. There is a vent to the south as well as a door to the east.")
        room15 = True
      else:
        print("There is a ladder propped up against one of the trees. There is a vent to the south as well as a door to the east.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      print("\nYou cannot go this way.")
    elif command.lower() == "s" or command.lower() == "south":
      room = 12 
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou climb up the ladder and see a few banana bushels.")
      treecommand = input("\nWhat now?\n")
      if treecommand.lower() == "take banana":
        banana = True
        print("\nYou take a banana. I wonder who likes bananas?") 
      elif treecommand == "d" or command.lower() == "down":
        room = 15
    elif command.lower() == "w" or command.lower() == "west":
      print("\nYou cannot go this way.")
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      room = 3
    else:
      print("\nNo.")
  #Machine shop 16
  while room == 16:
    if room == 16:
      print("\nMove = " + str(turn))
      print("\nMACHINE SHOP")
      if room16 == False:
        print("You emege from the vent into a room filled with tools. Power saws and drill presses line the walls, and several handheld tools including a sledgehammer are scattered around. The only exit is the vent to the east. I wonder how all these tools got here since there are no doors.")
        room16 = True
      else:
        print("Several handheld tools including a sledgehammer are scattered around the room. The only exit is the vent to the east.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      print("\nYou cannot go this way.")
    elif command.lower() == "s" or command.lower() == "south":
      print("\nYou cannot go this way.") 
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      print("\nYou cannot go this way.")
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      room = 13
    else:
      print("\nNo.")
  #balcony 17
  while room == 17:
    if room == 17:
      print("\nMove = " + str(turn))
      print("\nBALCONY")
      if room17 == False:
        print("You climb through the window onto a balcony overlooking a maze. The cool air rushes through your hair and you start to feel free again. There is a ladder that seems to go down into the maze, as well as the window you came through.")
        room17 = True
      else:
        print("\nThere is a ladder that seems to go down into the maze, as well as the window you came through.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      print("\nYou cannot go this way.")
    elif command.lower() == "s" or command.lower() == "south":
      print("\nYou cannot go this way.") 
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      room = 1
    elif command.lower() == "d" or command.lower() == "down":
      room = 18
    elif command.lower() == "e" or command.lower() == "east":
      print("\nYou cannot go this way.")  
    else:
      print("\nNo.")
  #maze 18
  while room == 18:
    if room == 18:
      print("\nMove = " + str(turn))
      print("\nMAZE")
      if room18 == False:
        print("You drop into a maze. You cannot reach the ladder you came from, so your only option now is to complete the maze. Good luck!")
        room18 = True
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      x = random.random()
      if x >= 0 and x < 0.05:
        print("\nYou have escaped the maze!")
        room = 25
      elif x >= 0.05 and x < 0.5:
        print("\nDead end.")
        room = 18
      elif x >= 0.5 and x < 1:
        print("\nMore maze.")
        room = 18
    elif command.lower() == "s" or command.lower() == "south":
      x = random.random()
      if x >= 0 and x < 0.1:
        print("\nYou have escaped the maze!")
        room = 25
      elif x >= 0.1 and x < 0.5:
        print("\nDead end.")
        room = 18
      elif x >= 0.5 and x < 1:
        print("\nMore maze.")
        room = 18 
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      x = random.random()
      if x >= 0 and x < 0.1:
        print("\nYou have escaped the maze!")
        room = 25
      elif x >= 0.1 and x < 0.5:
        print("\nDead end.")
        room = 18
      elif x >= 0.5 and x < 1:
        print("\nMore maze.")
        room = 18
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      x = random.random()
      if x >= 0 and x < 0.1:
        print("\nYou have escaped the maze!")
        room = 25
      elif x >= 0.1 and x < 0.5:
        print("\nDead end.")
        room = 18
      elif x >= 0.5 and x < 1:
        print("\nMore maze.")
        room = 18
    else:
      print("\nNo.")
  #river 19
  while room == 19:
    if room == 19:
      print("\nMove = " + str(turn))
      print("\nRIVER")
      if room19 == False:
        print("You jump into the freezing cold river below. You shock of the cold water blinds you for a moment, but when you regain vision you cannot see anything but rapidly moving water. You feel yourself moving west, but unscalable cliff faces surround you. You have one move. Choose wisely.")
        room19 = True
      else:
        print("Cold water. You feel yourself moving west, but unscalable cliff faces surround you. You have one move. Choose wisely.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      print("\nYou swim blindly in the northern direction, and luckily you get to the shore.") 
      room = 20
    elif command.lower() == "s" or command.lower() == "south":
      print("\nYou attempt to swim south but hit a steep rock face. As you realise that you are doomed, you are swept down the waterfall.") 
      YOUDIED()
    elif command.lower() == "u" or command.lower() == "up": 
      print("\nYou try to climb up a rock face, but can't. You fall down the waterfall. Loser.") 
      YOUDIED() 
    elif command.lower() == "w" or command.lower() == "west":
      print("\nYou swim downstream and fall down a waterfall. Nice one!") 
      YOUDIED()
    elif command.lower() == "d" or command.lower() == "down":
      print("\nFor some reason you swim underwater and get stuck on a rock. You drown.")
      YOUDIED()
    elif command.lower() == "e" or command.lower() == "east":
      print("\nYou swim upstream, going nowhere. You get tired and are swept down stream off the waterfall.") 
      YOUDIED()
    else:
      print("\nNo.")
  #shore 20
  while room == 20:
    if room == 20:
      print("\nMove = " + str(turn))
      print("\nSHORE")
      if room20 == False:
        print("You find yourself on the shore of a rushing river located south. To your north is a golden gate embedded in the rocky cliff face with a lock near the handle. As you continue to examine your surroundings, you notice a cave to your east.")
        room20 = True
      else:
        print("There is a gate your your north, a cave to your east, and a river of death south of you.")
      STANDBY()
    if command.lower() == "use key on gate":
      if key == True:
        print("\nYou use the key you found inside the soap to unlock the gate.")
        gate = False
      else:
        print("\nYou do not have a key you clown.")
    if command.lower() == "n" or command.lower() == "north":
      if gate == False:
        print("\nYou walk victoriously through the unlocked gate into the light of freedom.")
        room = 101
      else:
        print("\nThis gate is locked")
    elif command.lower() == "s" or command.lower() == "south":
      room = 19
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      print("\nYou cannot go this way.")  
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      room = 22
    else:
      print("\nNo.")
  #sienas brain 21
  while room == 21:
    if room == 21:
      print("\nMove = " + str(turn))
      print("\nSIENA'S BRAIN")
      if room21 == False:
        print("You enter a room, Buddy Holly by Weezer is playing at 100 decibels. You can't make out where the sound is coming from, and you have no way of stopping it. Oh no... you're getting Weezered. You look to the west, and Bryce Hall approaches you. To your north is a screening of the hit musical movie Dear Evan Hansen. South of you is a group of fake Italians yelling at you for mispronouncing mozzarella.")
        room21 = True
      else:
        print("No")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      print("\nYou see Ben Platt, actor playing Evan Hansen, join in with Weezer to sing Buddy Holly. He starts sobbing and begins reciting slam poetry on The Situation in Kyrgyzstan.")
    elif command.lower() == "s" or command.lower() == "south":
      print("\nThe Italian's chants grow louder, louder, louder. Weezer's Buddy Holly persits, and the Italian's chants morph into the melody of Buddy Holly.")
    elif command.lower() == "u" or command.lower() == "up":
      print("\nThere's a ceiling. You hit your head. Hard. You fade in and out of consciousness, and think to yourself: Will Buddy Holly be the last thing I hear? The last thing I remember?") 
    elif command.lower() == "w" or command.lower() == "west":
      print("\nYou approach Bryce Hall, and he begins to call you various funny nicknames. You yell, scream... for mercy... for help. No one can help you. You are at the merciless hands of Bryce Hall and Weezer.")
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou can't go down. There is no down. This room is made of steel, and you are trapped inside. Just you, and those weird white dudes that wrote Say It Aint So. This is your life now.")
    elif command.lower() == "e" or command.lower() == "east":
      print("\nYou try to pull a sui. No... don't do this... you must stay alive for the Great Awakening. The inevitable nirvana that will rain down on Earth with the death of Weezer awaits you. Until then, Buddy Holly remains your fate.")
    elif command.lower() == "help" or command.lower() == "h":
      print("\nnote from dev: press esc to leave Siena's brain")
    else:
      print("\nbruh")
  #art hall 22
  while room == 22:
    if room == 22:
      print("\nMove = " + str(turn))
      print("\nART HALL")
      if room22 == False:
        print("You enter into a grand marble hall with artistic masterpieces hanging on the walls. Most of the paintings have been beaten and battered by vandals with exceptional taste. There is an exposed brick wall to the south, as well as enterances to the east and west.")
        room22 = True
      else:
        print("Art is here. There is an exposed brick wall to the south, as well as enterances to the east and west.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      print("\nYou cannot go this way.")
    elif command.lower() == "s" or command.lower() == "south":
      print("\nThere is a wall in your way.") 
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      room = 20
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      room = 23
    else:
      print("\nNo.")
  #throne hall 23
  while room == 23:
    if room == 23:
      print("\nMove = " + str(turn))
      print("\nTHRONE HALL")
      if room23 == False:
        print("Grand marble columns line the hall along with several marble statues of various people and mythical creatures. There are passageways to the west and a large door marked EXIT to the east. As you walk through the hall, you feel that gaze again. This time its is stronger. Closer.")
        room23 = True
      else:
        print("The carcass of the Basilisk lies cold on the floor. There are passageways to the west and a large door marked EXIT to the east.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      print("\nYou cannot go this way.")
    elif command.lower() == "s" or command.lower() == "south":
      print("\nYou cannot go this way.")
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      room = 22
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      room = 24
    else:
      print("\nNo.")
  #throne room 24
  while room == 24:
    if room == 24:
      print("\nMove = " + str(turn))
      print("\nTHRONE ROOM")
      if room24 == False:
        print("You open the heavy wooden doors to reveal a monsturus throne room. As you enter the room, the doors slam close behind you and you hear them lock in place. The vaulted celings go higher than the eye can see, and there is a throne in the middle of the room. There is a shadowy figure sitting in the chair. They beckon you to approach.")
        room24 = True
      thronecommand = input("Do you approach?\n>")
      if thronecommand.lower() == "yes" or thronecommand.lower() == "y":
        print("\nYou approach the shadowy figure. As you get closer you start to make out his face. He looks strangely like Will Toledo. When you reach the foot of the throne he speaks. \nDo you want to die?")
        thronecommand = input(">")
        if thronecommand.lower() == "yes" or thronecommand.lower() == "y":
          YOUDIED()
        elif thronecommand.lower() == "no" or thronecommand.lower() == "n":
          print("\nDo you want to live? Do you want to be free?")
          thronecommand = input(">")
          if thronecommand.lower() == "yes" or thronecommand.lower() == "y":
            print("\nYou. You. You are alive.")
            time.sleep(3)
            print("\nand sometimes the player believed the universe had spoken to it through the sunlight that came through the shuffling leaves of the summer trees")
            time.sleep(3)
            print("\nand sometimes the player believed the universe had spoken to it through the zeros and ones, through the electricity of the world, through the scrolling words on a screen at the end of a dream")
            time.sleep(3)
            print("\nand the universe said I love you")
            time.sleep(3)
            print("\nand the universe said you have played the game well")
            time.sleep(3)
            print("\nand the universe said everything you need is within you")
            time.sleep(3)
            print("\nand the universe said you are stronger than you know")
            time.sleep(3)
            print("\nand the universe said you are the daylight")
            time.sleep(3)
            print("\nand the universe said you are the night")
            time.sleep(3)
            print("\nand the universe said the darkness you fight is within you")
            time.sleep(3)
            print("\nand the universe said the light you seek is within you")
            time.sleep(3)
            print("\nand the universe said you are not alone")
            time.sleep(3)
            print("\nand the universe said you are not separate from every other thing")
            time.sleep(3)
            print("\nand the universe said I love you because you are love.")
            time.sleep(3)
            print("\nAnd the game was over and the player woke up from the dream. And the player began a new dream. And the player dreamed again, dreamed better. And the player was the universe. And the player was love.")
            time.sleep(3)
            print("\nYou are the player.")
            time.sleep(3)
            print("\nWake up.")
            time.sleep(3)
            room = 101
          elif thronecommand.lower() == "no" or thronecommand.lower() == "n":
            YOUDIED()
          else:
            print("\nAnswer the question.")
        else:
          print("\nAnswer the question.")
      elif thronecommand.lower() == "no" or thronecommand.lower() == "n":
        print("\nBecasue of your disobedience, the shadow figure snaps his fingers and you cease to exist.")
        YOUDIED()
      else:
        print("\nAnswer the question.")
  #Maze exit 25
  while room == 25:
    if room == 25:
      print("\nMove = " + str(turn))
      print("\nMAZE EXIT")
      if room25 == False:
        print("\nYou somehow mangage to escape the maze and enter a room with stone pillars so high you cannot see the room. All you see are stars above you. As a reward for completing the maze, I have chose to give you an extra life. Spend it well.\nThere is a passage to the north.")
        room25 = True
        elife = True
      else:
        print("\nYou are back in this room which means you did the maze again. Why? I am not going to give you anything extra for doing it again. Be gone.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      room = 23
    elif command.lower() == "s" or command.lower() == "south":
      print("\nThis is back in the maze. Why whould you want to go there?") 
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      print("\nYou cannot go this way.") 
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      print("\nYou cannot go this way.") 
    else:
      print("\nNo.")
  #mineshaft 26
  while room == 26:
    if room == 26:
      print("\nMove = " + str(turn))
      print("\nMINESHAFT")
      if room26 == False:
        print("\nYou pass through a wall of dangling vines into a torch-lit room. Exposed rock surrounds you along with what looks like mining tools scattered everywhere. On the ground is a pickaxe. \nThere are what appear to be cavern enterances to your east and west, along with the passageway you came in from to the north.")
        room26 = True
      else:
        if pickaxe == False:
          print("\nThere are passages to your east, west, and north, and a pickaxe on the ground.")
        else:
          print("\nThere are passages to your east, west, and north.")
      STANDBY()
    if command.lower() == "take pickaxe":
      if pickaxe == False:
        print("\nYou hoist the heavy pick off the ground, and store it in your pocket for later use.")
        pickaxe = True
      else:
        print("\nYou already have this item.")
    elif command.lower() == "n" or command.lower() == "north":
      room = 6
    elif command.lower() == "s" or command.lower() == "south":
      print("\nYou cannot go this way.") 
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      room = 28
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      room = 27
    else:
      print("\nNo.")
  #Crazy Miners Abode 27
  while room == 27:
    if room == 27:
      print("\nMove = " + str(turn))
      print("\nCRAZY MINERS ABODE")
      if room27 == False:
        print("\nYou walk into a small but cozy cavern. From the looks of things, somebody is living here. Before you process that thought, a small man drops from the celing shrieking on his way down. He lands on your back forcing you to the ground. He holds a sharp pointy rock to your throat and demands an entry fee.")
        room27 = True
        caveCommand = input("What will you give him? > ")
        if caveCommand.lower() == "gem":
          if gem == True:
            gem = False
            caveman = False
            print("\nThe caveman takes your gem and studies it curiouly. He seems to be satisifed as he scurries off with his newfound rock making strange gunting noises.")
          else: 
            print("\nThe caveman is disappointed that you dont have what you say you have. He calls you a dirty little liar and cuts you into a million pieces, throws them in a big pot, and makes a nice stew for dinner.")
          YOUDIED()
        else:
          print("\nThe caveman is unhappy with your contribution and throws it across the room. He then focuses his rage on you and cuts you into a million pieces, throws them in a big pot, and makes a nice stew for dinner.")
          YOUDIED()
      else:
        print("\nThe caveman is happily dancing around his shiny new toy in the corner. There is nothing but a crowbar on the floor.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      print("\nYou cannot go this way.")
    elif command.lower() == "s" or command.lower() == "south":
      print("\nYou cannot go this way.") 
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      room = 26
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      print("\nYou cannot go this way.")
    elif command.lower() == "take crowbar":
      if caveman == False:
        print("\nYou pickup the crowbar quietly from the ground. You should probalbly leave before you the caveman gets mad.")
        crowbar = True
      else: 
        print("\nHacker. I haven't told you that this item is here yet. Die.")
        YOUDIED()
    else:
      print("\nNo.")
  #frozen cave 28
  while room == 28:
    if room == 28:
      print("\nMove = " + str(turn))
      print("\nFROZEN CAVE")
      if room28 == False:
        print("\nYou enter through a veil of frost to reveal an icy room with dangerous looking icicles hanging precariuly from the celing. There is a stack of what appears to be geodes on the far side of the room, and a heater to your left. The only exit is the way you came in.")
        room28 = True
      else:
        if icicles == True: 
          if geode == False:
            print("\nYou enter a room with icicles hanging precariuly from the celing. There is a stack of what appears to be geodes on the far side of the room, and a heater to your left. The only exit is the way you came in.")
          else:
            print("\nYou enter a room with icicles hanging precariuly from the celing. There is a heater to your left. The only exit is the way you came in.")
        else:
          if geode == False:
            print("\nYou enter a room with a pool of water on the floor. There is a stack of what appears to be geodes on the far side of the room, and an active heater to your left. The only exit is the way you came in.")
          else:
            print("\nYou enter a room with a pool of water on the floor. There is an active heater to your left. The only exit is the way you came in.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      if icicles == True:
        print("\nYou walk under the icicles and instantly realize your mistake. The vibrations caused by your movement make the sharp daggers of ice fall from the celing, instatly killing you.")
        YOUDIED()
      else:
        print("\nYou cannot go this way.")
    elif command.lower() == "s" or command.lower() == "south":
      if icicles == True:
        print("\nYou walk under the icicles and instantly realize your mistake. The vibrations caused by your movement make the sharp daggers of ice fall from the celing, instatly killing you.")
        YOUDIED()
      else:
        print("\nYou cannot go this way.") 
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      if icicles == True:
        print("\nYou walk under the icicles and instantly realize your mistake. The vibrations caused by your movement make the sharp daggers of ice fall from the celing, instatly killing you.")
        YOUDIED()
      else:
        print("\nYou cannot go this way.")
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      room = 26
    elif command.lower() == "use heater":
      print("\nYou switch on the heater and instantly feel its effect. The ice that once coated the walls and the icicles on the celing instanly melt leaving nothing to fear.")
      icicles = False
    elif command.lower() == "take geode":
      if icicles == False:
        print("\nYou grab a rock from the pile and study it closely. Perhaps there is something inside?")
        geode = True
      else:
        print("\nYou walk under the icicles and instantly realize your mistake. The vibrations caused by your movement make the sharp daggers of ice fall from the celing, instatly killing you.")
        YOUDIED()
    else:
      print("\nNo.")
  #Dungeon Hallway 29
  while room == 29:
    if room == 29:
      print("\nMove = " + str(turn))
      print("\nDUNGEON HALLWAY")
      if room29 == False:
        print("\nWelcome to your average run of the mill dungeon hallway filled with all kinds of mossy stone bricks and a variety of strange smells including but not limited to wet, mold, and a faint odor that reminds you of manure. \nThe hallway runs east to west.")
        room29 = True
      else:
        print("\nThis particular hallway runs east to west.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      print("\nYou cannot go this way.")
    elif command.lower() == "s" or command.lower() == "south":
      print("\nYou cannot go this way.") 
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      room = 30
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      room = 6
    else:
      print("\nNo.")
  #farm 30
  while room == 30:
    if room == 30:
      print("\nMove = " + str(turn))
      print("\nFARM")
      if room30 == False:
        print("\nYou enter into a large open field with wheat and barley growing all around. There are some cows grazing in teh fields, as well as chickens and other barnyard animals. There are roads leading north, west and east; however, the western and northern roads have signs reading: \n--WARNING: DANGER--")
        room30 = True
      else:
        print("\nYou are at a farm. There are roads leading north, west and east; however, the western and northern roads have signs reading: \n--WARNING: DANGER--")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      room = 31
    elif command.lower() == "s" or command.lower() == "south":
      print("\nYou cannot go this way.") 
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.")  
    elif command.lower() == "w" or command.lower() == "west":
      room = 32
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      room = 29
    else:
      print("\nNo.")
  #grain storage 31
  while room == 31:
    if room == 31:
      print("\nMove = " + str(turn))
      print("\nGRAIN STORAGE")
      if room31 == False:
        print("\nfun dialouge")
        room31 = True
      else:
        print("\nfun dialouge")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      print("\nYou cannot go this way.") 
    elif command.lower() == "s" or command.lower() == "south":
      room = 30
    elif command.lower() == "u" or command.lower() == "up":
      room = 7
    elif command.lower() == "w" or command.lower() == "west":
      print("\nYou cannot go this way.") 
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      print("\nYou cannot go this way.") 
    else:
      print("\nNo.")
  #pig corral 32
  while room == 32:
    if room == 32:
      print("\nMove = " + str(turn))
      print("\nPIG CORRAL")
      if room32 == False:
        print("\nfun dialouge")
        room32 = True
      else:
        print("\nfun dialouge")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      room = 33
    elif command.lower() == "s" or command.lower() == "south":
      print("\nYou cannot go this way.") 
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.") 
    elif command.lower() == "w" or command.lower() == "west":
      print("\nYou cannot go this way.") 
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      room = 30
    else:
      print("\nNo.")
  #tunnel 33
  while room == 33:
    if room == 33:
      print("\nMove = " + str(turn))
      print("\nTUNNEL")
      if room33 == False:
        print("\nThe rank smell of pig is definatly noticalbe as you find yourself in a a musty tunnel. The passage is inclined, with opening to both the north and south.")
        room33 = True
      else:
        print("\nYou find yourself in a a musty tunnel. The passage is inclined, with opening to both the north and south.")
      STANDBY()
    if command.lower() == "n" or command.lower() == "north":
      room = 8
    elif command.lower() == "s" or command.lower() == "south":
      room = 32
    elif command.lower() == "u" or command.lower() == "up":
      print("\nYou cannot go this way.") 
    elif command.lower() == "w" or command.lower() == "west":
      print("\nYou cannot go this way.") 
    elif command.lower() == "d" or command.lower() == "down":
      print("\nYou cannot go this way.")
    elif command.lower() == "e" or command.lower() == "east":
      print("\nYou cannot go this way.") 
    else:
      print("\nNo.")
  #End 101
  while room == 101:
    if room == 101:
      print("\nThe End :D")
      print("\nCongratulation you escaped! Your total number of moves was: ")
      print(turn)
      print("\nWould you like to play again and try and escape with less moves?")
      playAgain = input("y or n > ")
      if playAgain == "y":
        RESET()
      elif playAgain == "n":
        print("\nWhat a party pooper.")
        QUIT()
  
