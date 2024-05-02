import unittest
import numpy as np
from src.algorithms.ppo import PPO

class TestPPO(unittest.TestCase):
    def test_ppo_initialization(self):
        state_dim = 10
        action_dim = 4
        hidden_dim = 64
        lr = 0.001
        gamma = 0.99
        clip_param = 0.2
        
        ppo = PPO(state_dim, action_dim, hidden_dim, lr, gamma, clip_param)
        
        self.assertEqual(ppo.actor[0].in_features, state_dim)
        self.assertEqual(ppo.actor[0].out_features, hidden_dim)
        self.assertEqual(ppo.actor[-1].out_features, action_dim)
        self.assertEqual(ppo.critic[0].in_features, state_dim)
        self.assertEqual(ppo.critic[-1].out_features, 1)
        self.assertEqual(ppo.gamma, gamma)
        self.assertEqual(ppo.clip_param, clip_param)
    
    def test_ppo_get_action(self):
        state_dim = 10
        action_dim = 4
        hidden_dim = 64
        lr = 0.001
        gamma = 0.99
        clip_param = 0.2
        
        ppo = PPO(state_dim, action_dim, hidden_dim, lr, gamma, clip_param)
        
        state = np.random.rand(state_dim)
        action = ppo.get_action(state)
        
        self.assertIsInstance(action, int)
        self.assertGreaterEqual(action, 0)
        self.assertLess(action, action_dim)

if __name__ == '__main__':
    unittest.main()