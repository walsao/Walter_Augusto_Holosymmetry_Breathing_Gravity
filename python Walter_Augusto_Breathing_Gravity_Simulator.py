# 🚀 Walter Augusto's Holobreathing Gravity: Breathing Condensation Animation (Save GIF - smaller version)

# --- Import libraries ---
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import matplotlib.animation as animation

# --- Define Parameters ---
epsilon = 0.1        # Nonlinear self-densification strength
phi0 = 0.1           # Initial breathing phase
phi_dot0 = 0.0       # Initial breathing rate

# 🌟 Smaller breathing time span
t_span = (0, 10)    # Smaller, faster breathing (only from t=0 to t=10)
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # 1000 points (smooth but small)

# --- Define the Breathing Condensation Equation ---
def breathing_condensation(t, y):
    phi, phi_dot = y
    dphi_dt = phi_dot
    dphi_dot_dt = -np.sin(phi) * (1 + epsilon * phi**2)
    return [dphi_dt, dphi_dot_dt]

# --- Solve the System ---
initial_conditions = [phi0, phi_dot0]
sol = solve_ivp(breathing_condensation, t_span, initial_conditions, t_eval=t_eval, method='RK45')

# --- Set up the Animation ---
fig, ax = plt.subplots(figsize=(6, 6))  # smaller figure
ax.set_xlim(-0.15, 0.15)
ax.set_ylim(-0.15, 0.15)
ax.set_xlabel(r'$\varphi$ (Breathing Phase)', fontsize=12)
ax.set_ylabel(r'$\dot{\varphi}$ (Breathing Rate)', fontsize=12)
ax.set_title("Walter Augusto's Holobreathing Field Animation 🌬️", fontsize=14)
line, = ax.plot([], [], 'o-', color='purple', markersize=8)

# --- Initialization function ---
def init():
    line.set_data([], [])
    return (line,)

# --- Update function ---
def update(frame):
    x = sol.y[0][:frame+1]  # Breathing phase values up to current frame
    y = sol.y[1][:frame+1]  # Breathing rate values up to current frame
    line.set_data(x, y)
    return (line,)

# --- Create and Save the Animation ---
ani = animation.FuncAnimation(
    fig, update, frames=len(t_eval),
    init_func=init, blit=True, interval=20  # 20ms between frames
)

# --- Save animation as a GIF file ---
ani.save('Walter_Augusto_Holobreathing_Condensation_Small.gif', writer='pillow', fps=30)

print("✅ Animation saved as 'Walter_Augusto_Holobreathing_Condensation_Small.gif'! Check the Files panel 📂 to download it.")
