import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import Categorical

class PPO:
    def __init__(self, state_dim, action_dim, hidden_dim, lr, gamma, clip_param):
        self.actor = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, action_dim),
            nn.Softmax(dim=-1)
        )
        self.critic = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1)
        )
        self.optimizer = optim.Adam(list(self.actor.parameters()) + list(self.critic.parameters()), lr=lr)
        self.gamma = gamma
        self.clip_param = clip_param
        
    def get_action(self, state):
        state = torch.from_numpy(state).float()
        action_probs = self.actor(state)
        dist = Categorical(action_probs)
        action = dist.sample()
        return action.item()
    
    def update(self, states, actions, rewards, next_states, dones):
        states = torch.tensor(states, dtype=torch.float)
        actions = torch.tensor(actions, dtype=torch.long)
        rewards = torch.tensor(rewards, dtype=torch.float)
        next_states = torch.tensor(next_states, dtype=torch.float)
        dones = torch.tensor(dones, dtype=torch.float)
        
        # Calculate advantages
        with torch.no_grad():
            values = self.critic(states)
            next_values = self.critic(next_states)
            advantages = rewards + self.gamma * next_values * (1 - dones) - values
        
        # Calculate policy loss
        old_action_probs = self.actor(states).gather(1, actions.unsqueeze(1)).squeeze()
        new_action_probs = self.actor(states).gather(1, actions.unsqueeze(1)).squeeze()
        ratio = new_action_probs / old_action_probs
        surr1 = ratio * advantages
        surr2 = torch.clamp(ratio, 1 - self.clip_param, 1 + self.clip_param) * advantages
        policy_loss = -torch.min(surr1, surr2).mean()
        
        # Calculate value loss
        value_loss = nn.MSELoss()(self.critic(states), rewards + self.gamma * next_values * (1 - dones))
        
        # Update actor and critic
        self.optimizer.zero_grad()
        (policy_loss + value_loss).backward()
        self.optimizer.step()