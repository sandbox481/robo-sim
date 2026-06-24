import numpy as np
import matplotlib.pyplot as plt

# 1. Physical Constants for 4.5ft (1.37m) B1 Droid
g = 9.81              # Gravity (m/s^2)
z_c = 0.8             # Center of Mass height (meters)
T_gait = 0.5          # Time per step (seconds)
dt = 0.01             # Simulation time step (seconds)
omega = np.sqrt(g / z_c) # Natural frequency of the pendulum

# 2. Desired Foot Positions (Steps along the X-axis)
foot_steps = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
total_time = T_gait * (len(foot_steps) - 1)
time_steps = int(total_time / dt)

# 3. Initialize Vectors
time = np.linspace(0, total_time, time_steps)
com_x = np.zeros(time_steps)
zmp_x = np.zeros(time_steps)

# Initial state [position, velocity]
x = 0.0
v = 0.15  # Initial forward push to start walking

# 4. Run Physics Simulation Loop
for idx, t in enumerate(time):
    # Determine which foot step the droid is currently on
    step_phase = int(t / T_gait)
    p = foot_steps[step_phase] # Current active ZMP target
    
    # Calculate CoM acceleration using the LIPM physics equation
    a = (g / z_c) * (x - p)
    
    # Numerical Integration (Euler-Cromer)
    v += a * dt
    x += v * dt
    
    # Store results
    com_x[idx] = x
    zmp_x[idx] = p

# 5. Plot the Balance Trajectory
plt.figure(figsize=(10, 5))
plt.plot(time, com_x, label="Center of Mass (CoM)", color="blue", linewidth=2)
plt.step(time, zmp_x, label="Zero Moment Point / Foot Steps (ZMP)", color="red", linestyle="--", where="post")
plt.title("4.5ft B1 Droid Bipedal Balance Simulation (LIPM)")
plt.xlabel("Time (seconds)")
plt.ylabel("Forward Position (meters)")
plt.grid(True, linestyle=":")
plt.legend()
plt.show()
