#prints the welcome Message To the user
print("~~~~~WELCOME TO TREASURE ISLAND~~~~~ \n your mission is to find the hidden treasure.")
while True:
#Starts the game askinf for the the gamers decision
  direction = input("You are at a crossroad. where do you want to go? Type 'LEFT'⬅️  or 'RIGHT'➡️  or Enter 'QUIT'❎ to quit the game: ").lower()
  if direction == "right":
      print("==" * 20)
      print("Game Over what's right of you doesn't always seem right lol!!!!")

      #statement to end the game
  elif direction == "quit":
      print("==" * 20)
      print("Game Ended. We Hate to see you go come back soon Treasure Hunter, Great Treasures Await your discovery!!!")
      break    
  
  elif direction == "left":
      print("you reach a lake. There is an island in the middle of the lake.")
      lake_decision = input("Type 'WAIT' to wait for a boat or 'SWIM' to swim across.: ").lower()

      if lake_decision == "swim":
          print("==" * 20)
          print("Game Over 😭😭😭 You Swam in shark infested waters and got eaten!!!")
        #Nested Statements for the adventure game that is more decision based
      elif lake_decision == "wait":
          print("==" * 20)
          print("You were patient enough a boat ⛵ came by and you crossed safely. You arrive at the island unharmed. ")
          door_selection = input("There are three doors one RED, one BLACK, one YELLOW\n "
                               "enter 'YELLOW'🟡 or 'RED'🔴 or 'BLACK'⚫ to pick a door: ").lower()
          
          if door_selection == "red":
              print("==" * 20)
              print("Game Over 😭😭😭 You picked the danger color and entered a room full of fire!!")

          elif door_selection == "yellow":
              print("==" * 20)
              print("You have entered a room filled with snow and frozed up, Game Over!!")

          elif door_selection == "black":
              print("==" * 20)
              print("CONGRATULATIONS SEEKER!! You found the hidden treasure.🍾🍾🍾🍾🍾 ")
              #break to end the loop after the gamer wins the game
              break
          
            # else statements to control invalid inputs 
          else:
              print("==" * 20)
              print("pick valid door-color selection!! 'YELLOW'🟡 or 'RED'🔴 or 'BLACK'⚫")
      else:
          print("==" * 20)
          print("Invalid ❌ selection!")   
  else:
      print("==" * 20)
      print("invalid ❌ Input pick a direction")
      