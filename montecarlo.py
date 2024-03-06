import random
import matplotlib.pyplot as plt

interval = 1000
circle_points = 0
square_points = 0

points_inside_circlex = []
points_inside_circley = []


for i in range(interval):
    
    rnd_x = random.uniform(-1,1)
    rnd_y = random.uniform(-1,1)
    origin_distance = rnd_x**2 + rnd_y**2

    if origin_distance <= 1:
        circle_points += 1
        points_inside_circlex.append(rnd_x)
        points_inside_circley.append(rnd_y)
    square_points += 1

    pi = 4 * circle_points / square_points

print("Estimated pi value through simulation: ", pi)

#Plotting square boundary
plt.plot([-1, 1], [1, 1], color='red')  # Top line
plt.plot([-1, 1], [-1, -1], color='red')  # Bottom line
plt.plot([-1, -1], [-1, 1], color='red')  # Left line
plt.plot([1, 1], [-1, 1], color='red')  # Right line

# Plotting points inside the circle
plt.scatter(points_inside_circlex, points_inside_circley, color='blue', label='points inside circle')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Points inside circle')
plt.legend()
plt.axis('equal')
plt.show()