

# Parameters 
N = input ("Total number of tosses: ")
p = .5 # initial probability of heads
alpha = .05 #significance level
k = 5 # update interval

# State variables
recent_outcomes = [] 
head_count = 0
tail_count = 0
p_history = []