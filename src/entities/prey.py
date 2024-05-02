from .entity import Entity

class Prey(Entity):
    def __init__(self, position, health=100, reproduction_rate=0.1):
        super().__init__(position, health, reproduction_rate)
        
    def update(self, simulation):
        # Move randomly
        direction = np.random.randint(-1, 2, size=2)
        self.move(direction)
        
        # Reproduce
        offspring = self.reproduce()
        if offspring is not None:
            simulation.add_entity(offspring)