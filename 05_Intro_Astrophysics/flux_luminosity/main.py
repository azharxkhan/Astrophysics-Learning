"""
Flux and luminosity calculator.

Given luminosity and distance, compute flux.
Given flux and distance, compute luminosity.
"""

import math

FOUR_PI = 4.0 * math.pi

def flux_from_luminosity(L, d):
    """Compute flux F from luminosity L and distance d."""
    return L / (FOUR_PI * d * d)


def luminosity_from_flux(F, d):
    """Compute luminosity L from flux F and distance d."""
    return F * FOUR_PI * d * d


def main():
    # example: star with 5 times solar luminosity at 10 parsec
    L_sun = 3.828e26  # W
    parsec = 3.086e16 # m
    L = 5.0 * L_sun
    d = 10.0 * parsec

    F = flux_from_luminosity(L, d)
    print(f"Luminosity: {L:.3e} W")
    print(f"Distance: {d:.3e} m")
    print(f"Flux at Earth: {F:.3e} W m^-2")


if __name__ == "__main__":
    main()
