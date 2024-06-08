print('''
                                                 
                                         |
                                         |
                                         |
   _______                   ________    |
  |ooooooo|      ____       | __  __ |   |
  |[]+++[]|     [____]      |/  \/  \|   |
  |+ ___ +|     ]()()[      |\__/\__/|   |
  |:|   |:|   ___\__/___    |[][][][]|   |
  |:|___|:|  |__|    |__|   |++++++++|   |
  |[]===[]|   |_|_/\_|_|    | ______ |   |
_ ||||||||| _ | | __ | | __ ||______|| __|
  |_______|   |_|[::]|_|    |________|  
              \_|_||_|_/               jro
                |_||_|                     
               _|_||_|_                     
      ____    |___||___|                     
     /  __\          ____                     
     \( oo          (___ \                     
     _\_o/           oo~)/
    / \|/ \         _\-_/_
   / / __\ \___    / \|/  
   \ \|   |__/_)  / / .- \ 
    \/_)  |       \ \ .  /_/
     ||___|        \/___(_/
     | | |          | |  |
     | | |          | |  |
     |_|_|          |_|__|
     [__)_)        (_(___]
      ''')
while True:
    
    print("Welcome to Engineer's Odyssey: Robo Rescue.")
    user_input = input("Type 'init' to start your adventure : ").lower()
    if user_input == 'init':
        break
    else:
      print("Invalid input. Please type 'init' to start the game.")


print("Your adventure begins now!")
print("You find yourself in a labratory filled with various robotic parts.")
print("There are two doors: one to your left and one to your right.")
print('''
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
ejm        |__________|
      ''')

while True:
    choice = input("Do you choose the left door or the right door? (left/right) : ").lower()
    if choice == 'left':
        print("You enter the left door and find a room full of advanced robotic prototypes.")
        print("One of the robots suddenly comes to life and greets you. It asks you for help to complete it's programming.")
        print("Do you agree to help the robot or do you leave the room? (help/leave)")
    
        while True:
            action = input("What do you do? (help/leave) : ").lower()
            if action == 'help':
                print("You agree to help the robot. Together, you manage to complete it's programming and it offers to assist you in your quest.")
                print("The robot guides you to a hidden passage behind the room, leading you to the main control center of the lab.")
                print("In the control center, you see a panel with two buttons: one red and one blue.")

                while True: 
                    button = input("Do you press the red button or the green button? (red/blue) : ").lower()
                    if button == 'red':
                        print("You press the red button and the alarms begin blaring. Security robots storm the room and apprehend you.")
                        print("Game Over...")
                        break
                    elif button == 'blue':
                        print("You press the blue button and a screen flickers on. You're able to make out the main systems controlling the rogue robots.")
                        print("You shut down the systems and watch all the rogue robots slowy power down and begin falling over.")
                        print("Congratulations, you've completed your quest to save the lab!")
                        break
                    else:
                        print("Invalid choice. Please type 'red' or 'blue'.")
                break
            elif action == 'leave':
                print("You decide to leave the room, but as you turn around, the door locks.")
                print("The robot approaches you and in a static voice says 'If you wont help me, You'll join me here forever.")
                print("Game Over...")
                break
            else:
                print("Invalid choice. Please type 'help' or 'leave'.")
        break
    elif choice == 'right':
        print('''
              ________________
              | /~~~~~~~~\ ||||
              ||          |...|
              ||          |   |
              | \________/  O |
              ~~~~~~~~~~~~~~~~
              ''')
        print("You enter the right door and find a control room with many monitors and buttons.")
        print("On one of the monitors, you see a distress signal from the nearby robotic assembly line.")
        print("Do you investigate the signal or ignore it and explore the room? (investigate/ignore)")

        while True:
            action = input("What do you do? (investigate/ignore) : ").lower()
            if action == 'investigate':
                print("You decide to investigate the signal. You discover that the assembly line is malfunctioning and producing rogue robots.")
                print("Using the control panel, you manage to halt and reprogram the rogue robots to assist you.")
                print("With the help of the reprogrammed robots, you uncover a secret hatch leading to an underground lab.")
                print("While in the underground lab, you find a panel with two levers: one green and one yellow.")
                print('''
                     ___ (@)
                    |.-.|/
                    || |/
                    || /|
                    ||/||
                    || ||
                    ||_||
                    '---'

                LGB                  
                      ''')
                while True: 
                    lever = input("Do you pull the green lever or the yellow? (green/yellow) : ").lower()
                    if lever == 'green':
                        print("You pull the green lever and the lights go out. Security robots storm in apprehend you in the darkness.")
                        print("Game Over...")
                        break
                    elif lever == 'yellow':
                        print("You pull the yellow lever and a secret door opens, revealing the main control systems responsible for the rogue robots.")
                        print("You shut down all operations, powering down the assembly line and restoring power back to the upper levels of the lab.")
                        print("Congratulations, you've completed your quest to save the lab!")
                        break
                    else:
                        print("Invalid input, please type 'green' or 'yellow'.")
                break
            elif action == 'ignore':
                print("You decide to ignore the signal and explore the room. You find a keycard that grants you access to restricted areas of the lab.")
                print("Using the keycard, you open a door that leads to the reactor room of the lab.")
                print("As you approach the controls for the reactor, you spot a mechanics toolkit below what looks like a panel that was being worked on.")
                while True:
                    repair = input("Do you continue towards the reactor controls or the panel next to the toolkit? (controls/panel) : ").lower()
                    if repair == 'controls':
                        print('''
                            ____________________________________                 ______________
                            |------|------|     __   __   __     |     ___________     |           () |
                            | 64X4 | 64X4 | || |  | |  | |  |    |    |           |    |           ___|
                            |------|------| || |  | |  | |  |    |____|           |____|         || D |
                            | 64X4 | 64X4 | || |__| |__| |__|                 ________________  ||| I |
                            |------|------|  |  ________   ______   ______   | ADV476KN50     | ||| P |
                            | 64X4 | 64X4 |    |TRIDENT | |______| |______|  | 1-54BV  8940   | ||| S |
                            |------|------| || |TVGA    | |______| |______|  |________________| |||___|
                            | 64X4 | 64X4 | || |8800CS  |          ________________                ___|
                            |------|------| || |11380029|    LOW->|  /\ SUPER VGA  | _________    |   |
                            | 64X4 | 64X4 |     --------    BIOS  | \/         (1) ||_________|   | 1 |
                            |------|------| ||  ______  J  ______ |________________| _________    | 5 |
                            | 64X4 | 64X4 | || |______| 2 |______| ________________ |_________|   |___|
                            |------|------| ||  ________   ______ |  /\ SUPER VGA  |               ___|
                            | 64X4 | 64X4 |    |________| |______|| \/         (2) |   _________  |   |
                            |------|------| ()              HIGH->|________________|  |_________| | 9 |
                            | 64X4 | 64X4 |     ________   _________   _____________   _________  |   |
                            |______|______|__  |________| |_________| |_____________| |_________| |___|
                                            |               __    TVGA-1623D                    _ () |
                                            |LLLLLLLLLLLLLL|  |LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL| |___|
                                                                                                    |
                                                                                                    |
                              ''')
                        print("You disregard the panel left behind and go towards the reactor controls.")
                        print("With a sudden sense of uncertainty, you begin messing with the controls. Your hands drift towards a a screen on the left.")
                        print("A Crack bursts out of the main pipe, in a  single moment, the room flashes, followed by the sounds of destuction, then silence.")
                        print("Game Over...")
                        break
                    elif repair == 'panel':
                        print('''
                            ___________________________
                            |[]                        []|
                            |[]                        []|
                            |                            |
                            |            . .             |
                            |          `    _`           |
                            |         `  ()|_|`          |
                            |         `       `          |
                            |          ` . . `           |
                            |      ________________      |
                            |     |          ____  |     |
                            |     |         |    | |     |
                            |     |         |    | |     |
                            |     |         |    | |     |
                            |()   |         |_  _| |   ()|
                            |)    |           --   |    (|
                        das |_____|[]______________|\___/
                              ''')
                        print("You dismiss the reactor, approaching the panel on the wall.")
                        print("You spot a trail a blood trailing off and a pair of wire cutters left behind.")
                        print("picking up the tool you glance back at the panel, removing the cover reveals several red wires.")
                        print("a sudden chill climbs up your back, without hesitation you jab at the wires and cut the wires.")
                        print("all operations have been stopped, emergency power started up and all rogue robots have powered down.")
                        print("Congratulations, You managed to save the lab!")
                        break
                    else:
                        print("Invalid input, please type 'controls' or 'panel'.")
                break
            else: 
                print("Invalid choice. Please type 'investigate' or 'ignore'.")
        break
    else:
        print("Invalid choice. Please type 'left' or 'right'.")
    
