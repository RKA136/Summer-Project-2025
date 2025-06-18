import numpy as np
import matplotlib.pyplot as plt

#Part 1
x1 = [1,2,3,4,5,10,20,30,40,50,60]
y1 = [28.6608,29.3761,30.3371,31.0245,31.8180,36.0146,43.9865,55.6685,64.3914,70.4470,76.4432]
#Part 2
x2 = [1,2]
y2 = [33.7364,34.7915]
#Part 3
x3 = [1,2,5,10,20,30,40,50,60]
y3 = [54.6770,55.3840,57.9298,61.6311,67.6792,232.2784,570.5683,399.3458,322.4526]

#Plotting the data
# plt.figure(figsize=(10, 6))
# plt.plot(x1, y1, marker='o', linestyle='-', color='blue', label='Data Points')
# plt.title('Time of Flight Resolution vs Pusher Voltage')
# plt.xlabel('Pusher Voltage (V)')
# plt.ylabel('Time of Flight Resolution (M₀)')
# plt.xticks(np.arange(0, 70, step=10))
# plt.yticks(np.arange(0, 80, step=10))
# plt.legend()
# plt.grid()
# plt.tight_layout()
# plt.show()

# plt.figure(figsize=(10, 6))
# plt.plot(x2, y2, marker='o', linestyle='-', color='blue', label='Data Points')
# plt.title('Time of Flight Resolution vs Pusher Voltage')
# plt.xlabel('Pusher Voltage (V)')
# plt.ylabel('Time of Flight Resolution (M₀)')
# plt.xticks(np.arange(0, 70, step=10))
# plt.yticks(np.arange(0, 80, step=10))
# plt.legend()
# plt.grid()
# plt.tight_layout()
# plt.show()

plt.figure(figsize=(10, 6))
plt.plot(x3, y3, marker='o', linestyle='-', color='blue', label='Data Points')
plt.title('Time of Flight Resolution vs Pusher Voltage')
plt.xlabel('Pusher Voltage (V)')
plt.ylabel('Time of Flight Resolution (M₀)')
# plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
