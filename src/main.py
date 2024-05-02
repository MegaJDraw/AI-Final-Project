from .environment.simulation import Simulation
from .algorithms.ppo import PPO
from .utils.visualization import visualize_simulation
from .utils.analysis import analyze_performance, analyze_best_genes

def train_agents(num_episodes, num_steps):
    simulation = Simulation(width=100, height=100, num_prey=50, num_predators=10)
    state_dim = simulation.get_state().shape[0]
    action_dim = 4  # Assuming 4 possible actions (up, down, left, right)
    hidden_dim = 64
    lr = 0.001
    gamma = 0.99
    clip_param = 0.2
    
    prey_agent = PPO(state_dim, action_dim, hidden_dim, lr, gamma, clip_param)
    predator_agent = PPO(state_dim, action_dim, hidden_dim, lr, gamma, clip_param)
    
    performance_metrics = []
    best_genes = []
    
    for episode in range(num_episodes):
        state = simulation.get_state()
        episode_reward = 0
        
        for step in range(num_steps):
            # Prey agent's action
            prey_action = prey_agent.get_action(state)
            
            # Predator agent's action
            predator_action = predator_agent.get_action(state)
            
            # Update simulation
            simulation.update()
            
            next_state = simulation.get_state()
            reward = simulation.get_reward()
            done = (step == num_steps - 1)
            
            # Update agents
            prey_agent.update(state, prey_action, reward, next_state, done)
            predator_agent.update(state, predator_action, -reward, next_state, done)
            
            state = next_state
            episode_reward += reward
        
        performance_metrics.append(episode_reward)
        best_genes.append((prey_agent.actor.state_dict(), predator_agent.actor.state_dict()))
        
        print(f"Episode {episode+1}/{num_episodes}, Reward: {episode_reward:.2f}")
    
    return performance_metrics, best_genes

def main():
    num_episodes = 100
    num_steps = 1000
    
    performance_metrics, best_genes = train_agents(num_episodes, num_steps)
    
    # Visualize the simulation
    simulation = Simulation(width=100, height=100, num_prey=50, num_predators=10)
    visualize_simulation(simulation)
    
    # Analyze performance metrics
    analyze_performance(performance_metrics)
    
    # Analyze best genes
    analyze_best_genes(best_genes)

if __name__ == "__main__":
    main()