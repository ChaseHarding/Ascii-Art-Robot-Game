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
    user_input = input("Type 'init' to start your adventure: ").lower()
    if user_input == 'init':
        break
    else:
      print("Invalid input. Please type 'init' to start the game.")


print("Your adventure begins now!")
print("You find yourself in a labratory filled with various robotic parts.")
print("There are two doors: one to your left and one to your right.")

while True:
    choice = input("Do you choose the left door or the right door? (left/right): ").lower()
    if choice == 'left':
        print("You enter the left door and find a room full of advanced robotic prototypes.")
        print("One of the robots suddenly comes to life and greets you. It asks you for help to complete it's programming.")
        print("Do you agree to help the robot or do you leave the room? (help/leave)")
    
        while True:
            action = input("What do you do? (help/leave): ").lower()
            if action == 'help':
                print("You agree to help the robot. Together, you manage to complete it's programming and it offers to assist you in your quest.")
                print("The robot guides you to a hidden passage behind the room, leading you to the main control center of the lab")
                break
            
            elif action == 'leave':
                print("You decide to leave the room, but as you turn around, the door locks.")
                print("The robot approaches you and in a static voice says 'If you wont help me, You'll join me here forever.")
                print("Game Over.")
              
        

    elif choice == 'right':
        print('''
              ________________
              | /~~~~~~~~\ ||||
              ||          |...|
              ||          |   |
              | \________/  O |
              ~~~~~~~~~~~~~~~
              ''')
        print("You enter the right door and find a control room with many monitors and buttons")
        
        break
    else:
        print("Invalid choice. Please type 'left' or 'right'.")
    
