# Daniel Simpson

# This dictionary links all the rooms together along with each room's respective item
rooms = {
    'cellar': {'east': 'hallway'},
    'hallway': {'north': 'study', 'south': 'library', 'west': 'cellar', 'east': 'laboratory', 'item': 'boots'},
    'study': {'east': 'dungeon', 'south': 'hallway', 'item': 'diamond ring'},
    'library': {'north': 'hallway', 'east': 'kitchen', 'item': 'garfield comic'},
    'kitchen': {'west': 'library', 'item': 'split pea soup'},
    'laboratory': {'north': 'craft room', 'west': 'hallway', 'item': 'love potion'},
    'craft room': {'south': 'laboratory', 'item': 'mushy mothers day card'},
    'dungeon': {'west': 'study', 'item': 'agrona'}
}


# This function captures the player's name, and displays a welcome message
def intro():
    player_name = input('Enter Your Name: ').lower()
    print('Welcome' + ' ' + player_name.title() + '!')
    print("In the depths of your slumber, a cloth smothers your face, stealing consciousness."
          "\nAbruptly awakened, you find yourself trapped in a chilling room reeking of chemicals."
          "\nA note reveals the sinister presence of Agrona, commanding you to gather six essential"
          "\nitems before facing a fatal encounter. With time slipping away, embark on a perilous journey"
          "\nthrough the castle's chambers, armed with bravery and determination."
          "\nSurvive or succumb. Your fate hangs in the balance.")


# This function displays a list of commands the user can input
def commands():
    print('Move commands: south, north, east, west')
    print('Add to Inventory: get "[item name]"')
    print('Enter "exit" to leave')

# This function tells the player the current room they are in, displays their current inventory, and displays
# the item in the current room


def status(current_room, player_inventory, items_in_inventory):
    print('You are currently in the:', current_room.capitalize())
    print('Inventory:', player_inventory, 'Number of items:', items_in_inventory)
    if 'item' in rooms[current_room]:
        item = rooms[current_room]['item']
        if item not in player_inventory:
            print('You Discover a:', item)
            return item

    return "None"


# This function is the main 'brains' of the program and allows the player to exit at any time before winning or loosing
def main():
    player_inventory = []  # This holds the player's inventory and is updated as the player collects items
    current_room = 'cellar'  # This is the room the player starts in and is updated as the player moves around
    item = ""  # This serves as a place-holder for the items to be discovered and collected as the player moves around
    intro()
    commands()
    items_in_inventory = player_inventory.count(item)
    while True:
        item = status(current_room, player_inventory, items_in_inventory)
        command = input('Enter Command: ').lower()
        if command == 'exit':
            print("You can't get out that easy! Agrona finds you and eats you")
            break
        elif command in rooms[current_room].keys():
            current_room = rooms[current_room][command]
        elif item != 'None' and command == 'get ' + item:
            print(item.capitalize(), "collected.".capitalize())
            player_inventory.append(item)
            items_in_inventory += 1
        else:
            print('Invalid Command! The list of commands are:')
            commands()
        if current_room == 'dungeon':
            if items_in_inventory == 6:
                print('Congratulations, valiant adventurer! Against all odds, you have'
                      '\ndefied my machinations and emerged triumphant. With unwavering determination,'
                      '\nyou sought out every hidden chamber, retrieving the six sacred items that were once'
                      '\nscattered throughout my labyrinthine castle. Your resourcefulness and courage have'
                      '\nproven to be your greatest allies, and I commend your indomitable spirit.'
                      '\nThanks for Playing!')
                break
            elif items_in_inventory < 6:
                print('In a cruel twist of fate, your valiant efforts have been vanquished, and the jaws'
                      '\nof doom close in upon you. No longer shall your name be whispered among the brave, for'
                      '\nyour light fades into oblivion. The darkness relishes your demise, as the tendrils of its'
                      '\nhunger consume your very essence. May your tragic tale serve as a warning to all who dare'
                      '\ndefy the realm of Agrona, a chilling testament to the indomitable power that lies within.'
                      '\nThanks for playing! Better luck next time!')
                break


main()
