class EntityRegister:
    def __init__(self):
        self.cnt = 0
        self.registry = []
        # Note: player(s) will be added to the registry first and will not be removed (unless in multiplier mode and a
        # player leaves or joins)

    def registerEntity(self, entity):
        # If the entity's info is updated outside of this registry array, will the registry be "out of date"? This may
        # not be an issue though if the registry's only purpose is to keep track of what entities exist and how many
        # there are...
        self.registry[self.cnt] = entity
        self.cnt += 1
        return self.cnt - 1  # Returns the index for THIS entity and should be saved in the entity.idx attribute

    def removeEntity(self, entity):
        self.registry[entity.idx] = []  # Does this clear the entree at that index?
        self.registry[entity.idx:-2] = self.registry[entity.idx+1:-1]  # Shift entrees back to fill in space
        # TODO: Account for special case like when the entity being removed is the last entree or there are onlt 2
        #       entities in existence

    def getRegistry(self):
        return self.registry