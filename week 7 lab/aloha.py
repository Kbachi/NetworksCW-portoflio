import random

# Simulate Slotted ALOHA Protocol
def simulate_slotted_aloha(n_nodes, p, n_slots):
    successes = 0
    for _ in range(n_slots):
        transmissions = sum(1 for _ in range(n_nodes) if random.random() < p)
        if transmissions == 1:
            successes += 1
    return successes / n_slots  # Efficiency calculation

# Simulation Parameters
n_nodes = 50  # Number of nodes
transmission_probs = [i / 20 for i in range(21)]  # Transmission probability values (0 to 1 in steps of 0.05)

# Run simulation and print results
efficiencies = []
for p in transmission_probs:
    efficiency = simulate_slotted_aloha(n_nodes, p, 10000)
    efficiencies.append(efficiency)
    print(f"Transmission Probability: {p:.2f}, Efficiency: {efficiency:.4f}")