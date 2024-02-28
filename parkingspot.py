import math
import random

#event generator
#system state
# simulation controller

#λ(t) = 100 +10 sin(πt/12)


def create_arrival(time):
    #sin function between -1 and 1, so we would get smooth fluctuation 
    lambda_t = 100 + 10 * math.sin(math.pi * time / 12)

    #poisson exponential 
    
    next_arrival_time = time + random.expovariate(lambda_t)
    return next_arrival_time
