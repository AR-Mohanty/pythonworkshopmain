print("Welcome to Treasure Island\n\nYour mission to find the treasure\n\nyou are at a cross road")
direction = input("Where do you want to go? (left or right) => ").lower()

if direction == 'left':
    wait_or_swim = input(
        "you came to a lake.\n There is an island in the middle of the lake.\nType 'Wait' to wait for boat "
        "and 'Swim' to swim across => ")
    if wait_or_swim == 'wait':
        color_choice = input("you have arrived at the island unharmed.\nThere is a house with three doors one read, "
                             "one yellow and "
                             "one blue. => ")
        if color_choice == 'red' or color_choice == 'blue':
            print("You enter a room of beast.Game Over")
        else:
            print("Congratulations!. you got the 'Treasure'. you won the game")
    else:
        print("Game over")
else:
    print("Game over")


