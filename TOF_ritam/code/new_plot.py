from Time_Of_Flight_data_recording import histogram_parameters_plot, plot_resolution
import numpy as np
import matplotlib.pyplot as plt

data = "TOF_440"
mu ,sigma, M = histogram_parameters_plot(data,100, 2.24, 2.84)

print(f"Mean (μ): {mu:.4f}, Standard Deviation (σ): {sigma:.4f} for {data}")
print(f"Resolution: M₀ = {M:.4f} for {data}")

# sl_no = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
# plot_resolution(sl_no, 2.24, 2.84, 100, exp_no = 5)




