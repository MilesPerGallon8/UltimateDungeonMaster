from Entity import Entity


class Enemy(Entity):
    def __init__(self):
        super(Enemy, self).__init__()
        self.sightRange = 10