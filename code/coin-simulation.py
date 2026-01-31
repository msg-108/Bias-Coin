#import libraries
import random
import matplotlib.pyplot as plt

# Parameters 
while True:
    try:
        N = int(input("Total number of tosses: "))
        if N <= 0:
            raise ValueError
        break
    except ValueError:
        print("N must be a positive integer")

p = .5 # initial probability of heads
alpha = .05 #significance level
k = 5 # update interval
window = k # window size

# State variables
recent_outcomes = [] 
p_history = []

#Simulation loop
for i in range(N):
    random_number = random.random() # Generates a random float between 0.0 and 1.0

    if random_number <= p:
        outcome = 1 # heads
    else:
        outcome = 0 # tails

    recent_outcomes.append(outcome)
    
    if len(recent_outcomes) == window:
        head_count = recent_outcomes.count(1)
        tail_count = recent_outcomes.count(0)
        
        if head_count > tail_count:
            p = p + alpha
        elif head_count < tail_count:
            p = p - alpha
        else:
            pass

        p = min(max(p, 0), 1)

        p_history.append(p)
        recent_outcomes.clear()

# Plotting
plt.plot([k*i for i in range(len(p_history))], p_history)
plt.xlabel('Toss number')
plt.ylabel('Estimated probability of heads')
plt.title('Coin That Learns to Cheat')
plt.show()