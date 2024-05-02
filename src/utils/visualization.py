import matplotlib.pyplot as plt

def visualize_simulation(simulation):
    plt.figure(figsize=(8, 8))
    plt.xlim(0, simulation.width)
    plt.ylim(0, simulation.height)
    
    for entity in simulation.entities:
        if isinstance(entity, Prey):
            plt.scatter(entity.position[0], entity.position[1], color='blue')
        elif isinstance(entity, Predator):
            plt.scatter(entity.position[0], entity.position[1], color='red')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Prey vs Predator Simulation')
    plt.show()