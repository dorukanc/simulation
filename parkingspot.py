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

# avarage_service_time = 2 hours
avarage_service_time = 2

def create_departure(time):
    labmda_ast = 1/avarage_service_time
    next_departure_time = time + random.expovariate(labmda_ast)
    return next_departure_time
