import unittest
from src.entities.entity import Entity
from src.entities.prey import Prey
from src.entities.predator import Predator

class TestEntities(unittest.TestCase):
    def test_entity_initialization(self):
        entity = Entity(position=[0, 0], health=100, reproduction_rate=0.1)
        self.assertEqual(entity.position.tolist(), [0, 0])
        self.assertEqual(entity.health, 100)
        self.assertEqual(entity.reproduction_rate, 0.1)
    
    def test_prey_initialization(self):
        prey = Prey(position=[10, 20])
        self.assertEqual(prey.position.tolist(), [10, 20])
        self.assertEqual(prey.health, 100)
        self.assertEqual(prey.reproduction_rate, 0.1)
    
    def test_predator_initialization(self):
        predator = Predator(position=[30, 40])
        self.assertEqual(predator.position.tolist(), [30, 40])
        self.assertEqual(predator.health, 200)
        self.assertEqual(predator.reproduction_rate, 0.05)

if __name__ == '__main__':
    unittest.main()