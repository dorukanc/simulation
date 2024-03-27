# IE304 Simulation Class Repository

This repository contains Python scripts for simulation exercises conducted in the IE304 Simulation class.

## Contents

1. [Monte Carlo Simulation of π](#monte-carlo-simulation-of-π)
2. [Parking Lot Simulation](#parking-lot-simulation)
3. [Machine Failure and Repair Simulation](#machine-failure-and-repair-simulation)
4. [Normal Distribution Simulation](#normal-distribution-simulation)
5. [Input Data Analysis](#input-data-analysis)

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

## Normal Distribution Simulation

The `areaunderfunc_sim.py` script simulates the estimation of the area under a normal distribution curve using Monte Carlo simulation. It generates random points within a rectangle and calculates the ratio of points falling under the normal distribution curve to the total points. By multiplying this ratio by the area of the rectangle, it approximates the area under the curve. The script visualizes the points falling under the curve using Matplotlib.

![Alt text](https://raw.githubusercontent.com/dorukanc/simulation/main/imgs/pointsunderfunction.png)

## Input Data Analysis

This section provides an analysis of the input data using Python. It includes fitting the data to both normal and exponential distributions, plotting histograms with different bin sizes along with the fitted PDFs, displaying fitted parameters, and performing Kolmogorov-Smirnov tests for both distributions. The results are interpreted, including null hypotheses about the distribution of the data.

![Alt text](https://raw.githubusercontent.com/dorukanc/simulation/main/imgs/input_data_analysis.png)


Feel free to explore and utilize these scripts for simulation exercises in the IE304 Simulation class.
