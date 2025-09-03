print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
#Treasure Island Project
#An Adventure Game to find the Right Path.
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_move = input("DO you want to move Left or Right? (left/right).\n").lower()
if first_move == "left" or first_move == "l":
    second_move = input("Do you want to Swim or Wait? (s/w).\n").lower()
    if second_move == "w" or second_move == "wait":
        third_move = input("Which Door do you want to Enter? (R/G/Y/B).\n").lower()
        if third_move == "y":
            print("Congratulation. Reached at Iceland.\nYou Won!")
        elif third_move == "r":
            print("Burned by fire.\nGame Over.")
        elif third_move == "g":
            print("Too Close.\nGame Over")
        elif third_move == "b":
            print("Nope. Eaten by beats.\nGame Over.")
        else:
            print("Please Go fior valid Choice.\nGame Over.")
    elif second_move == "s" or second_move == "swim":
        print("Attacked by A Trout.\nGame Over")
    else:
        print("Please Go fior valid Choice.\nGame Over.")
elif first_move == "r" or first_move == "right":
    print("Rong Decicion. Fall in a Whole.\nGame Over")
else:
    print("Please Go fior valid Choice.\nGame Over.")


#Asadaf Writes