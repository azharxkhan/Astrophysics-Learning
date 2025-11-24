"""
Photon counting simulation for a faint star modelled as a Poisson process.
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_photon_counts(rate_lambda, t_total, dt):
    """
    rate_lambda: photons per second
    t_total: total simulation time (seconds)
    dt: time step (seconds)

    Returns:
        times, counts_per_bin
    """
    n_steps = int(t_total / dt)
    times = np.arange(n_steps) * dt
    # Poisson mean for each bin
    mean_per_bin = rate_lambda * dt
    counts = np.random.poisson(mean_per_bin, size=n_steps)
    return times, counts


def main():
    rate_lambda = 4.0   # photons per second
    t_total = 100.0     # simulate 100 seconds
    dt = 0.5            # 0.5 second time bin

    times, counts = simulate_photon_counts(rate_lambda, t_total, dt)

    plt.figure()
    plt.step(times, counts, where="mid")
    plt.xlabel("Time (s)")
    plt.ylabel("Counts per bin")
    plt.title("Photon counting simulation (Poisson process)")
    plt.show()

    # histogram of counts
    plt.figure()
    plt.hist(counts, bins=range(0, max(counts)+2), align="left", rwidth=0.8)
    plt.xlabel("Counts per bin")
    plt.ylabel("Frequency")
    plt.title("Distribution of counts per time bin")
    plt.show()


if __name__ == "__main__":
    main()
