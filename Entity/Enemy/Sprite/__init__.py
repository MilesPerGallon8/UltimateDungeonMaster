from Entity.Enemy import Enemy
import numpy as np


class Sprite(Enemy):
    MAX_HP = 5
    ARMOR = 0
    dmg = np.round(np.random.uniform(0.5, 2.5), 0)

    def __init__(self):
        super().__init__()