from Entity import Entity


class Player(Entity):
    def __init__(self):
        self.MAX_HP = 10.0  # Does this overwrite the super attribute?
        self.ARMOR = 0.0
        self.hp = self.MAX_HP
        self.name = 'Player'

    # Sets the player's damage stat
    def equipWeapon(self, weapon):
        self.dmg = weapon.getDmg()

    def addMaxHP(self, hp):
        self.MAX_HP += hp

    def addArmor(self, armor):
        self.ARMOR = armor