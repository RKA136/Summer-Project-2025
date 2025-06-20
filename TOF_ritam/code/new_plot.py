from Time_Of_Flight_data_recording import histogram_parameters_plot, plot_resolution
import numpy as np
import matplotlib.pyplot as plt

# data = "TOF_50080"
# mu ,sigma, M = histogram_parameters_plot(data,100, 2.24, 2.84)

# print(f"Mean (μ): {mu:.4f}, Standard Deviation (σ): {sigma:.4f} for {data}")
# print(f"Resolution: M₀ = {M:.4f} for {data}")

sl_no = [40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 80]
plot_resolution(sl_no, 3, 4, 100, exp_no = 5)