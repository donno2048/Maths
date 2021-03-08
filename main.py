from math import cos, e, sqrt
from matplotlib.pyplot import figure, plot, show
from matplotlib.animation import FuncAnimation
x, y, z, fig, data = [], [], [], figure(figsize = (12.8, 9.6)), open("main.tex").readlines()
def animate(i):
    x.append(i / 1000)
    y.append(sum([cos(3 ** n * i / 1000) / (3 ** n) for n in range(10)])) # 10 instead of ∞
    z.append(sum([cos(3 ** n * i / 1000) / (e ** (sqrt(3 ** n) - 1)) for n in range(10)])) # 10 instead of ∞
    plot(x, y, "b-", x, z, "r-")
fig.text(0.05, 0.96, data[1][:-3] + ' ' + data[2][:-3], bbox = dict(facecolor = 'blue', alpha = 0.5))
fig.text(0.05, 0.907, data[3][:-3] + ' ' + data[4][:-1], bbox = dict(facecolor = 'red', alpha = 0.5))
anim = FuncAnimation(fig, animate)
show()
