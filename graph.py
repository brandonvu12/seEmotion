import matplotlib.pyplot as plt
import time
import random
import alg
import webcam

xdata = []
ydata = []
plt.show()

axes = plt.gca()
axes.set_xlim(0,30)
axes.set_ylim(0, 100)
line, = axes.plot(xdata, ydata, 'r-')

for i in range(30):
    xdata.append(i)
    ysample = webcam.web()
    print(f'Confusion Index: {ysample}')
    ydata.append(ysample)
    line.set_xdata(xdata)
    line.set_ydata(ydata)
    plt.draw()
    plt.pause(1e-17)
    time.sleep(2)

# add this if you don't want the window to disappear at the end
plt.show()
