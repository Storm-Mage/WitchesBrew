waterlily = 5
rosepetal = 5
gingerroot = 5
ingredlist = {"water lily":1,"rose petal":3,"ginger root":5}
potionlist = {9:"Herbal Medicine"}

# Start of story
print("You are a novice Witch, who is going to start her own shop.")
print("You find an abandoned cottage, which you decided to turn into a shop.")
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
    print("You heat the potion, stir it, then wait for the results.)
          
