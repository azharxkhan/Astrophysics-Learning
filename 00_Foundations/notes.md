---

# 1. Scientific Notation

## 1.1 Why it is important
Astrophysics uses very large and very small numbers. Scientific notation makes them easy to read, compare, and compute.

Examples:
- Mass of the Sun: 1.989 × 10^30 kg
- Radius of an atom: 1 × 10^-10 m
- Milky Way diameter: 1 × 10^21 m

## 1.2 Form
A number is written as:
```

a × 10^n

```
where:
- a is between 1 and 10  
- n is the power of ten

Examples:
- 45000 = 4.5 × 10^4
- 0.00032 = 3.2 × 10^-4

## 1.3 Rules of powers of ten
- Multiply: (a × 10^m)(b × 10^n) = ab × 10^(m + n)
- Divide: (a × 10^m)/(b × 10^n) = (a/b) × 10^(m - n)
- Powers: (10^a)(10^b) = 10^(a + b)

These rules are used constantly in astrophysics.

---

# 2. Units and Dimensions

## 2.1 SI Units
Astrophysics mostly uses SI units:
- Length: metre (m)
- Mass: kilogram (kg)
- Time: second (s)
- Temperature: kelvin (K)

## 2.2 Astronomical Units
More convenient units are used for cosmic distances:
- Astronomical unit (AU): 1.496 × 10^11 m  
- Light year: 9.461 × 10^15 m  
- Parsec: 3.086 × 10^16 m  
- Mass of Sun: M☉ = 1.989 × 10^30 kg  
- Speed of light: c = 3 × 10^8 m/s  

## 2.3 Dimensional Analysis
Used to check equations and derive relationships.

Example:
Gravitational force:
```

F = G m M / r^2

```
Dimensions must match newtons (kg m s^-2).

Dimensional analysis confirms the form of many astrophysical laws.

---

# 3. Functions and Graphs

## 3.1 What is a function
A function maps an input to an output:
```

f(x) gives a value for each x

```

Examples:
- Position as a function of time  
- Temperature as a function of radius inside a star  
- Luminosity as a function of time in a supernova  

## 3.2 Common functions used in astrophysics
- Linear: f(x) = ax + b  
- Quadratic: f(x) = ax^2 + bx + c  
- Power laws: f(x) = k x^n  
  (common in mass luminosity relations)
- Exponential: f(x) = e^(kx)  
- Logarithmic: f(x) = log(x)  
  (used in magnitude scales and temperature relations)

## 3.3 Graph interpretation
You should recognize:
- slopes  
- intercepts  
- curvature  
- asymptotes  

Graphs appear everywhere:
- Hertzsprung Russell diagrams  
- galaxy rotation curves  
- light curves of variable stars  

---

# 4. Vectors

## 4.1 Definition
A vector has magnitude and direction.

In 2D:
```

A = (Ax, Ay)

```
In 3D:
```

A = (Ax, Ay, Az)

```

## 4.2 Magnitude
```

|A| = sqrt(Ax^2 + Ay^2 + Az^2)

```

## 4.3 Vector addition
```

A + B = (Ax + Bx, Ay + By, Az + Bz)

```

## 4.4 Dot product
```

A · B = Ax Bx + Ay By + Az Bz

```
Gives:
- projection of one vector onto another  
- allows calculation of angles  

## 4.5 Cross product (3D only)
Produces a vector perpendicular to both inputs:
```

A × B

```
Magnitude is:
```

|A||B| sin(theta)

```
Used heavily in angular momentum and torque.

---

# 5. Basic Newtonian Physics

## 5.1 Newton's Laws
1. An object stays at rest or moves at constant velocity unless a net force acts.  
2. Force equals mass times acceleration (F = m a).  
3. Every force has an equal and opposite reaction.

These laws form the base of orbital mechanics.

## 5.2 Work and Energy
Work:
```

W = F d

```
Kinetic energy:
```

K = 1/2 m v^2

```
Potential energy:
Near Earth:
```

U = m g h

```
In general gravity:
```

U = -G m M / r

```

## 5.3 Gravity
Newtonian gravitational force:
```

F = G m M / r^2

```
This explains:
- orbits  
- tides  
- galaxy rotation dynamics  
- free fall  

## 5.4 Motion in one dimension
If acceleration is constant (example: gravity):
```

v = u + a t
d = u t + 1/2 a t^2

```

These equations are the foundation you will later replace with calculus.

---

# 6. Why These Foundations Matter

These are the tools that allow you to progress to real astrophysics.

Calculus needs:
- functions  
- slopes  
- rates of change  

Mechanics needs:
- vectors  
- forces  
- energy  

Astrophysics needs:
- units  
- scaling laws  
- scientific notation  
- gravitational relationships  

Everything in higher levels builds directly on these ideas.

---

# 7. Checklist Before Moving to Calculus

You should be able to:

- convert distances between AU, light years, and metres  
- write numbers in scientific notation  
- add and subtract vectors  
- compute dot product and magnitude  
- read and interpret simple graphs  
- compute basic motion under constant acceleration  
- understand gravitational force in its simple form  

If you are comfortable with all items above, you are ready for **Milestone 2**.
```
