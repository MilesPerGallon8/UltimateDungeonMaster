from Items.Equipment.equipment import Equipment
import scipy as sp
import numpy as np


class Weapon(Equipment):
    def getDmg(self):
        return np.round(sp.stats.truncnorm(self.avgDmg, self.stdDmg), 0)

    avgDmg = 0
    stdDmg = 0