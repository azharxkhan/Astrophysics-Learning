# 01_Calculus notes.md

```markdown
# Calculus Notes

This section builds the core mathematical tools you need for mechanics and astrophysics. Calculus describes change. It allows you to study velocity, acceleration, orbits, energy changes, and many physical systems.

---

# 1. What Calculus Studies

Calculus answers questions about:
- how fast something changes (derivatives)
- how much accumulates (integrals)
- how physical systems evolve (differential equations)

Examples in astrophysics:
- how a planet's position changes with time
- how pressure changes inside a star
- how luminosity changes during a supernova
- how density changes in a galaxy

---

# 2. Derivatives

## 2.1 Concept
The derivative of a function f(t) measures how fast the function changes.

Mathematically:
```

f'(t) = lim (h -> 0) [f(t + h) - f(t)] / h

```

## 2.2 Physical meaning
- derivative of position is velocity  
- derivative of velocity is acceleration  
- derivative of temperature can show cooling rates  
- derivative of luminosity can show stellar variability  

## 2.3 Basic rules
- d/dx (x^n) = n x^(n - 1)  
- d/dx (sin x) = cos x  
- d/dx (cos x) = -sin x  
- d/dx (e^x) = e^x  
- d/dx (ln x) = 1/x  

## 2.4 Product rule
```

d/dx (u v) = u' v + u v'

```

## 2.5 Chain rule
Used when functions are inside functions.
```

d/dx f(g(x)) = f'(g(x)) g'(x)

```

---

# 3. Integrals

## 3.1 Concept
Integrals measure accumulated change or total quantity.

Example:
Total distance traveled is the integral of velocity.

Integral notation:
```

∫ f(x) dx

```

## 3.2 Definite integrals
A definite integral between limits a and b:
```

∫ from a to b f(x) dx

```
represents area under the curve.

## 3.3 Fundamental Theorem of Calculus
Differentiation and integration are inverse processes.

If F'(x) = f(x) then:
```

∫ from a to b f(x) dx = F(b) - F(a)

```

---

# 4. Differential Equations

A differential equation relates a function to its derivatives.

Examples:
- radioactive decay: dy/dt = -k y  
- simple harmonic motion: d^2x/dt^2 = -k x  
- gravitational acceleration: d^2r/dt^2 = -GM/r^2  

The ability to solve differential equations is essential for:
- orbital mechanics  
- stellar structure  
- galaxy dynamics  
- cosmology  

---

# 5. Applications in Physics and Astrophysics

## 5.1 Gravity from derivatives
Acceleration is the second derivative of position. For a gravitational system:
```

a = d^2r/dt^2 = -GM / r^2

```

## 5.2 Escape velocity
Escape velocity is found by integrating force or energy.

## 5.3 Orbital motion
Derivatives describe:
- changing direction of velocity
- centripetal acceleration
- elliptical orbits

## 5.4 Stellar structure
Integrals compute:
- mass as a function of radius
- pressure distribution
- luminosity distribution

---

# 6. Key Formulas

Velocity:
```

v = dx/dt

```

Acceleration:
```

a = dv/dt = d^2x/dt^2

```

Area:
```

A = ∫ f(x) dx

```

Exponential growth and decay:
```

y = y0 e^(kt)

```

Newtonian gravity:
```

F = G m M / r^2

```

---

# 7. Checklist Before Moving On

You should be able to:
- compute derivatives of simple functions  
- compute basic integrals  
- plot functions and their derivatives  
- solve simple differential equations  
- connect derivatives to velocity and acceleration  

These skills will be essential for classical mechanics.
```

---