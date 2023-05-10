def print_instructions():
    # Displays title of the game and instructions
    print("Star Wars Text Adventure Game")
    print("Collect 6 items to defeat Darth Bane and save the galaxy")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get <item name>")

def print_status(c_room, inventory, rooms):
    # Prints the current status of the player:
    #room they're in
    #items they have
    #what is in the room
    print(f"\nYou are on {c_room}")
    print(f"Inventory: {inventory}")

    if "item" in rooms[c_room]:
        # Check to see if the word is "a" or "an"
        if rooms[c_room]["item"][0].lower() in "aeiou":
            print(f"You see an {rooms[c_room]['item']}")
        else:
            print(f"You see a {rooms[c_room]['item']}")
    else:
        print(f"This room is empty")

    print("-----------------")

def make_move(c_room, inventory, rooms):
    # Allows player to make a move based on what items they have
    # And what room they are in
    move = input("Enter your move: ").lower()
    print()
    if move == "go north" and "North" in rooms[c_room]:
        print(f"You moved to {rooms[c_room]['North']}")
        return rooms[c_room]["North"]

    elif move == "go east" and "East" in rooms[c_room]:
        print(f"You moved to {rooms[c_room]['East']}")
        return rooms[c_room]["East"]

    elif move == "go south" and "South" in rooms[c_room]:
        # Check if they are moving into the boss room without proper equipment
        if rooms[c_room]["South"] == "Death Star" and len(inventory) != 6:
            while True:
                print("You do not have all the items, are you sure you want to proceed?")
                choice = input("Enter yes or no: ").lower()
                if choice == "yes":
                    break
                elif choice == "no":
                    return c_room
                else:
                    print("Invalid choice, please try again\n")
        print(f"You moved to {rooms[c_room]['South']}")
        return rooms[c_room]["South"]

    elif move == "go west" and "West" in rooms[c_room]:
        print(f"You moved to {rooms[c_room]['West']}")
        return rooms[c_room]["West"]

    elif "item" in rooms[c_room] and move == f"get {rooms[c_room]['item'].lower()}":
        print(f"You picked up the {rooms[c_room]['item']}")
        inventory.append(rooms[c_room]['item'])
        del rooms[c_room]['item']
        return c_room

    else:
        print("Invalid move made")
       
            


def main():
    # A dictionary linking all the rooms and detailing what is inside of each room
    rooms = {"Mustafar": {"South": "Korriban", "item": "Droid"},
             "Korriban": {"North": "Mustafar", "East": "Hoth", "item": "Lightsaber"},
             "Hoth": {"North": "Endor", "East": "Dathomir", "South": "Geonosis", "West": "Korriban", "item": "Blaster"},
             "Endor": {"East": "Coruscant", "South": "Hoth", "item": "Ewok Army"},
             "Coruscant": {"South": "Dathomir", "West": "Endor"},
             "Dathomir": {"North": "Coruscant", "South": "Death Star", "West": "Hoth", "item": "Sith Holocron"},
             "Geonosis": {"North": "Hoth", "item": "Holocron"},
             "Death Star": {"North": "Dathomir", "item": "Darth Bane"}}
    
    c_room = "Coruscant"
    inventory = []

    while True:
        print_status(c_room, inventory, rooms)

        # If they are facing the boss
        if c_room == "Death Star":
            if len(inventory) == 6:
                print("Congratulations! You have collected all the items and defeated Darth Bane!")
                print("You have brought peace to the galaxy. Thank you for playing.")
            else:
                print("AAAAH, Darth Bane has killed you")
                print("You have failed to bring peace to the galaxy. Thank you for playing.")
            break

        new_room = make_move(c_room, inventory, rooms)
        if new_room:
            c_room = new_room

main()