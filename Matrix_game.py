import random
import time

print(input("Click enter button to start"))

print("Welcome to the Matrix Game")
ans = input("Before you get to know about the Matrix, please tell me your name: ")
print("Welcome", ans , "! You have just discovered the truth...")
morpheus = ("The Matrix is a dangerous place, but it is also the reality. To know it, you need to take one pill")
print(morpheus)
time.sleep(1)
print("")
print("If you take the blue pill, then you forget about everything and go back to your old delusional world.")
time.sleep(1)
print("")
print("If you take the red pill, you will see how the world you see is actually a simulated world created by computers and programs, which isn't real but just a delusional dream.")
time.sleep(1)
print("")
print("The choice is up to you,",ans,"... Remember, I'm only offering the truth, nothing more.")
pill = input("Do you take the red pill or the blue pill? (type 'red' or 'blue'): ")
print("")
if pill.lower() == "red":
    print("You have chosen the red pill. Welcome to the real world!")
    time.sleep(1)
    print("You now have recognized the matrix and to escape from here pick any one door")
    doors = ["treasure chest", "monster", "nothing"]
    random.shuffle(doors)
    door = input("Which door do you choose? (type '1', '2', or '3'): ")
    while door not in ["1", "2", "3"]:
        print("Invalid input. Please try again.")
        door = input("Which door do you choose? (type '1', '2', or '3'): ")
    print("You have entered door", door)
    door_idx = int(door) - 1
    if doors[door_idx] == "treasure chest":
        print("You have entered a room with a treasure chest.")
        time.sleep(1)
        choice = input("What would you like to do? (type 'open chest' or 'search room'): ")
        if choice.lower() == "open chest":
            print("You have found a pile of gold coins!")
            time.sleep(1)
            print("Congratulations, you have completed the game!")
        elif choice.lower() == "search room":
            print("You have found a map that shows the way out of the matrix!")
            time.sleep(1)
            print("Congratulations, you have completed the game!")
        else:
            print("Invalid input. Please try again.")
    elif doors[door_idx] == "monster":
        print("You have entered a room with a monster.")
        time.sleep(1)
        print("The monster attacks you and you die.")
        time.sleep(1)
        print("Game over.")
    elif doors[door_idx] == "nothing":
        print("You have entered a room with nothing in it.")
        time.sleep(1)
        print("You spend some time searching the room, but find nothing of interest.")
        time.sleep(1)
        print("You return to the starting room.")
    else:
        print("Invalid input. Please try again.")

elif pill.lower() == "blue":
    print("You have chosen the blue pill. You will forget everything and go back to your ordinary life.")
    time.sleep(1)
    print("Game over.")

else:
    print("Invalid input. Please try again.")


    
