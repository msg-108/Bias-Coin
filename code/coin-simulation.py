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

head_prob = .5 # initial probability of heads
alpha = .05 #significance level
epsilon = 0.01 # prevents probability = 0 or 1
fraction = 0.05 
interval = min(max(round(total_tosses * fraction), 1), 100) # update interval
window = interval # window size

# State variables
recent_outcomes = [] 
prob_history = []

#Simulation loop
for i in range(total_tosses):
    random_number = random.random() # Generates a random float between 0.0 and 1.0

    if random_number <= head_prob:
        outcome = 1 # heads
    else:
        outcome = 0 # tails

    recent_outcomes.append(outcome)
    
    if len(recent_outcomes) == window:
        head_count = recent_outcomes.count(1)
        tail_count = recent_outcomes.count(0)
        
        if head_count > tail_count:
            head_prob = head_prob + alpha
        elif head_count < tail_count:
            head_prob = head_prob - alpha
        else:
            pass

        head_prob = min(max(head_prob, epsilon), 1 - epsilon) #prevents absorbing state

        prob_history.append(head_prob)
        recent_outcomes.clear()

# Plotting
plt.plot([interval*i for i in range(len(prob_history))], prob_history)
plt.xlabel('Toss number')
plt.ylabel('Estimated probability of heads')
plt.title('Coin That Learns to Cheat')
plt.show()