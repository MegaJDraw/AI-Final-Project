import numpy as np
from ..entities.prey import Prey
from ..entities.predator import Predator

class Simulation:
    def __init__(self, width, height, num_prey, num_predators):
        self.width = width
        self.height = height
        self.entities = []
        
        # Initialize prey and predators
        for _ in range(num_prey):
            position = np.random.randint(0, self.width, size=2)
            self.entities.append(Prey(position))
        
        for _ in range(num_predators):
            position = np.random.randint(0, self.width, size=2)
            self.entities.append(Predator(position))
    
    def add_entity(self, entity):
        self.entities.append(entity)
    
    def remove_entity(self, entity):
        self.entities.remove(entity)
    
    def get_nearest_prey(self, position):
        nearest_prey = None
        min_distance = float('inf')
        for entity in self.entities:
            if isinstance(entity, Prey):
                distance = np.linalg.norm(entity.position - position)
                if distance < min_distance:
                    min_distance = distance
                    nearest_prey = entity
        return nearest_prey
    
    def update(self):
        for entity in self.entities:
            entity.update(self)
        
        # Remove dead entities
        self.entities = [entity for entity in self.entities if entity.health > 0]
    
    def get_state(self):
        # Return the state of the simulation (e.g., positions of entities)
        state = []
        for entity in self.entities:
            state.append(entity.position)
        return np.array(state)
    
    def get_reward(self):
        # Calculate the reward based on the simulation state
        num_prey = sum(isinstance(entity, Prey) for entity in self.entities)
        num_predators = sum(isinstance(entity, Predator) for entity in self.entities)
        reward = num_prey - num_predators
        return reward