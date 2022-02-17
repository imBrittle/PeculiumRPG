# Creatures

class creaturePassive:
    class winder:
        name = "winder"
        display = "Winder"
        element = "Gale"
        hp = 10
        damage = 5
        level = 1
    class finder:
        name = "finder"
        display = "Finder"
        element = None
        hp = 10
        damage = 5
        level = 1

class creatureNeutral:
    class dragonSpider:
        name = "dragon_spider"
        display = "Dragon Spider"
        element = "Pyro"
        hp = 30
        damage = 10
        level = 1
    class suspiciousFlower:
        name = "suspicious_flower"
        display = "Suspicious Flower"
        element = None
        hp = 10
        damage = 5
        level = 1

class creatureAggressive:
    class swarmer:
        name = "swarmer"
        display = "Swarmer"
        element = None
        hp = 50
        damage = 25
        level = 1
    class hellhound:
        name = "hellhound"
        display = "Hellhound"
        element = "Pyro"
        hp = 80
        damage = 30
        level = 1


# Attacks
class attack:
    class wind:
        damage = 5