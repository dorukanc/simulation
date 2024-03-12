import random
import matplotlib.pyplot as plt

interval = 1000
under_func_points = 0
rectangle_points = 0

points_underfunc_x = []
points_underfunc_y = []

# generate random points inside rectangle where x is between a and b
# y is between 0 and c
for i in range(interval):

    # Generate rnd_x between 3 and 7
    rnd_x = 3 + (7 - 3) * random.random()
    points_underfunc_x.append(rnd_x)
    # Generate rnd_y between 0 and 0.45
    rnd_y = 0 + (0.45 - 0) * random.random()
    points_underfunc_y.append(rnd_y)


# Plotting square boundary with adjusted rectangle boundaries
plt.plot([3, 7], [0.45, 0.45], color='red')  # Top line
plt.plot([3, 7], [0, 0], color='red')  # Bottom line
plt.plot([3, 3], [0, 0.45], color='red')  # Left line
plt.plot([7, 7], [0, 0.45], color='red')  # Right line

# Adding labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Rectangle Boundaries')

# Plotting points under the function
plt.scatter(points_underfunc_x, points_underfunc_y, color='blue', label='points under the rectangle')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Points under the function')
plt.show()
