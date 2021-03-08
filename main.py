from math import cos, e, sqrt
from matplotlib.pyplot import figure, plot, show
from matplotlib.animation import FuncAnimation
x, y, z = [], [], []
def animate(i):
    x.append(i / 1000)
    y.append(sum([cos(3 ** n * i / 1000) / (3 ** n) for n in range(10)])) # 10 instead of ∞
    z.append(sum([cos(3 ** n * i / 1000) / (e ** (sqrt(3 ** n) - 1)) for n in range(10)])) # 10 instead of ∞
    plot(x, y, "b-", x, z, "r-")
fig = figure(figsize = (12.8, 9.6))
fig.text(0.05, 0.96, r"$\sum_{n=0}^\infty\frac{\cos\left(3^nx\right)}{3^n}$ Is continuous but not differentiable in any point", bbox = dict(facecolor = 'blue', alpha = 0.5))
fig.text(0.05, 0.907, r"$\sum_{n=0}^\infty\frac{\cos\left(3^nx\right)}{e^{-1+\sqrt{3^n}}}$ Is smooth but not analytic in any point", bbox = dict(facecolor = 'red', alpha = 0.5))
anim = FuncAnimation(fig, animate)
show()
