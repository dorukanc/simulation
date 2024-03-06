# IE304 Simulation Class Repository

This repository contains Python scripts for simulation exercises conducted in the IE304 Simulation class.

## Contents

1. [Monte Carlo Simulation of π](#monte-carlo-simulation-of-π)
2. [Parking Lot Simulation](#parking-lot-simulation)
3. [Machine Failure and Repair Simulation](#machine-failure-and-repair-simulation)

---

## Monte Carlo Simulation of π

The `montecarlo.py` script utilizes the Monte Carlo method to estimate the value of π. It generates random points within a square and calculates the ratio of points falling inside a quarter circle to the total points. By multiplying this ratio by 4, it approximates the value of π. The script then visualizes the points inside the circle and the square boundary using Matplotlib.


![Alt text](https://raw.githubusercontent.com/dorukanc/simulation/main/imgs/points_inside_circle.png)

---

## Parking Lot Simulation

The `parkingspot.py` script simulates the system state of a parking lot over a period of time using a discrete-event simulation approach. It models car arrivals and departures based on a time-varying arrival rate following a sinusoidal pattern. The script utilizes the SimPy library for event-driven simulation and Pandas for data storage and visualization. It plots the system state (number of cars in the parking lot) against time.

---

## Machine Failure and Repair Simulation

The `sys_state_simulation.py` script simulates the failure and repair process of machines over a specified time period. It models machine failures and repairs using exponential distributions for failure and repair times. The script prints the system state, next failure time, next repair time, and area under the curve of system state over time. It terminates when either all machines fail or the simulation time ends.

---

Feel free to explore and utilize these scripts for simulation exercises in the IE304 Simulation class.