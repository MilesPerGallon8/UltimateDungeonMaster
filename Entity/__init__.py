import numpy as np
import random


class Entity:
    def __init__(self):
        self.MAX_HP = 10.0
        self.ARMOR = 0.0
        self.dmg = 1.0
        self.critChance = 10  # Critical hit chance (%)
        self.critDmg = 2  # This is a multiplier on damage
        # Dynamic health points
        # TODO: This may be able to be combined with MAX_HP to form a single HP stat: one
        #       initialize with a certain value and then changed per object
        self.hp = self.MAX_HP
        self.name = self.getType()

    """
    getType()
    Method to get the object class type
    Returns a string containing the class type
    """
    def getType(self):
        return type(self).__name__

    """
    setName()
    Sets entity's display name
    """
    def setName(self, newName):
        self.name = newName

    """
    getName()
    Returns entity's display name
    """
    def getName(self):
        return self.name

    """
    setPos()
    Sets entity's current position in x and y (x, y)
    """
    def setPos(self, pos):
        self.pos = pos

    """
    setPos()
    Returns entity's current position in x and y (x, y)
    """
    def getPos(self):
        return self.pos

    """
    attack()
    Returns the damage done by an attack (can be critical)
    """
    def attack(self):
        # 0.5 is added in to account for rounding a uniform distribution from a to b: a and b will have a lower chance
        # of draw b/c they only get drawn if, for example, the value is a + # where # < 0.5 (value cannot be lower than
        # a or greater than b
        # TODO: This method DOES NOT support any critical hit chance greater than 50%
        # critDraw = np.round(np.random.uniform(0.5, (100/self.critChance)+.5), 0)
        if random.randint(0, 100) < self.critChance:
            self.isCrit = True  # TODO: This might make more sense as an attribute of an attack class...
            self.dmg *= self.critDmg

        print(f'{self.getName()} attacked for {self.dmg} damage')
        return self.dmg

    """
    getHP()
    Returns the current hp of the entity
    """
    def getHP(self):
        return self.hp

    """
    setHP()
    Sets the current hp of the entity and returns the new hp attribute
    """
    def setHP(self, newHP):
        self.hp = newHP
        return self.hp

    """
    loseHP()
    Method for simulating an entity taking damage
    Decreases the current hp of the entity by the given amount and returns the new hp attribute
    """
    def loseHP(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    """
    isAlive()
    Method for checking if an entity is alive or not
    Returns true if the entity's current hp is greater than zero; returns false if entity's current hp is less than or
    equal to zero
    """
    def isAlive(self):
        return self.hp > 0

    """
    die()
    Causes the entity to die and calls the object destructor
    """
    def die(self):
        if self.hp == 0:  # This is a call check (makes sure entity is actually dead)
            print(f'{self.__name__} has died')
            # TODO: This should call the destructor