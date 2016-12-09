import matplotlib.pyplot as pyplot

def f(x):
    return 2*x+1

def g(x):
    return x + 1

xs = range(-3, 5)

ys = []

for x in xs:
    ys.append(f(x))

plot.plot(xs,ys)
plot.show()
