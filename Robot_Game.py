import random

# Map zones 
locations = {
    "Nothing": "You are in a barren area with nothing around.",
    "Power Station": "You found a power station! It contains power cells."
}

# Robot starting point
player_location = "Nothing"
power_cells = 5
max_power_cells = 10

def show_status():
# Displays robot's position and amount of power cells in inv
    print(f"\nLocation: {player_location}")
    print(locations[player_location])
    print(f"Power Cells: {power_cells}")

def move():
# The robot will either get nothing or 1 - 2 power cells based on luck
    global player_location, power_cells
    if power_cells > 0:
        # There is a 50% chance to find a power station or nothing
        if random.choice([True, False]): 
            player_location = "Power Station"
            # Based on luck, the robot gets 1-2 power cells
            cells_collected = random.randint(1, 2)
            power_cells += cells_collected
            print(f"You moved and found a Power Station! You collected {cells_collected} power cells.")
        else:
            player_location = "Nothing"
            print("You moved and found nothing.")
        power_cells -= 1  # The robot consumes 1 power cell every time it moves
    else:
        print("You don't have enough power cells to move!")

def check_game_status():
    # If the robot has 0 power cells,  you lose the game
    if power_cells <= 0:
        print("You have run out of power cells. Game Over!")
        return True
    # If the robot manages to collect 10 power cells, you win the game
    elif power_cells >= max_power_cells:
        print("Congratulations! You've collected 10 power cells. You win!")
        return True
    return False

def main():
    # loop
    print("Welcome to the Robot Explorer Game!")
    
    while True:
        show_status()
        
        if check_game_status():
            break
        
        action = input("\nWhat would you like to do? (move, quit): ").strip().lower()
        
        if action == "move":
            move()
        elif action == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid action. Please choose again.")

if __name__ == "__main__":
    main()
