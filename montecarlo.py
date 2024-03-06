import random

interval = 1000
circle_points = 0
square_points = 0


for i in range(interval):
    
    rnd_x = random.uniform(-1,1)
    rnd_y = random.uniform(-1,1)
    origin_distance = rnd_x**2 + rnd_y**2

    if origin_distance <= 1:
        circle_points += 1
    square_points += 1

    pi = 4 * circle_points / square_points

print("Estimated pi value through simulation: ", pi)