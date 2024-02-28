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

#init values for simulation controller
system_state = 0 #number of cars in the system
clock = 0
fel_arrivals = [0] #future event list arrivals
fel_departures = [] #future event list departure

while clock <= 24:
    next_arrival_time = min(fel_arrivals)
    if (len(fel_departures) > 0):
        next_departure_time = min(fel_departures)
    else:
        next_departure_time = float('inf')

    if next_departure_time < next_arrival_time:
        #departure event tbd
        clock = next_departure_time #advance to clock to earliest
        system_state -= 1
        print("Car departs at: ", clock)
        fel_departures.remove(next_departure_time)

    else: 
        #arrival event
        clock = next_arrival_time
        system_state += 1 #increased the numbers of cars in the system
        print("Car arrives at: ", clock)
        fel_arrivals.remove(next_arrival_time)

        #departure time of the current car
        departure_time = create_departure(clock)
        fel_departures.append(departure_time)

        # arrival time of next car

        arrival_time = create_arrival(clock)
        fel_arrivals.append(arrival_time) #appended the arrival time to the list