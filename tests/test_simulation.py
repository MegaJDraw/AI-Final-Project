import unittest
from src.environment.simulation import Simulation
from src.entities.prey import Prey
from src.entities.predator import Predator

class TestSimulation(unittest.TestCase):
    def test_simulation_initialization(self):
        width = 100
        height = 100
        num_prey = 50
        num_predators = 10
        
        simulation = Simulation(width, height, num_prey, num_predators)
        
        self.assertEqual(simulation.width, width)
        self.assertEqual(simulation.height, height)
        self.assertEqual(len(simulation.entities), num_prey + num_predators)
        self.assertEqual(sum(isinstance(entity, Prey) for entity in simulation.entities), num_prey)
        self.assertEqual(sum(isinstance(entity, Predator) for entity in simulation.entities), num_predators)
    
    def test_simulation_get_nearest_prey(self):
        simulation = Simulation(width=100, height=100, num_prey=5, num_predators=1)
        
        predator = simulation.entities[-1]
        nearest_prey = simulation.get_nearest_prey(predator.position)
        
        self.assertIsInstance(nearest_prey, Prey)
        
        min_distance = float('inf')
        for entity in simulation.entities:
            if isinstance(entity, Prey):
                distance = np.linalg.norm(entity.position - predator.position)
                if distance < min_distance:
                    min_distance = distance
                    expected_nearest_prey = entity
        
        self.assertEqual(nearest_prey, expected_nearest_prey)
    
    def test_simulation_update(self):
        simulation = Simulation(width=100, height=100, num_prey=5, num_predators=1)
        
        initial_num_entities = len(simulation.entities)
        
        simulation.update()
        
        self.assertNotEqual(len(simulation.entities), initial_num_entities)
        
        for entity in simulation.entities:
            self.assertGreater(entity.health, 0)
    
    def test_simulation_get_state(self):
        simulation = Simulation(width=100, height=100, num_prey=5, num_predators=1)
        
        state = simulation.get_state()
        
        self.assertEqual(state.shape, (len(simulation.entities), 2))
        
        for entity_state, entity in zip(state, simulation.entities):
            self.assertTrue(np.array_equal(entity_state, entity.position))
    
    def test_simulation_get_reward(self):
        simulation = Simulation(width=100, height=100, num_prey=5, num_predators=1)
        
        reward = simulation.get_reward()
        
        expected_reward = len([entity for entity in simulation.entities if isinstance(entity, Prey)]) - \
                          len([entity for entity in simulation.entities if isinstance(entity, Predator)])
        
        self.assertEqual(reward, expected_reward)

if __name__ == '__main__':
    unittest.main()