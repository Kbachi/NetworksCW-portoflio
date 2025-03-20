import random

# aloha
def simulate_slotted_aloha(n_nodes, p, n_slots):
    successes = 0
    for _ in range(n_slots):
        transmissions = 0
        for _ in range(n_nodes):
            if random.random() < p:
                transmissions += 1
        if transmissions == 1:
            successes += 1
    return successes / n_slots  # Efficiency calculation

# Simulation Parameters
n_nodes = 50  # Number of nodes
transmission_probs = [x / 20 for x in range(21)]  # Transmission probability values (0 to 1 in steps of 0.05)

# Run simulation and print results
efficiencies = []
for prob in transmission_probs:
    efficiencies.append(simulate_slotted_aloha(n_nodes, prob, 10000))
    print(f"Transmission Probability: {prob:.2f}, Efficiency: {efficiencies[-1]:.4f}")