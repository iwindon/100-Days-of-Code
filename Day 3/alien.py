import os
print('''

               \.   \.      __,-"-.__      ./   ./
           \.   \`.  \`.-'"" _,="=._ ""`-.'/  .'/   ./
            \`.  \_`-''      _,="=._      ``-'_/  .'/
             \ `-',-._   _.  _,="=._  ,_   _.-,`-' /
          \. /`,-',-._"""  \ _,="=._ /  """_.-,`-,'\ ./
           \`-'  /    `-._  "       "  _.-'    \  `-'/
           /)   (         \    ,-.    /         )   (
        ,-'"     `-.       \  /   \  /       .-'     "`-,
      ,'_._         `-.____/ /  _  \ \____.-'         _._`,
     /,'   `.                \_/ \_/                .'   `,
    /'       )                  _            Krogg (       `
            /   _,-'"`-.  ,++|T|||T|++.  .-'"`-,_   
           / ,-'        \/|`|`|`|'|'|'|\/        `-, 
          /,'             | | | | | | |             `,
         /'               ` | | | | | '               `
                            ` | | | '
                              ` | '

''')
print("Welcome to Alien Escape")
print("Your mission is escape the space station.") 

print("You wake up to find yourself on a dark space craft that has been boarded by a hostile alien")
print("You need to find your way to the escape pod as fast as possible.")
print("")
choice1 = str(input("You head down the hallway and come to a junction, do you turn left or right. (left / right): "))
if (choice1 == "left"):
    os.system('clear')
    choice2 = input("You walk down the cold dark hallway until you reach the elevator.  Do you take the stairs or wait for the elavator? (stairs / wait): ")
    if choice2 == "stairs":
        os.system('clear')
        print("You run up 30 flights of stairs, the adrenealine pupping in your system, knowing you are getting closer to escaping.")
        choice3 = input("You arive at the escape pod deck and are confronted with 3 doors, which pod do you want (1 / 2 / 3): ")
        if choice3 == "1":
            os.system('clear')
            print("You jump into POD 1, press the emergency launch button.")
            print("The POD bay doors close, and you are launched safely into space.")
        elif choice3 == "2":
            os.system('clear')
            print("You jump into POD 2, press the emergency launch button, yet nothing happens!")
            print("You frantically press the button over and over when you hear the alien come up behind you.")
            print("Game Over")
        else:
            os.system('clear')
            print("You jump into POD 3, press the emergency launch button.")
            print("The launch system has a catastrophic malfunction and your pod is destroyed in a ball of plasma.")
            print("Game Over")
    else:
        os.system('clear')
        print("While waiting for the slow elevator, the alien catches up from you and kills you.")
        print("Game Over")
else:
    os.system('clear')
    print("You walk a short way down the hall when the Alien jumps out and kills you.")
    print("Game Over")    
