import matplotlib.pyplot as plt
from Salon import *

# Create figure and axes
fig,ax = plt.subplots(1)
ax.set_xlim([0,2000])
ax.set_ylim([0,2000])

salon = Salon()
salon.draw(ax)

plt.show()
