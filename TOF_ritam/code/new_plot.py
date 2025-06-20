from Time_Of_Flight_data_recording import histogram_parameters_plot, plot_resolution

# data = "TOF_40100"
# mu ,sigma, M = histogram_parameters_plot(data,100, 2.24, 2.84)

# print(f"Mean (μ): {mu:.4f}, Standard Deviation (σ): {sigma:.4f} for {data}")
# print(f"Resolution: M₀ = {M:.4f} for {data}")

sl_no = [80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
plot_resolution(sl_no, 3, 4, 100, exp_no = 4)