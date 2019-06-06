import numpy as np
import Gnuplot

g = Gnuplot.Gnuplot()
g.title("RHN training graph")

g.xlabel("Epoch")
g.ylabel("Perplexity")

g("set grid")

y1 = np.array([3.821,3.619,3.613,3.642,3.550])
y2 = np.array([3.150,3.205,3.179,3.183,3.167])
y3 = np.array([3.007,3.164,3.102,3.011,3.102])
y4 = np.array([2.893,3.020,3.022,3.024,3.032])

y5 = np.array([3.729,3.366,3.183,3.054,2.979])

x = np.arange (len(y1))

d1 = Gnuplot.Data (x, y1, title="Dataset 1 Training Perplexity", with_="lines")
d2 = Gnuplot.Data (x, y2, title="Dataset 2 Training Perplexity", with_="lines")
d3 = Gnuplot.Data (x, y3, title="Dataset 3 Training Perplexity", with_="lines")
d4 = Gnuplot.Data (x, y4, title="Dataset 4 Training Perplexity", with_="lines")
d5 = Gnuplot.Data (x, y5, title="Test8 Valid Perplexity", with_="lines linecolor rgb 'black'")

g("set yrange [2:6]")
g("set terminal svg")
g.plot(d1, d2, d3, d4, d5)

# g.hardcopy (filename='perplexity.png', terminal='png')
g.hardcopy (filename='rhn_perplexity.svg', terminal='svg')

del g