import random
import matplotlib.pyplot as plt
import math

# PDF of the normal distrubition
def func(x):
    return math.exp(-x ** 2 / 2) / math.sqrt(2 * math.pi)


interval = 10000000
under_func_points = 0

points_underfunc_x = []
points_underfunc_y = []

# define a b c values
a = -2
b = 2
c = 0.4

area_rectangle = (b - a) * c

# generate random points inside rectangle where x is between a and b
# y is between 0 and c
for i in range(interval):

    # Generate rnd_x between 0 and 2
    rnd_x = a + (b - a) * random.random()
    # Generate rnd_y between 0 and 1
    rnd_y = 0 + c * random.random()

    if rnd_y <= func(rnd_x):
        under_func_points += 1
        points_underfunc_x.append(rnd_x)
        points_underfunc_y.append(rnd_y)

    ratio_in = under_func_points / interval
    estimated_area = ratio_in * area_rectangle

print("Estimated area under the function through simulation is:", estimated_area)

# Adding labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Points under the function')

# Plotting points under the function
plt.scatter(points_underfunc_x, points_underfunc_y, color='blue', label='Points under the function')
plt.legend()
plt.show()
