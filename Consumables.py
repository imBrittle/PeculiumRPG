# Classes

# Spells
class spellBurn:
    name = "burn"
    display = "Burn"
    element = "Pyro"
    damage = 10
    mana = 5
    level = 1
    maxLevel = 5
    def __init__(self):
        pass

class spellShock:
    name = "shock"
    display = "Shock"
    element = "Capacita"
    damage = 10
    mana = 5
    level = 1
    maxLevel = 5

class spellGale:
    name = "gale"
    display = "Gale"
    element = "Atmos"
    damage = 10
    mana = 5
    level = 1
    maxLevel = 5

class spellSplash:
    name = "splash"
    display = "Splash"
    element = "Hydro"
    damage = 10
    mana = 5
    level = 1
    maxLevel = 5
    
class spellDev:
    name = "dev"
    display = "Developer"
    element = "Dev"
    damage = 500
    mana = 1
    level = 1
    maxLevel = 10

# Items
class itemArcaneCrystal:
    name = "arcanecrystal"
    display = "Arcane Crystal"
    mana = 100
    spellPoints = 1
    stack = 0
    maxStack = 1
    def __init__(self) -> None:
        

        
        self.stack - 1
    def use(self):
        pass

class itemHealingStone:
    name = "healingstone"
    display = "Healing Stone"
    mana = 10
    healing = 20
    stack = 0
    maxStack = 10