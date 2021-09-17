# pythonista_matplotlib_backports
Various backports from newer matplotlib to pythonistas version

Usage example shown below
``` 
"""
A simple example of an animated plot
"""
import pythonista_matplotlib_backports #do this first before matplotlib import

# regular simple example start
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi']=80 #smaller = faster # this is a good idea on pythonista
import matplotlib.animation as animation


fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)        # x-array
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x+i/10.0))  # update the data
    return line,

#Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 30), init_func=init,
    interval=25, blit=True)

#ani.show() no, cannot do this in pythonista

# pythonista specific, convert to html and display
html=ani.to_jshtml()
import ui
w=ui.WebView(frame=(0,0,1024,980))
w.load_html(html)
w.present('sheet')
``` 
