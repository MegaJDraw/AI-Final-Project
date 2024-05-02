from .entity import Entity

class Predator(Entity):
    def __init__(self, position, health=200, reproduction_rate=0.05):
        super().__init__(position, health, reproduction_rate)
        
    def update(self, simulation):
        # Move towards the nearest prey
        nearest_prey = simulation.get_nearest_prey(self.position)
        if nearest_prey is not None:
            direction = np.sign(nearest_prey.position - self.position)
            self.move(direction)
            
            # Attack the prey
            if np.linalg.norm(self.position - nearest_prey.position) < 1:
                nearest_prey.health -= 50
                if nearest_prey.health <= 0:
                    simulation.remove_entity(nearest_prey)
                    self.health += 100
        
        # Reproduce
        offspring = self.reproduce()
        if offspring is not None:
            simulation.add_entity(offspring)