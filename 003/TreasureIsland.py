print("---TREASURE ISLAND---")

print('''
                     ,     _,
                    #\`-"-'/
                   #/   o (o
                  #/ \__   '._
  ,_#_#          #/  /=/`-. _")
   '-.`\#       #/  /=(_.. `-`.
      \ `\#    #/  -.'`_|||`_|
       ;  \#  #/ '.__.'=\_.'
       |   '-#;    _|====\_
       ;      '  /`  `\==| |
        \     .        \=| /
         '-.._         // /__
              `)-.    `----._|
       jgs    <_________\_\_|
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choiceCrossRoad = input("You\'re at a cross road. Where do you want to go? Type left or right \n").lower()
if (choiceCrossRoad == "left"):
    choiceLake = input("You\'ve come to a lake. There is an island in the middle of the lake. Type wait to wait for a boat. Type swim to swim across. \n").lower()
    if choiceLake == "wait":
        choiceDoors = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if choiceDoors == "red":
            print("It's a room full of fire. Game Over.")
        elif choiceDoors == "yellow":
            print("You found the treasure! You Win!")
        elif choiceDoors == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("Something is coming. It's the Dragon. GameOver!")
else:
    print("Something is coming. It's the Dragon. GameOver!")
