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
     /,'   `.                \_/ \_/                .'   `,\\
    /'       )                  _            Krogg (       `\\
            /   _,-'"`-.  ,++|T|||T|++.  .-'"`-,_   \\
           / ,-'        \/|`|`|`|'|'|'|\/        `-, \\
          /,'             | | | | | | |             `,\\
         /'               ` | | | | | '               `\\
                            ` | | | '
                              ` | '

''')
print("Welcome to Alien Escape")
print("Your mission is escape the space station.") 
input("Press ENTER when you are ready...")

os.system('clear')
print("You wake up to find yourself on a dark space station that has been boarded by a hostile alien")
print("The alarm klaxons are ringing through the ship, with an automated message repeating...")
print("ALERT, ALERT: Abandon ship, intruder alert!")
print("You need to find your way to the escape pod as fast as possible!")
print("")
print("")
choice1 = str(input("You head down the hallway and come to a junction, do you turn left or right. (left / right): "))
if (choice1 == "left"):
    os.system('clear')
    choice2 = input("You walk down the cold dark hallway until you reach the elevator bay. \nDo you take the stairs or wait for the elevator? (stairs / wait): ")
    if choice2 == "stairs":
        os.system('clear')
        print("You run up 30 flights of stairs, the adrenealine pumping in your system, knowing you are getting closer to escaping.")
        choice3 = input("You arive at the escape pod deck and are confronted with 3 escape doors, which pod do you want (1 / 2 / 3): ")
        if choice3 == "1":
            os.system('clear')
            print("You jump into POD 1, press the emergency launch button.")
            print("The POD bay doors close, and you are launched safely into space.")
            print("Congratulations on making it off the space station alive")
        elif choice3 == "2":
            os.system('clear')
            print("You jump into POD 2, press the emergency launch button, yet nothing happens!")
            print("You frantically press the button over and over when you hear the alien come up behind you.")
            print("Game Over")
        else:
            os.system('clear')
            print("You jump into POD 3, press the emergency launch button.")
            print("The launch system has a catastrophic malfunction and your POD is destroyed in a ball of plasma.")
            print("Game Over")
    else:
        os.system('clear')
        print("While waiting for the slow elevator, the alien catches up to you and kills you.")
        print("Game Over")
else:
    os.system('clear')
    print("You walk a short way down the hall when the Alien jumps out and kills you.")
    print("Game Over")    
