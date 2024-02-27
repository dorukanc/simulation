import random

# Initial state: both machines are active
machine_count = 2
time = 0
both_crashed_time = None

# Simulate the process over time
while time < 30:
    # Increment time
    time += 1
    print("Time:", time)

    # Simulate a random crash time for each machine
    crash_times = random.randint(1, 6)

    # Check if any machine crashes at the current time
    for machine_index, crash_time in enumerate(crash_times):
        if crash_time == time:
            machine_count -= 1
            print(f"Machine {machine_index + 1} crashed! Remaining active machines:", machine_count)

            if machine_count == 0:
                both_crashed_time = time
                break

    if both_crashed_time is not None:
        print(f"Both machines crashed at time {both_crashed_time}. System failure!")
        break

    # Update machine count if necessary
    if machine_count < 2:  # If there are crashed machines
        repair_time = time + (0.5 if random.random() < 0.5 else 4.5)  # 50% chance of quick repair, 50% chance of slow repair
        print(f"Machine repaired at time {repair_time}")
        machine_count += 1

    # Print the current state of the machines
    print("Current state of machines:", machine_count)

    # Add a line break for clarity
    print()
