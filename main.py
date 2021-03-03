import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate(i):
    line.set_ydata(np.sin(x * np.pi  + i))
    return line,


fig = plt.figure(figsize = (5, 5))
ax = fig.subplots()
x = np.linspace(-np.pi, np.pi + 10, 300)
line, = ax.plot(x, np.sin(x))

ani = animation.FuncAnimation(fig, animate, interval=250, blit=True)
plt.title("Sine wave demontration with matplotlib")
plt.xlim(xmin=0 , xmax=4)
plt.ylim(ymin=-2 , ymax=2)
plt.show()
