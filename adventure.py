import sys
import json
import argparse



class Adventure:
    def __init__(self, map):
        self._load(map)
        self.current_room = 0
        self._inventory = []
        list_of_verbs = []
        for verb in dir(self):
            if "_" not in verb:
                list_of_verbs.append(verb)
        self.verbs = list_of_verbs
    
    def _load(self, map):
        try:
            with open(map, 'r') as file:
                self.map_data = json.load(file)
        except FileNotFoundError:
            print("Map File not found")
            sys.exit(1)
        except json.JSONDecodeError:
            print("JSON Decode Error: incorrect json format")
            sys.exit(1)
    
    def look(self):
        room = self.map_data[self.current_room]
        print(f"> {room['name']}\n")
        print(f"{room['desc']}\n")
        if 'items' in room:
            print(f"Items: {' '.join(room['items'])}")
        print(f"Exits: {' '.join(room['exits'])}\n")
    
    def go(self, direction):
        room = self.map_data[self.current_room]
        if direction in room["exits"]:
            print(f"You go {direction}.\n")
            self.current_room = room["exits"][direction]
            self.look()
        else:
            print(f"There's no way to go {direction}.")
    
    def inventory(self):
        if not self._inventory:
            print("You're not carrying anything.")
        else:
            print("Inventory:")
            for item in self._inventory:
                print(f"  {item}")
    
    def get(self, item):
        room = self.map_data[self.current_room]
        if 'items' in room:
            if item in room['items']:
                if item == "diamond":
                    print("Oops! diamond is locked in a safe.")
                    print("You'll have to 'pick' the item in order to unlock the safe and add the 'diamond' to your inventory")
                else:
                    self._inventory.append(item)
                    room['items'].remove(item)
                    print(f"You pick up the {item}.")
            else:
                print(f"There's no {item} anywhere.")

    def pick(self,item):
        room = self.map_data[self.current_room]
        if 'items' in room:
            if item != "diamond":
                print(f"You don't need to 'pick' {item} since it's not in a safe. You can simply 'get' it.")
            else:
                if item in room['items']:
                    print("\nYou'll need to answer riddles in order to unlock the safe (ONE-WORD-ANSWERS)")
                    answer1 = input("1) What's something that has a head and a tail, but no body (hint: think round objects)? ")
                    if answer1 == "coin":
                        print("\nThats the right answer! Next one is a little harder though")
                        answer2 = input("2) If you have me, you will want to share me. If you share me, you will no longer have me. What am I? ")
                        if answer2 == "secret":
                            print("\nCorrect again! Okay, this is it. FINAL riddle.")
                            answer3 = input("3) I follow you all the time and copy your every move, but you can't touch or catch me. What am I? ")
                            if answer3 == "shadow":
                                print("\nAlright! Alright! Here! You deserve it.")
                                self._inventory.append(item)
                                room['items'].remove(item)
                                print(f"You pick up the {item}.")
                            else:
                                print("Ohhhh! So close. Better luck next time.")
                        else:
                            print("Wrong! Better luck next time.")
                    else:
                        print(f"Really? {answer1}? You're not even trying.")
                else:
                    print(f"There's no {item} anywhere.")

    def drop(self, item):
        room = self.map_data[self.current_room]
        if 'items' not in room:
            room['items'] = []

        if item in self._inventory:
            self._inventory.remove(item)
            if 'items' in room:
                room['items'].append(item)
            else:
                room['items'] = [item]    
            print(f"You drop the {item}.")
        else:
            print(f"There's no {item} in your inventory.")
    
    def help(self):
        print("You can run the following commands:")
        for verb in self.verbs:
            if verb == "go":
                print("  go ...")
            elif verb == "get":
                print("  get ...")
            elif verb == "drop":
                print("  drop ...")
            elif verb == "pick":
                print("  pick ...")
            else:
                print(f"  {verb}")



    def quit(self):
        print("Goodbye!")
        sys.exit(0)

def main():
    #adventure run
    # print("hello")
    if len(sys.argv) != 2:
        print("Usage: python3 adventure.py [map filename]")
        sys.exit(1)
    
    map =  Adventure(sys.argv[1])
    map.look()

    while True:
        try:
            game_command = input("What would you like to do? ").strip().lower().split()
        except EOFError:
            print("\nUse 'quit' to exit.")
            continue
        except KeyboardInterrupt:
            print("Traceback (most recent call last):\n")
            print("  ...\n")
            print("KeyboardInterrupt")

        if not game_command:
            continue

        verb =  game_command[0]
        
        if verb == "go":
            if len(game_command) > 1:
                map.go(game_command[1])
            else:
                print("Sorry, you need to 'go' somewhere.")
        elif verb == "look":
            map.look()
        elif verb == "get":
            if len(game_command) > 1:
                map.get(game_command[1])
            else:
                print("Sorry, you need to 'get' something.")
        elif verb == "drop":
            if len(game_command) > 1:
                map.drop(game_command[1])
            else:
                print("Sorry, you need to 'drop' something.")
        elif verb == "pick":
            if len(game_command) > 1:
                map.pick(game_command[1])
            else:
                print("Sorry, you need to 'pick' something.")
        elif verb == "inventory":
            map.inventory()
        elif verb == "help":
            map.help()
        elif verb == "quit":
            map.quit()
        

if __name__ == '__main__':
    main()
