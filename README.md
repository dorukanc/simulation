# IE304 Simulation Class Python Examples

This repository contains Python code examples for the IE304 Simulation class. These examples demonstrate simple simulations of machine failures and repairs.

## Example Code

### Description
The provided Python script simulates the failure and repair process of a machine system with two machines. It calculates the downtime and uptime of the system.

### Usage
1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Run the script `simulation.py` using Python.

```bash
python simulation.py
```

### Simulation Parameters
- `machine_count`: Number of machines in the system.
- `repair_time`: Time taken to repair a machine.
- `simulation_time`: Duration of the simulation.

## Simulation Output
The script prints the following information for each time step:
- Clock time.
- Number of working machines (`SS`).
- Time until the next failure (`NF`).
- Time until the next repair (`NR`).
- Area under the uptime curve (`Area Under S`).

## License
This code is provided under the [MIT License](LICENSE).
