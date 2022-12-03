waterlily = 5
rosepetal = 5
gingerroot = 5
ingredlist = {"water lily":1,"rose petal":3,"ginger root":5}
potionlist = {9:"Herbal Medicine"}
mapplaces = ["Thornwood"]
inventory = []

def idenpotion(p):
    for key,value in potionlist.items():
        if p == key:
            return value
    return "Rainbow Sludge"

# Start of story
print("You are a novice Witch, who is going to start her own shop.")
print("You find an abandoned` cottage, which you decided to turn into a shop.")
print("You find a cauldron and some notes off recipies.")
print("You are now going to start your journey.")

answer = input("What would you like to do? ").lower()
if answer == "potion":
    print("You move to the cauldron, you then add the water. (Type done when you want to exit)")
    potion = 0
    ingred = ""
    while ingred != "done":
        ingred = input("What else would you like to add?\n")
        if ingred in ingredlist:
            potion += ingredlist[ingred]
        elif ingred != "done":
            print("You do not have that ingredient.")
        print(potion)
    if potion != 0:
        print("You heat the potion, stir it, then wait for the results.")
        print(idenpotion(potion))
        inventory.append(idenpotion(potion))
    else:
        print("You decide not to brew and leave.")
if answer == "adventure":
    print("You decide to go on an adventure, you pull out your map and look where you want to go.")
    print("You can goto:")
    for plce in mapplaces:
        print(plce)
    print("Where would you like to go?")
    answer = input()
    if answer == "Thornwood":
        print("What potion would you like to bring? You can bring:")
        if len(inventory) == 0:
            print("Nothing")
        else:
            for item in inventory:
                print(item)
        answer = input()
        if answer = "back":
            return ""
        elif answer == "Herbal Medicine" and answer in inventory:
            print("You enter the thornwood forest, use your potion, and return unharmed")
            inventory.remove(answer)
        elif answer not in inventory:
            print("You do not have this potion!")
        else:
            print("You venture into the forest, but you were not equiped to handle it. You manage to escape relatively unharmed, but without your potion.")
            inventory.remove(answer)