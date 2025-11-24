import numpy as np
import matplotlib.pyplot as plt

# position as a function of time
def x(t):
    return 3*t*t + 2*t - 5

# numerical derivative for velocity
def velocity(t, h=1e-4):
    return (x(t + h) - x(t)) / h

# sample times
times = np.linspace(0, 5, 200)
positions = x(times)
velocities = [velocity(t) for t in times]

plt.plot(times, positions, label="Position x(t)")
plt.plot(times, velocities, label="Velocity dx/dt")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.title("Position and derivative based velocity")
plt.show()
