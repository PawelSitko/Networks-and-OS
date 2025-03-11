import random
import matplotlib.pyplot as plt
import numpy as np

# Slotted ALOHA Simulation
def simulate_slotted_aloha(n_nodes, p, n_slots):
    successes = 0
    for _ in range(n_slots):
        # Each node transmits with probability p in a slot
        transmissions = sum(1 for _ in range(n_nodes) if random.random() < p)
        if transmissions == 1:  # Successful if only one node transmits
            successes += 1
    efficiency = successes / n_slots
    return efficiency

# Pure ALOHA Simulation
def simulate_pure_aloha(n_nodes, p, n_slots):
    successes = 0
    transmissions = []
    
    for t in range(n_slots):
        # Each node transmits with probability p
        new_transmissions = [t for _ in range(n_nodes) if random.random() < p]
        transmissions.extend(new_transmissions)
        
        # A successful transmission happens if only one node transmits in a window of 2 slots
        if len(new_transmissions) == 1:
            if all(abs(new_transmissions[0] - prev) > 1 for prev in transmissions[:-1]):
                successes += 1
    
    efficiency = successes / n_slots
    return efficiency

# CSMA/CD Simulation
def simulate_csma_cd(n_nodes, p, n_slots):
    successes = 0
    busy_until = 0  # Time until the channel is busy

    for t in range(n_slots):
        # Nodes that want to transmit
        contenders = [i for i in range(n_nodes) if random.random() < p]
        
        if contenders:
            first_transmitter = contenders[0]
            
            if t >= busy_until:  # If the channel is free
                if len(contenders) == 1:  # Successful transmission if only one node transmits
                    successes += 1
                busy_until = t + 1  # Mark the channel busy for the duration of the transmission

    efficiency = successes / n_slots
    return efficiency

# Simulation Parameters
n_nodes = 50
n_slots = 10000
ps = np.linspace(0, 1, 50)  # Transmission probability range

# Running the simulations
slotted_aloha_efficiencies = [simulate_slotted_aloha(n_nodes, p, n_slots) for p in ps]
pure_aloha_efficiencies = [simulate_pure_aloha(n_nodes, p, n_slots) for p in ps]
csma_cd_efficiencies = [simulate_csma_cd(n_nodes, p, n_slots) for p in ps]

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(ps, slotted_aloha_efficiencies, marker='o', linestyle='-', label='Slotted ALOHA')
plt.plot(ps, pure_aloha_efficiencies, marker='s', linestyle='--', label='Pure ALOHA')
plt.plot(ps, csma_cd_efficiencies, marker='^', linestyle='-.', label='CSMA/CD')

plt.xlabel('Transmission Probability')
plt.ylabel('Efficiency')
plt.title('Comparison of Multiple Access Protocols')
plt.legend()
plt.grid(True)
plt.show()
