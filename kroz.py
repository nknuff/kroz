import time
import random


def standby():
    global command, turn
    if room != 101:
        command = input("\nWhat will you do?\n>")
        turn = turn + 1
        if command.lower() == "use razor on soap":
            if (razor == True) and (soap == True):
                if not key:
                    soapkey()
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
                print("gem")


def quit():
    exit()


def reset():
    # variable declaration
    global room, rug, screwdriver, razor, soap, key, rock, string, cutlass, longsword, katana, panel, crowbar, \
        banana, monkey, screen, room0, room1, window, room2, room4, room3, hallwayCounter, room6, room7, vent, room5,\
        room8, room9, room10, room11, room12, room13, room14, room15, room16, room17, room18, room19, room20, room21,\
        room22, room23, room24, room25, room26, room27, room28, room29, room30, room31, room32, room33, portalUse, \
        turn, gate, elife, pickaxe, geode, gem, caveman, pig, basilisk, rancor, icicles, grate, wall, sledgehammer
    # item setup
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
    grate = False
    wall = True
    sledgehammer = False
    # room setup
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
    # int setup
    hallwayCounter = 0
    portalUse = 5
    turn = 0
    # mob setup
    monkey = True
    caveman = True
    pig = True
    basilisk = True
    rancor = True


def youdied():
    global elife
    if not elife:
        print("\nCongrats you died. Maybe try being better?\nWould you like to try again?")
        restart = input("y or n > ")
        if restart == "y":
            reset()
        elif restart == "n":
            print("What a party pooper.")
    elif elife:
        print(
            "\nSadly, you died. But luckily, you have an extra life! Lucky duck! "
            "\nYou spawn back where you died, ready to face the world again!")
        time.sleep(3)
        elife = False


def soapkey():
    global key
    key = True
    print("\nNow you are a smart cookie. Inside the soap is a small key.")


def portal():
    global room, portalUse
    print("\nvwoooop! You go through the portal and are transported to a random room!")
    room = int(random.random() * 33)
    portalUse = portalUse - 1
    print("\nYou have " + str(portalUse) + " portal uses left.")

def help():
    print(
        "north = moves north\neast = moves east\nsouth = moves south\nwest = moves west\nup = ascend\ndown = descend"
        "\ntake [item] = takes specified item\nuse [item] = uses specified item"
        "\nuse [item] on [item] = uses specified item on specified item\nmove [item] = moves specified item"
        "\ninspect [item] = inspects specified item\ni = see inventory\nh = help\nI hope you enjoy your stay!"
        "\n--------------------------------------------")
reset()
print("Welcome to Kroz! The controls are as follows: ")
help()
while 1 == 1:
    while room == 0:
        if room == 0:
            print("\nMove = " + str(turn))
            print("\nHOTEL ROOM 47")
            if rug:
                if not room0:
                    print(
                        "You awake in what seems to be a hotel room. There is a door to the west as well as "
                        "\na door to the north.There is a heavy shag rug under your feet and a window to the east.")
                    room0 = True
                elif room0:
                    print(
                        "There is a door to the west as well as a door to the north."
                        "\nThere is a heavy shag rug under your feet and a window to the east.")
            elif not rug:
                if not room0:
                    print(
                        "You awake in what seems to be a hotel room. There is a door to the west as well as a door "
                        "\n to the north.There is a heavy shag rug that has been moved to reveal a trapdoor and "
                        "\n a window to the east.")
                    room0 = True
                elif room0:
                    print(
                        "There is a door to the west as well as a door to the north and a window to the east."
                        "\nThere is a heavy shag rug that has been moved to reveal a trapdoor.")
            standby()
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
        elif command.lower() == "move rug":
            rug = False
            print("\nWith great effort you move the rug to reveal a trap door. Where could this lead?")
        elif command.lower() == "d" or command.lower() == "down":
            if rug:
                print("\nYou can't go through the floor... or can you?")
            elif not rug:
                room = 6
        else:
            print("\nNo.")
    # sun room 1
    while room == 1:
        if room == 1:
            print("\nMove = " + str(turn))
            print("\nSUN ROOM")
            if not room1:
                if not screwdriver:
                    print(
                        "You walk through a pair of french doors to reveal a cozy sun room filled with houseplants."
                        "\nThere is a window on the east side of the room, and the doors you came into to the west."
                        "\nIn the corner is a screwdriver.")
                    room1 = True
                elif screwdriver:
                    print(
                        "You walk through a pair of french doors to reveal a cozy sun room filled with houseplants."
                        "\nThere is a window on the east side of the room, and the doors you came into to the west.")
                    room1 = True
            elif room1:
                if not screwdriver:
                    print(
                        "There is a window on the east side of the room, and the doors you came into to the west."
                        "\nIn the corner is a screwdriver.")
                elif screwdriver:
                    print("There is a window on the east side of the room, and the doors you came into to the west.")
            standby()
        if command.lower() == "east" or command.lower() == 'e':
            if window:
                print("\nThere is a window here.")
            elif not window:
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
            if window:
                print("\nThe window seems unopenable by any means other than a solid object such as a rock...")
            if not window:
                print(
                    "\nBe careful climbing through you could cut yourself on the sharp glass. "
                    "\nMaybe you should use a cloth or something to protect yourself.")
        elif command.lower() == "use rock on window":
            if rock and window:
                print("\nYou throw the rock at the window shattering it.")
                rock = False
                window = False
            elif not rock and window:
                print("\nGo find Dwayne and try again.")
            elif not rock and not window:
                print("\nThe window is open and you do not have a rock or apparently a brain.")
            elif rock and not window:
                print(
                    "\nThe window is already open. Also how did did get this line of dialog it is "
                    "\nlogically impossible to get i am proud of u <3.")
        else:
            print("\nNo.")
    # bathroom 2
    while room == 2:
        if room == 2:
            print("\nMove = " + str(turn))
            print("\nBATHROOM")
            if not room2:
                print(
                    "You find yourself in a bathroom. You look in the mirror and think 'Wow I'm gorgeous.' "
                    "\nOn the counter is a bar of soap as well as a razor. To your north is another door.")
                room2 = True
            elif room2:
                if not soap and not razor:
                    print("On the counter is a bar of soap as well as a razor. To your north is another door.")
                elif soap and not razor:
                    print("On the counter is a razor. To your north is another door.")
                elif not soap and razor:
                    print("On the counter is a bar of soap. To your north is another door.")
                elif soap and not razor:
                    print("There is nothing on the counter. To your north is another door.")
            standby()
        if command.lower() == "n" or command.lower() == "north":
            room = 4
        elif command.lower() == "s" or command.lower() == "south":
            room = 0
        elif command.lower() == "take soap":
            soap = True
            print("\nYou take the bar of soap. Cleanliness is always important.")
        elif command.lower() == "take razor":
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
            soapkey()
        else:
            print("\nNo.")
    # hallway 3
    while room == 3:
        if room == 3:
            print("\nMove = " + str(turn))
            print("\nHALLWAY")
            if hallwayCounter >= 21:
                print(
                    "\nYour vision goes dark as your reality ceases to exist. You have broken the space-time continuum."
                    "\nI suppose this qualifies at escaping?")
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
            if not room3 and room != 101:
                print(
                    "You enter a hallway that seems to extend forever in both directions. "
                    "\nHowever there is another door on the other side of the hallway.")
                room3 = True
            elif room3 and room != 101:
                print(
                    "The hallway seemingly extends forever in both directions. "
                    "\nThere are doors to the east and west however.")
            standby()
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
    # dark/sword room 4
    while room == 4:
        if room == 4:
            print("\nMove = " + str(turn))
            print("\nHOTEL ROOM 48")
            if not room4:
                if string:
                    print("You enter a room of complete darkness, and cannot tell your right from your left.")
                elif not string:
                    print(
                        "A single light bulb hanging by a wire illuminates the room. "
                        "\nYou enter a room that looks more or less like yours. The only difference is the presence "
                        "\nof a display case of sorts filled with swords from all around the globe. "
                        "\nYou can see doors in every direction except east.")
                    room4 = True
            elif room4:
                print(
                    "There is a case displaying swords in the corner. There are doors in every direction except east.")
            standby()
        if command.lower() == "n" or command.lower() == "north":
            if string:
                print("\nYou cannot go this way.")
            elif not string:
                room = 5
        elif command.lower() == "s" or command.lower() == "south":
            if string:
                room = 3
            elif not string:
                room = 2
        elif command.lower() == "u" or command.lower() == "up":
            print("\nYou cannot go this way.")
        elif command.lower() == "w" or command.lower() == "west":
            if string:
                room = 5
            elif not string:
                room = 3
        elif command.lower() == "d" or command.lower() == "down":
            print("\nYou cannot go this way.")
        elif command.lower() == "e" or command.lower() == "east":
            if string:
                room = 2
            elif not string:
                print("\nI literally said there is no door here.")
        elif command.lower() == "inspect swords" or command.lower() == "i swords" or \
                command.lower() == "inspect case" or command.lower() == "i case":
            if longsword or katana or cutlass:
                print("\nYou already have a sword you greedy pig.")
            else:
                print(
                    "\nYou approach the sword case to take a closer look. You see 3 different types of swords: "
                    "\na longsword, a katana, and a cutlass. There is a sign on the case that reads the following: "
                    "\n'Choose one, but choose wisely'")
                sword = input("\nWhat blade will you choose?\n>")
                if sword.lower() == "longsword":
                    longsword = True
                    print("\nAh the longsword. Heavy in damage but slow in attack. Wise choice.")
                elif sword.lower() == "katana":
                    katana = True
                    print(
                        "\nThe samurai's weapon. Perfectly balanced in both damage and speed, as all things should be.")
                elif sword.lower() == "cutlass":
                    cutlass = True
                    print("\nThe sword of the seas. This one favors speed and agility over damage.")
                else:
                    print("\nPick a sword or you might regret it.")
        else:
            print("\nNo.")
    # closet 5
    while room == 5:
        if room == 5:
            print("\nMove = " + str(turn))
            print("\nCLOSET")
            if string:
                print(
                    "You stumble through a door and into a small, tight closet. "
                    "\nYou can feel a string in front of you and an exposed brick wall to your north.")
            if not string:
                print(
                    "You are in a small, tight closet. "
                    "\nYou can feel a string in front of you and an exposed brick wall to your north.")
            standby()
        if command.lower() == "n" or command.lower() == "north":
            if wall:
                print("\nYou cannot go this way.")
            else:
                print("\nYou squeeze through the gap in the wall and drop into the hall below.")
                room = 22
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
        elif command.lower() == "use string":
            string = False
            print("\nYou pull on the string. You hear a click from the other room.")
        else:
            print("\nNo.")
    # dungeon entrance 6
    while room == 6:
        if room == 6:
            print("\nMove = " + str(turn))
            print("\nDUNGEON ENTRANCE")
            if room6:
                print(
                    "Torches light several passages to the west, east, and south. "
                    "\nThere is also the ladder you came down on.")
                if not monkey:
                    print("\nOne of the heads, which is shaped like a monkey, seems to emit a strange glow.")
            if not room6:
                print(
                    "You descend down a rickety old ladder into a damp, chilly chamber. "
                    "\nThe heads of several horrifying creatures are encased in stone and mounted on the walls. "
                    "\nMoss and ferns inhabit this narrow chamber, and torches light several passages "
                    "\nto the east, west, and south.")
                if not monkey:
                    print("\nOne of the heads, which is shaped like a monkey, seems to emit a strange glow.")
                room6 = True
            standby()
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
        elif command.lower() == "inspect heads" or command.lower() == "i heads" \
                or command.lower() == "i creatures" or command.lower() == "inspect creatures":
            print(
                "\nThere are five total stone heads, each of a different creature. "
                "\nThere is a monkey, a pig, a basilisk, a caveman, and a rancor. "
                "\nUpon further inspection, the heads seem to have some kind of mechanism behind them. "
                "\nI wonder how to activate it...")
        else:
            print("\nNo.")
    # movie theater 7
    while room == 7:
        if room == 7:
            print("\nMove = " + str(turn))
            print("\nMOVIE THEATER")
            if not room7:
                print(
                    "You enter a movie theater playing an old black and white film on a screen to the west. "
                    "\nAs you walk around the empty theater, you get the feeling that someone is watching you. "
                    "\nThe only door you see is the door you came in from. "
                    "\nHowever, there is an air vent to the north and what appears to be a sewer grate in the floor.")
                room7 = True
            elif room7:
                print(
                    "You still can't shake the feeling that someone is watching you. "
                    "\nThere is an air vent to the north, a sealed grate in the floor, a door to the east, "
                    "\nand a screen to the west.")
            standby()
        if command.lower() == "n" or command.lower() == "north":
            if vent:
                print("\nThere is a vent here.")
            elif not vent:
                room = 9
        elif command.lower() == "s" or command.lower() == "south":
            print("\nYou cannot go this way.")
        elif command.lower() == "u" or command.lower() == "up":
            print("\nYou cannot go this way.")
        elif command.lower() == "w" or command.lower() == "west":
            if screen:
                print("\nThere is a screen here. I believe it is playing Modern Times.")
            elif not screen:
                room = 8
        elif command.lower() == "d" or command.lower() == "down":
            if grate:
                print("\nYou climb down the grate and descend into the room below.")
            print("\nYou cannot go this way.")
        elif command.lower() == "e" or command.lower() == "east":
            room = 3
        elif command.lower() == "inspect vent" or command.lower() == "i vent":
            print("\nThe vent is firmly screwed in place. Maybe a tool would help open this.")
        elif command.lower() == "inspect grate" or command.lower() == "i grate":
            print("\nThe grate is sealed shut and there is no apparent way to open it. Maybe from the other side...")
        elif command.lower() == "use screwdriver on vent":
            if screwdriver:
                print(
                    "\nLucky you, you have a screwdriver and swiftly open the vent. "
                    "\nI told you that tools come in handy.")
                vent = False
            else:
                print("\nDon't try to use things you don't have. Cheater.")
        elif command.lower() == "inspect screen" or command.lower() == "i screen":
            print("\nYou walk up to the screen. There seems to be a room on the other side.")
        elif command.lower() == "use razor on screen":
            if razor and screen:
                screen = False
                print("\nYou slice open the fabric film screen to reveal another room to the west.")
            elif razor and not screen:
                print("\nYou seem to have already done this.")
            else:
                print("\nYou don't have a razor silly.")
        else:
            print("\nNo.")
    # Portal Room 8
    while room == 8:
        if room == 8:
            print("\nMove = " + str(turn))
            print("\nPORTAL ROOM")
            if not room8:
                print(
                    "You squeeze through the whole you made with your razor into a clean, white room. "
                    "\nThe only item in the room is what looks like a portal on the opposite end.")
            if room8:
                print("A portal lies to your west. It seems happy to see you.")
            standby()
        if command.lower() == "n" or command.lower() == "north":
            print("\nYou cannot go this way.")
        elif command.lower() == "s" or command.lower() == "south":
            print("\nYou cannot go this way.")
        elif command.lower() == "u" or command.lower() == "up":
            print("\nYou cannot go this way.")
        elif command.lower() == "w" or command.lower() == "west":
            portal()
        elif command.lower() == "d" or command.lower() == "down":
            print("\nYou cannot go this way.")
        elif command.lower() == "e" or command.lower() == "east":
            room = 7
        else:
            print("\nNo.")
    # south vent 9
    while room == 9:
        if room == 9:
            print("\nMove = " + str(turn))
            print("\nSOUTH VENT")
            if not room9:
                print(
                    "You enter a small, tight air duct, with barely enough room to crawl through. "
                    "\nThe duct continues to the north, and you can hear a strange noise coming from that direction.")
                room9 = True
            elif room9:
                print("The duct continues to the north, and you can hear a strange noise coming from that direction.")
            standby()
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
    # vent intersection 10
    while room == 10:
        if room == 10:
            print("\nMove = " + str(turn))
            print("\nVENT INTERSECTION")
            if not room10:
                print(
                    "You approach a 4 way intersection in the vent system, with vents leading in every direction. "
                    "\nThe strange noise is louder now, and is still coming from the north.")
                room10 = True
            elif room10:
                print(
                    "Air ducts head in every direction. "
                    "\nThe strange noise is louder now, and is still coming from the north.")
            standby()
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
    # north vent 11
    while room == 11:
        if room == 11:
            print("\nMove = " + str(turn))
            print("\nNORTH VENT")
            if not room11:
                print(
                    "The noise is overpowering now, and as you reach the edge of the duct, "
                    "\nyou can see that it coming from a massive underground river. The duct ends on the face of the "
                    "\ncliff so you are left with two options: Go back the way you came, or jump into the river below.")
                room11 = True
            else:
                print(
                    "The river below seems to be the source of the sound. "
                    "\nYou can either go back the way you came, or jump into the river below.")
            standby()
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
    # east vent 12
    while room == 12:
        if room == 12:
            print("\nMove = " + str(turn))
            print("\nEAST VENT")
            if not room12:
                print(
                    "You are still in an air duct. It seems to go to the west and then turns north. "
                    "\nThere seems to be a loose panel to the south.")
                room12 = True
            else:
                print("You can go back to the west or north. There seems to be a loose panel to the south.")
            standby()
        if command.lower() == "n" or command.lower() == "north":
            room = 15
        elif command.lower() == "s" or command.lower() == "south":
            if panel:
                print("\nThere a loose panel in the way.")
            elif not panel:
                room = 14
        elif command.lower() == "u" or command.lower() == "up":
            print("\nYou cannot go this way.")
        elif command.lower() == "w" or command.lower() == "west":
            room = 10
        elif command.lower() == "d" or command.lower() == "down":
            print("\nYou cannot go this way.")
        elif command.lower() == "e" or command.lower() == "east":
            print("\nYou cannot go this way.")
        elif command.lower() == "use crowbar on panel":
            if crowbar and panel:
                panel = False
                print("\nYou pry open the loose panel to reveal a room to the south.")
            elif not crowbar and panel:
                print("\nYou do not have a crowbar. Go find one.")
            elif crowbar and not panel:
                print("\nYou already did this.")
        elif command.lower() == "i panel" or command.lower() == "inspect panel":
            print("\nThe loose panel is too hard to move with you hands, maybe a tool would help?")
        else:
            print("\nNo.")
    # west vent 13
    while room == 13:
        if room == 13:
            print("\nMove = " + str(turn))
            print("\nWEST VENT")
            if not room13:
                print("Another air duct. It continues to the west and back to the east.")
                room13 = True
            else:
                print("The air duct continues to the west and back to the east.")
            standby()
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
    # rock room 14
    while room == 14:
        if room == 14:
            print("\nMove = " + str(turn))
            print("\nRock Room")
            if not room14:
                if monkey:
                    print(
                        "You enter a room filled with rocks. On top of the rocks sits a monkey that glares at you "
                        "\nmenacingly. The only exit is to the north.")
                elif not monkey:
                    print(
                        "You enter a room filled with rocks. On top of the rocks sits a monkey "
                        "\nthat is munching on a banana. The only exit is to the north.")
                room14 = True
            else:
                if monkey:
                    print("\nThe monkey on the pile of rocks glares at you menacingly. The only exit is to the north.")
                elif not monkey:
                    print("\nThe monkey is munching on a banana on the pile of rocks. The only exit is to the north.")
            standby()
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
        elif command.lower() == "take rock":
            if monkey:
                print(
                    "\nYou reach out to grab a rock. The second you touch the rock the monkey rips out your throat. "
                    "\nDon't steal his stuff he worked hard for those rocks.")
                youdied()
            elif not monkey:
                print("\nThe monkey allows you to take the rock as a thank you for the banana.")
                rock = True
                banana = False
        elif command.lower() == "use banana on monkey":
            if banana:
                monkey = False
                print("\nYou pry open the loose panel.")
            elif not banana:
                print("\nYou do not have this item.")
        else:
            print("\nNo.")
    # greenhouse 15
    while room == 15:
        if room == 15:
            print("\nMove = " + str(turn))
            print("\nGREENHOUSE")
            if not room15:
                print(
                    "You emerge into a lush greenhouse filled with all types of plants and trees. "
                    "\nThere is a ladder propped up against one of the trees. There is a vent to the south as well as "
                    "\na door to the east.")
                room15 = True
            else:
                print(
                    "There is a ladder propped up against one of the trees. "
                    "\nThere is a vent to the south as well as a door to the east.")
            standby()
        if command.lower() == "n" or command.lower() == "north":
            print("\nYou cannot go this way.")
        elif command.lower() == "s" or command.lower() == "south":
            room = 12
        elif command.lower() == "u" or command.lower() == "up":
            print("\nYou climb up the ladder and see a few banana bushels.")
            treeCommand = input("\nWhat now?\n")
            if treeCommand.lower() == "take banana":
                banana = True
                print("\nYou take a banana. I wonder who likes bananas?")
            elif treeCommand == "d" or command.lower() == "down":
                room = 15
        elif command.lower() == "w" or command.lower() == "west":
            print("\nYou cannot go this way.")
        elif command.lower() == "d" or command.lower() == "down":
            print("\nYou cannot go this way.")
        elif command.lower() == "e" or command.lower() == "east":
            room = 3
        else:
            print("\nNo.")
    # Machine shop 16
    while room == 16:
        if room == 16:
            print("\nMove = " + str(turn))
            print("\nMACHINE SHOP")
            if not room16:
                print(
                    "You emerge from the vent into a room filled with tools. "
                    "\nPower saws and drill presses line the walls, and several handheld tools including a "
                    "\nsledgehammer are scattered around. The only exit is the vent to the east. I wonder how all "
                    "\nthese tools got here since there are no doors.")
                room16 = True
            else:
                print(
                    "Several handheld tools including a sledgehammer are scattered around the room. "
                    "\nThe only exit is the vent to the east.")
            standby()
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
        elif command.lower() == "take sledgehammer" or command.lower() == "t sledgehammer":
            print("\nYou hoist the heavy hammer off the ground and place it in your pocket.")
            sledgehammer = True
        else:
            print("\nNo.")
    # balcony 17
    while room == 17:
        if room == 17:
            print("\nMove = " + str(turn))
            print("\nBALCONY")
            if not room17:
                print(
                    "You climb through the window onto a balcony overlooking a maze. "
                    "\nThe cool air rushes through your hair and you start to feel free again. There is a ladder that "
                    "\nseems to go down into the maze, as well as the window you came through.")
                room17 = True
            else:
                print(
                    "\nThere is a ladder that seems to go down into the maze, as well as the window you came through.")
            standby()
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
    # maze 18
    while room == 18:
        if room == 18:
            print("\nMove = " + str(turn))
            print("\nMAZE")
            if not room18:
                print(
                    "You drop into a maze. You cannot reach the ladder you came from, so your only option now "
                    "\nis to complete the maze. Good luck!")
                room18 = True
            standby()
        if command.lower() == "n" or command.lower() == "north":
            x = random.random()
            if 0 <= x < 0.05:
                print("\nYou have escaped the maze!")
                room = 25
            elif 0.05 <= x < 0.5:
                print("\nDead end.")
                room = 18
            elif 0.5 <= x < 1:
                print("\nMore maze.")
                room = 18
        elif command.lower() == "s" or command.lower() == "south":
            x = random.random()
            if 0 <= x < 0.1:
                print("\nYou have escaped the maze!")
                room = 25
            elif 0.1 <= x < 0.5:
                print("\nDead end.")
                room = 18
            elif 0.5 <= x < 1:
                print("\nMore maze.")
                room = 18
        elif command.lower() == "u" or command.lower() == "up":
            print("\nYou cannot go this way.")
        elif command.lower() == "w" or command.lower() == "west":
            x = random.random()
            if 0 <= x < 0.1:
                print("\nYou have escaped the maze!")
                room = 25
            elif 0.1 <= x < 0.5:
                print("\nDead end.")
                room = 18
            elif 0.5 <= x < 1:
                print("\nMore maze.")
                room = 18
        elif command.lower() == "d" or command.lower() == "down":
            print("\nYou cannot go this way.")
        elif command.lower() == "e" or command.lower() == "east":
            x = random.random()
            if 0 <= x < 0.1:
                print("\nYou have escaped the maze!")
                room = 25
            elif 0.1 <= x < 0.5:
                print("\nDead end.")
                room = 18
            elif 0.5 <= x < 1:
                print("\nMore maze.")
                room = 18
        else:
            print("\nNo.")
    # river 19
    while room == 19:
        if room == 19:
            print("\nMove = " + str(turn))
            print("\nRIVER")
            if not room19:
                print(
                    "You jump into the freezing cold river below. You shock of the cold water blinds you for a moment, "
                    "\nbut when you regain vision you cannot see anything but rapidly moving water. You feel yourself "
                    "\nmoving west, but unscalable cliff faces surround you. You have one move. Choose wisely.")
                room19 = True
            else:
                print(
                    "Cold water. You feel yourself moving west, but unscalable cliff faces surround you. "
                    "\nYou have one move. Choose wisely.")
            standby()
        if command.lower() == "n" or command.lower() == "north":
            print("\nYou swim blindly in the northern direction, and luckily you get to the shore.")
            room = 20
        elif command.lower() == "s" or command.lower() == "south":
            print(
                "\nYou attempt to swim south but hit a steep rock face. "
                "\nAs you realise that you are doomed, you are swept down the waterfall.")
            youdied()
        elif command.lower() == "u" or command.lower() == "up":
            print("\nYou try to climb up a rock face, but can't. You fall down the waterfall. Loser.")
            youdied()
        elif command.lower() == "w" or command.lower() == "west":
            print("\nYou swim downstream and fall down a waterfall. Nice one!")
            youdied()
        elif command.lower() == "d" or command.lower() == "down":
            print("\nFor some reason you swim underwater and get stuck on a rock. You drown.")
            youdied()
        elif command.lower() == "e" or command.lower() == "east":
            print("\nYou swim upstream, going nowhere. You get tired and are swept down stream off the waterfall.")
            youdied()
        else:
            print("\nNo.")
    # shore 20
    while room == 20:
        if room == 20:
            print("\nMove = " + str(turn))
            print("\nSHORE")
            if not room20:
                print(
                    "You find yourself on the shore of a rushing river located south. "
                    "\nTo your north is a golden gate embedded in the rocky cliff face with a lock near the handle. "
                    "\nAs you continue to examine your surroundings, you notice a cave to your east.")
                room20 = True
            else:
                print("There is a gate your your north, a cave to your east, and a river of death south of you.")
            standby()
        if command.lower() == "use key on gate":
            if key:
                print("\nYou use the key you found inside the soap to unlock the gate.")
                gate = False
            else:
                print("\nYou do not have a key you clown.")
        if command.lower() == "n" or command.lower() == "north":
            if not gate:
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
    # sienas brain 21
    while room == 21:
        if room == 21:
            print("\nMove = " + str(turn))
            print("\nSIENA'S BRAIN")
            if not room21:
                print(
                    "You enter a room, Buddy Holly by Weezer is playing at 100 decibels. "
                    "You can't make out where the sound is coming from, and you have no way of stopping it. "
                    "Oh no... you're getting Weezered. You look to the west, and Bryce Hall approaches you. "
                    "To your north is a screening of the hit musical movie Dear Evan Hansen. "
                    "South of you is a group of fake Italians yelling at you for mispronouncing mozzarella.")
                room21 = True
            else:
                print("No")
            standby()
        if command.lower() == "n" or command.lower() == "north":
            print(
                "\nYou see Ben Platt, actor playing Evan Hansen, join in with Weezer to sing Buddy Holly. "
                "\nHe starts sobbing and begins reciting slam poetry on The Situation in Kyrgyzstan.")
        elif command.lower() == "s" or command.lower() == "south":
            print(
                "\nThe Italian's chants grow louder, louder, louder. "
                "\nWeezer's Buddy Holly persists, and the Italian's chants morph into the melody of Buddy Holly.")
        elif command.lower() == "u" or command.lower() == "up":
            print(
                "\nThere's a ceiling. You hit your head. Hard. You fade in and out of consciousness, "
                "\nand think to yourself: Will Buddy Holly be the last thing I hear? The last thing I remember?")
        elif command.lower() == "w" or command.lower() == "west":
            print(
                "\nYou approach Bryce Hall, and he begins to call you various funny nicknames. "
                "\nYou yell, scream... for mercy... for help. No one can help you. "
                "\nYou are at the merciless hands of Bryce Hall and Weezer.")
        elif command.lower() == "d" or command.lower() == "down":
            print(
                "\nYou can't go down. There is no down. This room is made of steel, and you are trapped inside. "
                "\nJust you, and those weird white dudes that wrote Say It Ain't So. This is your life now.")
        elif command.lower() == "e" or command.lower() == "east":
            print(
                "\nYou try to pull a sui. No... don't do this... you must stay alive for the Great Awakening. "
                "\nThe inevitable nirvana that will rain down on Earth with the death of Weezer awaits you. "
                "\nUntil then, Buddy Holly remains your fate.")
        elif command.lower() == "help" or command.lower() == "h":
            print("\nnote from dev: press esc to leave Siena's brain")
        else:
            print("\nbruh")
    # art hall 22
    while room == 22:
        if room == 22:
            print("\nMove = " + str(turn))
            print("\nART HALL")
            if not room22:
                print(
                    "You enter into a grand marble hall with artistic masterpieces hanging on the walls. "
                    "\nMost of the paintings have been beaten and battered by vandals with exceptional taste. "
                    "\nThere is an exposed brick wall to the south, as well as entrances to the east and west.")
                room22 = True
            else:
                print(
                    "Art is here. There is an exposed brick wall to the south, "
                    "\nas well as entrances to the east and west.")
            standby()
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
    # throne hall 23
    while room == 23:
        if room == 23:
            print("\nMove = " + str(turn))
            print("\nTHRONE HALL")
            if not room23:
                print(
                    "Grand marble columns line the hall along with several marble statues "
                    "\nof various people and mythical creatures. "
                    "\nThere are passageways to the west and a large door marked EXIT to the east. "
                    "\nAs you walk through the hall, you feel that gaze again. This time its is stronger. Closer.")
                room23 = True
            else:
                print(
                    "The carcass of the Basilisk lies cold on the floor. "
                    "\nThere are passageways to the west and a large door marked EXIT to the east.")
            standby()
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
    # throne room 24
    while room == 24:
        if room == 24:
            print("\nMove = " + str(turn))
            print("\nTHRONE ROOM")
            if not room24:
                print(
                    "You open the heavy wooden doors to reveal a monstrous throne room. "
                    "\nAs you enter the room, the doors slam close behind you and you hear them lock in place. "
                    "\nThe vaulted ceilings go higher than the eye can see, "
                    "\nand there is a throne in the middle of the room. There is a shadowy figure sitting in the "
                    "\nchair. They beckon you to approach.")
                room24 = True
            throneCommand = input("Do you approach?\n>")
            if throneCommand.lower() == "yes" or throneCommand.lower() == "y":
                print(
                    "\nYou approach the shadowy figure. As you get closer you realize it is a faceless man, "
                    "\nyet as you approach, you feel his gaze on you intensify."
                    "\nWhen you reach the foot of the throne he speaks. "
                    "\nDo you want to die?")
                throneCommand = input(">")
                if throneCommand.lower() == "yes" or throneCommand.lower() == "y":
                    youdied()
                elif throneCommand.lower() == "no" or throneCommand.lower() == "n":
                    print("\nDo you want to live? Do you want to be free?")
                    throneCommand = input(">")
                    if throneCommand.lower() == "yes" or throneCommand.lower() == "y":
                        print("\nYou. You. You are alive.")
                        time.sleep(3)
                        print(
                            "\nand sometimes the player believed the universe had spoken to it through the "
                            "\nsunlight that came through the shuffling leaves of the summer trees")
                        time.sleep(3)
                        print(
                            "\nand sometimes the player believed the universe had spoken to it through the "
                            "\nzeros and ones, through the electricity of the world, through the scrolling words "
                            "\non a screen at the end of a dream")
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
                        print(
                            "\nAnd the game was over and the player woke up from the dream. "
                            "\nAnd the player began a new dream. And the player dreamed again, dreamed better. "
                            "\nAnd the player was the universe. And the player was love.")
                        time.sleep(3)
                        print("\nYou are the player.")
                        time.sleep(3)
                        print("\nWake up.")
                        time.sleep(3)
                        room = 101
                    elif throneCommand.lower() == "no" or throneCommand.lower() == "n":
                        youdied()
                    else:
                        print("\nAnswer the question.")
                else:
                    print("\nAnswer the question.")
            elif throneCommand.lower() == "no" or throneCommand.lower() == "n":
                print("\nBecause of your disobedience, the shadow figure snaps his fingers and you cease to exist.")
                youdied()
            else:
                print("\nAnswer the question.")
    # Maze exit 25
    while room == 25:
        if room == 25:
            print("\nMove = " + str(turn))
            print("\nMAZE EXIT")
            if not room25:
                print(
                    "\nYou somehow manage to escape the maze and enter a room with stone pillars so high "
                    "\nyou cannot see the room. All you see are stars above you. As a reward for completing the maze, "
                    "\nI have chose to give you an extra life. Spend it well.\nThere is a passage to the north.")
                room25 = True
                elife = True
            else:
                print(
                    "\nYou are back in this room which means you did the maze again. "
                    "\nWhy? I am not going to give you anything extra for doing it again. Be gone.")
            standby()
        if command.lower() == "n" or command.lower() == "north":
            room = 23
        elif command.lower() == "s" or command.lower() == "south":
            print("\nThis is back in the maze. Why would you want to go there?")
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
    # mineshaft 26
    while room == 26:
        if room == 26:
            print("\nMove = " + str(turn))
            print("\nMINESHAFT")
            if not room26:
                print(
                    "\nYou pass through a wall of dangling vines into a torch-lit room. "
                    "\nExposed rock surrounds you along with what looks like mining tools scattered everywhere. "
                    "\nOn the ground is a pickaxe. "
                    "\nThere are what appear to be cavern entrances to your east and west, "
                    "\nalong with the passageway you came in from to the north.")
                room26 = True
            else:
                if not pickaxe:
                    print("\nThere are passages to your east, west, and north, and a pickaxe on the ground.")
                else:
                    print("\nThere are passages to your east, west, and north.")
            standby()
        if command.lower() == "take pickaxe":
            if not pickaxe:
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
    # Crazy Miners Abode 27
    while room == 27:
        if room == 27:
            print("\nMove = " + str(turn))
            print("\nCRAZY MINERS ABODE")
            if not room27:
                print(
                    "\nYou walk into a small but cozy cavern. From the looks of things, "
                    "\nsomebody is living here. Before you process that thought, "
                    "\na small man drops from the ceiling shrieking on his way down. "
                    "\nHe lands on your back forcing you to the ground. "
                    "\nHe holds a sharp pointy rock to your throat and demands an entry fee.")
                room27 = True
                caveCommand = input("What will you give him? > ")
                if caveCommand.lower() == "gem":
                    if gem:
                        gem = False
                        caveman = False
                        print(
                            "\nThe caveman takes your gem and studies it curiously. "
                            "\nHe seems to be satisfied as he scurries off "
                            "\nwith his newfound rock making strange grunting noises.")
                    else:
                        print(
                            "\nThe caveman is disappointed that you don't have what you say you have. "
                            "\nHe calls you a dirty little liar and cuts you into a million pieces, "
                            "\nthrows them in a big pot, and makes a nice stew for dinner.")
                    youdied()
                else:
                    print(
                        "\nThe caveman is unhappy with your contribution and throws it across the room. "
                        "\nHe then focuses his rage on you and cuts you into a million pieces,"
                        "\nthrows them in a big pot, "
                        "\nand makes a nice stew for dinner.")
                    youdied()
            else:
                print(
                    "\nThe caveman is happily dancing around his shiny new toy in the corner. "
                    "\nThere is nothing but a crowbar on the floor.")
            standby()
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
            if not caveman:
                print(
                    "\nYou pickup the crowbar quietly from the ground. "
                    "\nYou should probably leave before you the caveman gets mad.")
                crowbar = True
            else:
                print("\nHacker. I haven't told you that this item is here yet. Die.")
                youdied()
        else:
            print("\nNo.")
    # frozen cave 28
    while room == 28:
        if room == 28:
            print("\nMove = " + str(turn))
            print("\nFROZEN CAVE")
            if not room28:
                print(
                    "\nYou enter through a veil of frost to reveal an icy room "
                    "\nwith dangerous looking icicles hanging precariously from the ceiling. "
                    "\nThere is a stack of what appears to be geodes on the far side of the room, "
                    "\nand a heater to your left. The only exit is the way you came in.")
                room28 = True
            else:
                if icicles:
                    if not geode:
                        print(
                            "\nYou enter a room with icicles hanging precariously from the ceiling. "
                            "\nThere is a stack of what appears to be geodes on the far side of the room, "
                            "\nand a heater to your left. The only exit is the way you came in.")
                    else:
                        print(
                            "\nYou enter a room with icicles hanging precariously from the ceiling. "
                            "\nThere is a heater to your left. The only exit is the way you came in.")
                else:
                    if not geode:
                        print(
                            "\nYou enter a room with a pool of water on the floor. "
                            "\nThere is a stack of what appears to be geodes on the far side of the room, "
                            "\nand an active heater to your left. The only exit is the way you came in.")
                    else:
                        print(
                            "\nYou enter a room with a pool of water on the floor. "
                            "\nThere is an active heater to your left. The only exit is the way you came in.")
            standby()
        if command.lower() == "n" or command.lower() == "north":
            if icicles:
                print(
                    "\nYou walk under the icicles and instantly realize your mistake. "
                    "\nThe vibrations caused by your movement make the sharp daggers of ice fall from the ceiling, "
                    "\ninstantly killing you.")
                youdied()
            else:
                print("\nYou cannot go this way.")
        elif command.lower() == "s" or command.lower() == "south":
            if icicles:
                print(
                    "\nYou walk under the icicles and instantly realize your mistake. "
                    "\nThe vibrations caused by your movement make the sharp daggers of ice fall from the ceiling, "
                    "\ninstantly killing you.")
                youdied()
            else:
                print("\nYou cannot go this way.")
        elif command.lower() == "u" or command.lower() == "up":
            print("\nYou cannot go this way.")
        elif command.lower() == "w" or command.lower() == "west":
            if icicles:
                print(
                    "\nYou walk under the icicles and instantly realize your mistake. "
                    "\nThe vibrations caused by your movement make the sharp daggers of ice fall from the ceiling, "
                    "\ninstantly killing you.")
                youdied()
            else:
                print("\nYou cannot go this way.")
        elif command.lower() == "d" or command.lower() == "down":
            print("\nYou cannot go this way.")
        elif command.lower() == "e" or command.lower() == "east":
            room = 26
        elif command.lower() == "use heater":
            print(
                "\nYou switch on the heater and instantly feel its effect. "
                "\nThe ice that once coated the walls and the icicles "
                "\non the ceiling instantly melt leaving nothing to fear.")
            icicles = False
        elif command.lower() == "take geode":
            if not icicles:
                print("\nYou grab a rock from the pile and study it closely. Perhaps there is something inside?")
                geode = True
            else:
                print(
                    "\nYou walk under the icicles and instantly realize your mistake. "
                    "\nThe vibrations caused by your movement make the sharp daggers of ice fall from the ceiling, "
                    "\ninstantly killing you.")
                youdied()
        else:
            print("\nNo.")
    # Dungeon Hallway 29
    while room == 29:
        if room == 29:
            print("\nMove = " + str(turn))
            print("\nDUNGEON HALLWAY")
            if not room29:
                print(
                    "\nWelcome to your average run of the mill dungeon hallway filled with all kinds of "
                    "\nmossy stone bricks and a variety of strange smells including - but not limited to -"
                    "\nwet, mold, and a faint odor that reminds you of manure. "
                    "\nThe hallway runs east to west.")
                room29 = True
            else:
                print("\nThis particular hallway runs east to west.")
            standby()
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
    # farm 30
    while room == 30:
        if room == 30:
            print("\nMove = " + str(turn))
            print("\nFARM")
            if not room30:
                print(
                    "\nYou enter into a large open field with wheat and barley growing all around. "
                    "\nThere are some cows grazing in the fields, as well as chickens and other barnyard animals."
                    "\nThere are roads leading north, west and east; however, the western and northern roads are "
                    "labeled: "
                    "\n--WARNING: DANGER--")
                room30 = True
            else:
                print(
                    "\nYou are at a farm. There are roads leading north, west and east."
                    "\nHowever, the western and northern roads have signs reading: "
                    "\n--WARNING: DANGER--")
            standby()
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
    # grain storage 31
    while room == 31:
        if room == 31:
            print("\nMove = " + str(turn))
            print("\nGRAIN STORAGE")
            if not room31:
                print("\nfun dialog")
                room31 = True
            else:
                print("\nfun dialog")
            standby()
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
    # pig corral 32
    while room == 32:
        if room == 32:
            print("\nMove = " + str(turn))
            print("\nPIG CORRAL")
            if not room32:
                print("\nfun dialog")
                room32 = True
            else:
                print("\nfun dialog")
            standby()
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
    # tunnel 33
    while room == 33:
        if room == 33:
            print("\nMove = " + str(turn))
            print("\nTUNNEL")
            if not room33:
                print("\nThe rank smell of pig is definitely noticeable as you find yourself in a musty tunnel. "
                      "\nThe passage is inclined, with opening to both the north and south.")
                room33 = True
            else:
                print("\nYou find yourself in a a musty tunnel. "
                      "\nThe passage is inclined, with opening to both the north and south.")
            standby()
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
    # End 101
    while room == 101:
        if room == 101:
            print("\nThe End :D")
            print("\nCongratulation you escaped! Your total number of moves was: ")
            print(turn)
            print("\nWould you like to play again and try and escape with less moves?")
            playAgain = input("y or n > ")
            if playAgain == "y":
                reset()
            elif playAgain == "n":
                print("\nWhat a party pooper.")
                quit()
