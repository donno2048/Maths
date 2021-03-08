_main.py_ are just two interesting functions and their "pretty render", _init.py_ is a general case solution, you can use it to make "pretty renders" of functions,

Use it like so:

```py
from init import main
from math import cos
main("sum([cos(3 ** n * x / 1000) / (3 ** n) for n in range(10)])", Text = r"$\sum_{n=0}^\infty\frac{\cos\left(3^nx\right)}{3^n}$ Is continuous but not differentiable in any point", LineColor = "blue", TextColor = "blue", start = 0, end = 10, step = .001)
```

The first argument is the function (`x` is the variable),

`Text` is the additional text,

`LineColor` is the color of the line plotted, either `blue`, `green`, `red`, `cyan`, `magenta`, `yellow`, `black` or `white`,

`TextColor` is the color of the additional text, same colors as LineColor,

`start`, `end` and `step` are the starting and ending points and the size of the steps between them.
