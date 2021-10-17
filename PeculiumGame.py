# Peculium RPG Game
import random
import time
import pickle
from Classes import itemArcaneCrystal, itemHealingStone, spellBurn, spellShock, spellGale, spellSplash, spellDev

print("==================")
print("==  WELCOME TO  ==")
print("==   PECULIUM   ==")
print("== Version  1.0 ==")
print("==================")
print()

print("1) Start New Game")
print("2) Load Existing Game")
print()
gameType = input(">>> ")
print()

gameTypeLoop = True
while gameTypeLoop == True:
    if gameType in ["1", "Start New Game"]:
        print()
        print("Are you sure? (Yes/No)")
        print("WARNING: Starting a new game will overwrite the previous save")
        print()
        gameTypeChoice = input(">>> ")
        if gameTypeChoice in ["Yes", "yes"]:
            print()
            print("Generating new game...")
            print()
            gameTypeLoop = False
        elif gameTypeChoice in ["No"]:
            gameTypeChoice = None
            print()
        else:
            print()
            print(f"'{gameTypeChoice}' not recognised.")
            print()
    elif gameType in ["2", "Load Existing Game"]:
        print()
        print("Loading...")
        with open('save.pkl', 'rb') as saveFile:
            save = pickle.load(saveFile)
            print(save)
        print()
        gameTypeLoop = False
    else:
        print(f"'{gameType}' not recognised")

username = input("Enter your username: ")
print("Your username has been set to: " + username)
print()
chooseElement = True
while chooseElement == True:
    character = input("Choose your element (Pyro, Capacita, Atmos, Hydro): ")
    if character in ["Pyro", "pyro", "Capacita", "capacita", "Atmos", "atmos", "Hydro", "hydro"]:
        print("Your element has been set to: " + character)
        chooseElement = False
    elif character in ["Dev", "dev", "Developer", "developer"]:
        print("Developer mode has been enabled.")
        chooseElement = False
    else:
        print("Element not recognised. Please select an existing element.")
        print()

print()
print("Loading...")
time.perf_counter()

#Game Lists
pyroSpells = ["Burn"]
capacitaSpells = ["Shock"]
atmosSpells = ["Gale"]
hydroSpells = ["Splash"]
otherSpells = ["Dev"]
items = [itemArcaneCrystal(), itemHealingStone()]

if gameType in ["1", "Start New Game"]:
    #Character Settings
    hp = 100
    maxHp = 100
    energy = 100
    maxEnergy = 100
    mana = 100
    maxMana = 100
    inventory = []
    scroll = []
    exploreCount = 0
    sleepCount = 0
else:
    None

if character in ["Pyro", "pyro"]:
    scroll.append("Burn")
elif character in ["Capacita", "capacita"]:
    scroll.append("Shock")
elif character in ["Atmos", "atmos"]:
    scroll.append("Gale")
elif character in ["Hydro", "hydro"]:
    scroll.append("Hydro")
else:
    scroll.append("Dev")
        

time.perf_counter()
print(f"Done! Loading took {time.perf_counter()} nanoseconds.")
print()
time.sleep(2)

print("Story Placeholder")

print()
time.sleep(2)

ingame = True
while ingame == True:
    decision = True
    while decision == True:
        print("Choose your next action:")
        print("1) Explore")
        print("2) Open Bag")
        print("3) Change Spells")
        print("4) Check Stats")
        print("5) Sleep")
        print()
        print("'Exit' to Save and Exit")
        print()
        actionDecision = input(">>> ")

        if actionDecision in ["1", "Explore", "explore"]:
            print()
        elif actionDecision in ["2", "Open Bag", "Open bag", "open bag", "Bag", "bag"]:
            print()
            inventoryCount = len(inventory)
            if inventoryCount == 1:
                print(f"You have {inventoryCount} item in your bag:")
                for x in inventory:
                    print(f"- {x}")
                print()
                bagDecision = input(">>> ")
                if bagDecision in inventory:
                    print()
                    print(f"{bagDecision}:")
                    print()
                    print("1) Use")
                    print("2) Discard")
                    print("3) Cancel")
                    print()
                    bagSubDecision = input(">>> ")
                    if bagSubDecision in ["1", "Use", "use"]:
                        print()
                        inventory[0].use()
                        inventory.remove(bagDecision)
                    elif bagSubDecision in ["2", "Discard", "discard", "Delete", "delete", "Remove", "remove"]:
                        print()
                    elif bagSubDecision in ["3", "Cancel", "cancel"]:
                        print()
                    else:
                        print(f"'{actionDecision}' not recognised.")
                    print()

            elif inventoryCount > 1:
                print(f"You have {inventoryCount} items in your bag:")
                for x in inventory:
                    print(f"- {x}")
                print()
                bagDecision = input(">>> ")
                if bagDecision in inventory:
                    print()
                    print(f"{bagDecision}:")
                    print()
                    print("- Use")
                    print("- Discard")
                    print("- Cancel")
            else:
                print("You have no items in your bag")
                print()
                time.sleep(1)

        elif actionDecision in ["3", "Change Spells", "Change spells", "change spells", "Spells", "spells"]:
            print()
            

        elif actionDecision in ["4", "Check Stats", "Checks Stats", "check stats", "Stats", "stats"]:
            print()
            print("Stats:")
            print(f"HP: {hp}/{maxHp}")
            print(f"Energy: {energy}/{maxEnergy}")
            print(f"Mana: {mana}/{maxMana}")
            print()
            input("Press 'Enter' to continue ")
 
        elif actionDecision in ["5", "Sleep", "sleep"]:
            print()
            print("Sleeping...")
            time.sleep(3)
            print()
            if sleepCount == 0:
                print("I close my eyes and think about this intriguing place. I'm not sure how I got here, but I'm going to make the most of it and do whatever I can to get out. I ponder on the idea of improving my spells, and I think I may've experienced a breakthrough. The Arcane Stone that I found when I arrived has provided me with some basic information as to how spells work, and I may be able to put it to use to improve my spells.")
                inventory.append("Arcane Crystal")
                print()
                print("Received 1x Arcane Crystal")

                hp = maxHp
                energy = maxEnergy
                mana = maxMana
                sleepCount = sleepCount + 1

                time.sleep(10)
                print()
            else:
                hp = maxHp
                energy = maxEnergy
                mana = maxMana
                sleepCount = sleepCount + 1

                time.sleep(10)
                print()
        elif actionDecision in ["Exit", "exit"]:
            print()
            print("Saving game...")

            save = [hp, maxHp, energy, maxEnergy, mana, maxMana, inventory, inventoryCount, scroll, exploreCount, sleepCount]
            with open('save.pkl', 'wb') as saveFile:
                pickle.dump(save, saveFile)

            time.sleep(1)
            print("Exiting game...")
            time.sleep(2)
            exit()
        else:
            print()
            print(f"'{actionDecision}' not recognised.")
            print()
            time.sleep(1)
