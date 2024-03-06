import random
import math

#global variables and init values
machine_count = 2
time = 0
next_failure = 0
next_repair = float('inf')

repair_time = 2.5


def Failure():
  global machine_count, next_failure, next_repair, area_under_s, tlast
  area_under_s += machine_count * (time - tlast)
  tlast = time
  machine_count -= 1
  if machine_count == 1:
    next_repair = time + repair_time
    next_failure = time + math.ceil(6* random.random())
  else:
    next_failure = float('inf')




def Repair():
  global machine_count, next_failure, next_repair, area_under_s, tlast
  area_under_s += machine_count * (time - tlast)
  tlast = time
  machine_count += 1
  if machine_count == 1:
    next_repair = time + repair_time
    next_failure = time + math.ceil(6 * random.random())
  else:
    next_repair = float('inf')


#random seed

random.seed(5439)

#init values for simulation

time = 0
machine_count = 2
next_failure = math.ceil(6 * random.random())
next_repair = float('inf')

simulation_time = 30

tlast = 0
area_under_s = 0


#simulator
print("Clock", "\t" , "SS", "\t", "NF", "\t", "NR", "\t", "Area Under S")
print("_____________________________")
while (time < simulation_time and machine_count > 0):
  if time > 0:
    print(time, "\t" , machine_count, "\t", next_failure, "\t", next_repair, "\t", area_under_s/time)
  else:
    print(time, "\t" , machine_count, "\t", next_failure, "\t", next_repair)
  if next_failure < next_repair:
    time = next_failure
    Failure()
  else:
    time = next_repair
    Repair()
  if machine_count == 0:
    print(time, "\t" , machine_count, "\t", next_failure, "\t", next_repair, "\t", area_under_s/time)
    print("System failed at: ", time)
    break


