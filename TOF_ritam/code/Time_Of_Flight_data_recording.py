import re
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from scipy.stats import norm

def parse_ion_data(text):
    # Pattern to match each ion entry
    pattern = re.compile(
        r"Ion\((\d+)\) TOF\(([\d.]+) usec\) X\(([\d.-]+) mm\) Y\(([\d.-]+) mm\) Z\(([\d.-]+) mm\)\s+"
        r"Ion\(\1\) TOF\(([\d.]+) usec\) X\(([\d.-]+) mm\) Y\(([\d.-]+) mm\) Z\(([\d.-]+) mm\)"
    )
    
    data = []
    for match in pattern.finditer(text):
        ion_number = int(match.group(1))
        tof_start = float(match.group(2))
        start_x = float(match.group(3))
        start_y = float(match.group(4))
        start_z = float(match.group(5))
        tof_end = float(match.group(6))
        end_x = float(match.group(7))
        end_y = float(match.group(8))
        end_z = float(match.group(9))

        data.append([ion_number, tof_start, start_x, start_y, start_z, tof_end, end_x, end_y, end_z])
    
    return np.array(data)

def plot_histogram(filename,bins):
    with open(f"TOF_ritam/data/{filename}.txt","r") as file:
        text = file.read()
    ion_array = parse_ion_data(text)
    
    plt.figure(figsize=(10,8))
    plt.hist(ion_array[:,5],bins=bins, color='steelblue', edgecolor='black')
    plt.xlabel("Time of Flight (μs)")
    plt.ylabel("Counts")
    plt.title(f"Time of Flight Histogram for {filename}")
    plt.grid()
    plt.tight_layout()
    plt.savefig(f"TOF_ritam/figures/{filename}.png", dpi=300)
    plt.close()
    

def initial_position_plot_3d(filename):
    with open(f"TOF_ritam/data/{filename}.txt", "r") as file:
        text = file.read()
    ion_array = parse_ion_data(text)

    # Extract initial positions
    x_start = ion_array[:, 2]
    y_start = ion_array[:, 3]
    z_start = ion_array[:, 4]

    # Create 3D scatter plot with Plotly
    fig = go.Figure(data=[
        go.Scatter3d(
            x=x_start, y=y_start, z=z_start,
            mode='markers',
            marker=dict(
                size=2,
                color='blue',
                opacity=0.1
            )
        )
    ])

    fig.update_layout(
        scene=dict(
            xaxis_title='X_start (mm)',
            yaxis_title='Y_start (mm)',
            zaxis_title='Z_start (mm)'
        ),
        title=f"3D Scatter Plot of Ion Initial Positions: {filename}",
        margin=dict(l=0, r=0, b=0, t=40)
    )

    # Save as HTML (optional)
    fig.write_html(f"TOF_ritam/figures/{filename}_3D_pos.html")

    # Show interactive plot
    fig.show()

def histogram_parameters_plot(filename, bins1):
    with open(f"TOF_ritam/data/{filename}.txt","r") as file:
        text = file.read()
    ion_array = parse_ion_data(text)
    
    # Fit Gaussian: get mean and std deviation
    mu, sigma = norm.fit(ion_array[:,5])
    
    #Plot the Histogram
    plt.figure(figsize=(10,10))
    counts, bins, _ =plt.hist(ion_array[:,5],bins=bins1, color='steelblue', edgecolor='black')
    
    #Plot the gaussian fit
    x= np.linspace(bins[0],bins[-1], 1000)
    pdf = norm.pdf(x, mu, sigma)
    plt.plot(x, pdf * max(counts) / max(pdf), 'r--', linewidth=2, label=f'Gaussian Fit\nμ={mu:.2f}, σ={sigma:.2f}')
    plt.xlabel("Time of Flight (μs)")
    plt.ylabel("Counts")
    plt.title(f"Time of Flight Histogram with Gaussian Fit for {filename}")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig(f"TOF_ritam/figures/resolution/{filename}_hist_fit.png", dpi=300)
    plt.close()