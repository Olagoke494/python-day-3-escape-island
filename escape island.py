print("welcome to the escape the mysterious island game")
print("Your mission is to escape the island traps")

direction = input("Do you want to direction left or right?").strip().lower()

if direction == "left":
    print("you can enter the jungle and continue")
    choice = input("Do you want to swim or wait?").strip().lower()
    if choice == "wait":
        print("You can now cross the river")
        door = input("which door do you want to open? red, blue or yellow?").strip().lower()
        if door == "red":
            print("a dangerous animal attacks.Game over")
        elif door == "blue":
            print("the room is filled with poisonous gas. Game over")
        elif door == "yellow":
            print("you have discovered a secret tunnel. You can continue")
            item_choice = input("which item do you want to choose?, map or golden key").strip().lower()
            if item_choice == "golden key":
                print("you unlock a hidden boat and won")
                print("you successfully escape the mysterious island")
                print("congratulations you win")
            elif item_choice == "map":
                print("the map is a trap. You lost. Game over")
            else:
                print("invalid input")
        else:
            print("invalid input")

    elif choice == "swim":
        print("game over, you have been attacked by a crocodile")
    else:
        print("invalid input")
elif direction == "right":
    print("game over")
else:
    print("invalid input")


