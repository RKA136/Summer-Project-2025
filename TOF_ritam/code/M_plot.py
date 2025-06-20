import numpy as np
import matplotlib.pyplot as plt

#Part 1
x1 = [1,2,3,4,5,10,20,30,40,50,60]
y1 = [28.6608,29.3761,30.3371,31.0245,31.8180,36.0146,43.9865,55.6685,64.3914,70.4470,76.4432]
#Part 2
x2 = [1,2]
y2 = [33.7364,34.7915]
#Part 3
x3 = [1,2,5,10,20,30,40,50,60,70,80,90]
y3 = [54.6770,55.3840,57.9298,61.6311,67.6792,232.2784,570.5683,399.3458,322.4526,277.3566,249.4695,230.1245]

x4 = [-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40]
y4 = [608.6528,677.9655,738.5214,804.4702,843.7715,869.7935,879.3759,855.2658,829.6655,786.9454,747.5100,703.3694,665.8420,630.0221,602.3372,561.7344,541.2152,515.9305,491.5023,469.8987,454.1571]

plt.figure(figsize=(10, 6))
plt.plot(x4, y4, marker='o', linestyle='-', color='blue')
plt.title('Time of Flight Resolution vs Pusher Voltage for m = 5 amu')
plt.xlabel('Pusher Voltage (V)')
plt.ylabel('Time of Flight Resolution (M₀)')
# plt.xscale('log')
plt.yscale('log')
plt.grid()
plt.tight_layout()
plt.savefig('TOF_ritam/figures/resolution/TOF_ritam_m5.png')
plt.close()

