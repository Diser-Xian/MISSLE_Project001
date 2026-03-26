pi = 3.1415926535
g = 9.8

v = float(input("Enter speed: "))
angle = float(input("Enter angle (degrees): "))

# convert to radians
theta = angle * pi / 180

# sin and cos approximation
sin_t = theta - (theta**3)/6
cos_t = 1 - (theta**2)/2

vx = v * cos_t
vy = v * sin_t

time = (2 * vy) / g
height = (vy**2) / (2 * g)
distance = vx * time

print("Flight time:", time)
print("Max height:", height)
print("Distance:", distance)

# trajectory points
t = 0
step = time / 10

while t <= time:
    x = vx * t
    y = vy * t - 0.5 * g * t * t
    print("x:", x, "y:", y)
    t += step