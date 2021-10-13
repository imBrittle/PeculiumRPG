#AstrusRPG
import random
import time

print("==================")
print("==  WELCOME TO  ==")
print("==    ASTRUS    ==")
print("== Version  1.0 ==")
print("==================")
print()

time.sleep(2)

username = input("Enter your username: ")
print("Your username has been set to: " + username)
print()
character = input("Choose your element (Pyro, Capacita, Atmos, Hydro): ")
print("Your element has been set to: " + character)
print()

print("Applying Settings...")

time.perf_counter()
#Game Lists
pyroSpells = ["Burn"]
capacitaSpells = ["Shock"]
atmosSpells = ["Gale"]
hydroSpells = ["Splash"]
items = ["Healing Potion", "Arcane Crystal"]

#Character Settings
hp = 100
maxHp = 100
energy = 100
maxEnergy = 100
mana = 100
maxMana = 100
inventory = []
exploreCount = 0
sleepCount = 0

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
                    print("- Use")
                    print("- Discard")
                    print("- Cancel")
                    print()
                    bagSubDecision = input(">>> ")
                    if bagSubDecision == ["Use", "use"]:
                        print()
                        #-- Conditions for item use

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

        elif actionDecision in ["3", "Change Spells", "Change spells", "change spells", "Spells", "spells"]:
            print()

        elif actionDecision in ["4", "Check Stats", "Checks Stats", "check stats", "Stats", "stats"]:
            print()

        elif actionDecision in ["5", "Sleep", "sleep"]:
            print()
            print("Sleeping...")
            time.sleep(3)
            print()
            if sleepCount == 0:
                print("I close my eyes and think about this intriguing place. I'm not sure how I got here, but I'm going to make the most of it and do whatever I can to get out. I ponder on the idea of improving my spells, and I think I may've experienced a breakthrough. The Arcane Stone that I found when I arrived has provided me with some basic information as to how spells work, and I may be able to put it to use to improve my spells.")
                inventory.append("Arcane Crystal")

                hp = maxHp
                energy = maxEnergy
                mana = maxMana

                time.sleep(10)
                print()
            else:
                hp = maxHp
                energy = maxEnergy
                mana = maxMana

                time.sleep(10)
                print()
        else:
            print("Action not recognised.")
            print()
            time.sleep(1)
