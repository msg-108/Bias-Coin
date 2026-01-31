#import libraries
import random
import matplotlib.pyplot as plt

# Parameters 
while True:
    try:
        total_tosses = int(input("Total number of tosses: "))
        if total_tosses <= 0:
            raise ValueError
        break
    except ValueError:
        print("Total tosses must be a positive integer")

while True:
    try:
        true_bias = float(input("True bias (0.0 - 1.0): "))
        if true_bias < 0 or true_bias > 1:
            raise ValueError
        break
    except ValueError:
        print("True bias must be a number between 0.0 and 1.0")

head_prob = .5 # initial probability of heads
alpha = .05 #significance level
fraction = 0.05 
interval = min(max(round(total_tosses * fraction), 1), 100) # update interval
window = interval # window size

# State variables
recent_outcomes = [] 
prob_history = []

#Simulation loop
for i in range(total_tosses):
    random_number = random.random() # Generates a random float between 0.0 and 1.0

    if random_number <= true_bias:
        outcome = 1 # heads
    else:
        outcome = 0 # tails

    recent_outcomes.append(outcome)
    
    if len(recent_outcomes) == window:
        head_count = recent_outcomes.count(1)
        tail_count = recent_outcomes.count(0)
        
        avg_heads = head_count / window
        head_prob += alpha * (avg_heads - head_prob)

        prob_history.append(head_prob)
        recent_outcomes.clear()

# Plotting
plt.plot([interval*i for i in range(len(prob_history))], prob_history)
plt.xlabel('Toss number')
plt.ylabel('Estimated probability of heads')
plt.title('Coin That Learns to Cheat')
plt.show()