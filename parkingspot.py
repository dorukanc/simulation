import math
import random
import pandas as pd
import simpy

#created a empty data frame
df = pd.DataFrame() 
df['time'] = 0 # column names init
df['System State'] = 0 #column names init

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

while clock <= 120:
    next_arrival_time = min(fel_arrivals)
    if (len(fel_departures) > 0):
        next_departure_time = min(fel_departures)
    else:
        next_departure_time = float('inf')

    if next_departure_time < next_arrival_time:
        #departure event tbd
        clock = next_departure_time #advance to clock to earliest
        system_state -= 1
        #print("Car departs at: ", clock, " SS: ", system_state)
        df.loc[len(df.index)] = [clock, system_state]
        fel_departures.remove(next_departure_time)

    else: 
        #arrival event
        clock = next_arrival_time
        system_state += 1 #increased the numbers of cars in the system
        #print("Car arrives at: ", clock, " SS: ", system_state)
        df.loc[len(df.index)] = [clock, system_state]
        fel_arrivals.remove(next_arrival_time)

        #departure time of the current car
        departure_time = create_departure(clock)
        fel_departures.append(departure_time)

        # arrival time of next car

        arrival_time = create_arrival(clock)
        fel_arrivals.append(arrival_time) #appended the arrival time to the list

# @title time vs System State

from matplotlib import pyplot as plt
df.plot(kind='scatter', x='time', y='System State', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

#create a enviroment

env = simpy.Environment()

system_state = 0
def add_car(env, id):
    global system_state
    #enter the parking lot
    print("Car ", id, "arrives at time: ", env.now)
    system_state += 1
    #wait for some time
    yield env.timeout(random.expovariate(1/avarage_service_time))
    #leave the parking lot
    system_state -= 1
    print("Car ", id, "departs at time: ", env.now)

def car_generator(env):
    id = 0
    while 1:
        id += 1
        # generate a new car, and everytime line runs, it adds new car to the system
        env.process(add_car(env, id))
        lambda_t = 100 + 10 * math.sin(math.pi * env.now / 12)
        yield env.timeout(random.expovariate(lambda_t))

env.process(car_generator(env))
env.run(until = 24)