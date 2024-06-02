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

print("Welcome to Engineer's Odyssey: Robo Rescue.")
user_input = input("Type 'init' to start your adventure: ").lower()

if user_input == 'init':
    print("Your adventure begins now!")
    print("You find yourself in a labratory filled with various robotic parts.")
    print("There are two doors: one to your left and one to your right.")
    choice = input("Do you choose the left door or the right door? (left/right): ").lower()

else:
    print("Invalid input. Please type 'init' to start the game.")
