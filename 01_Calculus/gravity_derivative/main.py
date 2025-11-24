import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11
M = 5.972e24
R = 6.371e6

# position function for free fall (simple model)
def y(t):
    return 1000 - 0.5 * 9.8 * t * t

# first derivative: velocity
def v(t, h=1e-5):
    return (y(t + h) - y(t)) / h

# second derivative: acceleration
def a(t, h=1e-5):
    return (v(t + h) - v(t)) / h

times = np.linspace(0, 8, 300)

plt.plot(times, [y(t) for t in times], label="Position")
plt.plot(times, [v(t) for t in times], label="Velocity")
plt.plot(times, [a(t) for t in times], label="Acceleration")
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("Derivatives linked to gravitational acceleration")
plt.legend()
plt.show()
