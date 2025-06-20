from Time_Of_Flight_data_recording import histogram_parameters_plot, plot_resolution

# This code is so see the mean pattern
# data = "TOF_40100"
# mu ,sigma, M = histogram_parameters_plot(data,100, 2.24, 2.84)
# print(f"Mean (μ): {mu:.4f}, Standard Deviation (σ): {sigma:.4f} for {data}")
# print(f"Resolution: M₀ = {M:.4f} for {data}")

# This code is to plot the resolution for different experiments
# sl_no = [80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
# plot_resolution(sl_no, 3, 4, 100, exp_no = 4)


# To plot the peak resolution $(M_0)_{\\text{max}}$ against pusher voltage, you can use the following code snippet.
#import matplotlib.pyplot as plt

# # Data
# masses = [5, 10, 15, 20]
# M0_max = [879.3759, 892.7769, 384.5350, 298.6782]
# pusher_voltages = [-26, -33, -57, -83]

# # Colors for each mass
# colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']

# plt.figure(figsize=(10, 6))

# for mass, m0, voltage, color in zip(masses, M0_max, pusher_voltages, colors):
#     # Scatter point
#     plt.scatter(voltage, m0, label=f"Mass = {mass} amu", color=color, s=100)
    
#     # Horizontal line: from y-axis (x=plt.xlim()[0]) to point's x
#     plt.plot([plt.xlim()[0], voltage], [m0, m0], linestyle='--', color=color, linewidth=1)

#     # Vertical line: from x-axis (y=plt.ylim()[0]) to point's y
#     plt.plot([voltage, voltage], [plt.ylim()[0], m0], linestyle='--', color=color, linewidth=1)

# # Set limits before plotting ticks to avoid changes after plotting
# plt.xlim(min(pusher_voltages) - 10, 0)
# plt.ylim(0, max(M0_max) + 100)

# # Custom ticks
# plt.xticks(pusher_voltages, [f"{v}V" for v in pusher_voltages], fontsize=12)
# plt.yticks(M0_max, [f"{m0:.1f}" for m0 in M0_max], fontsize=12)

# # Labels and title
# plt.xlabel("Pusher Voltage (V)", fontsize=14)
# plt.ylabel("$(M_0)_{\\text{max}}$", fontsize=14)
# plt.title("Peak Resolution $(M_0)_{\\text{max}}$ vs Pusher Voltage", fontsize=16)
# plt.grid(True, linestyle=':', linewidth=0.5)
# plt.legend(title="Mass", fontsize=12)

# # Save and show
# plt.tight_layout()
# plt.savefig("TOF_ritam/figures/M0max_vs_pusher_voltage.png", dpi=300)
# plt.show()
