print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


first_choice = input('You have come to a fork in the road.  Do you want to go LEFT or RIGHT? ').lower()

if first_choice == "left":
  second_choice = input("You come to the ocean.  Do you want to SWIM across or WAIT for a boat? ").lower()
  if second_choice == "wait":
    print("You come to a house with three doors.  One is RED, another is BLUE, and the third is YELLOW.")
    final_choice = input("Which color door do you choose? ").lower()
    if final_choice == "red":
      print("This room has an uncontrollable fire.  No treasure here.")
      print("GAME OVER")
    elif final_choice == "blue":
      print("You open the door and a flood of water rushes out.  You are carried with the surge back to the ocean.")
      print("GAME OVER")
    elif final_choice == "yellow":
      print("Inside, you find a treasure chest.  You walk over and find that it opens easily and is filled with gems and gold. YOU WIN!")
    else:
      print("GAME OVER")
  else:
    print("A short way into the swim, you are stung by a jellyfish and have to turn around because you are too far from the other side.")
    print("GAME OVER")
else:
  print("You fall into a hidden hole.")
  print("GAME OVER")