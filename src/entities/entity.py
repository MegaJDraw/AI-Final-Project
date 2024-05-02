import numpy as np

class Entity:
    def __init__(self, position, health, reproduction_rate):
        self.position = position
        self.health = health
        self.reproduction_rate = reproduction_rate
        
    def move(self, direction):
        self.position += direction
        
    def reproduce(self):
        if np.random.rand() < self.reproduction_rate:
            # Create a new entity with the same attributes
            return self.__class__(self.position, self.health, self.reproduction_rate)
        return None