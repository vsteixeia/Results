import numpy as np
import matplotlib.pyplot as plt

# Nome do arquivo
#plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')

dist1 =  np.loadtxt('output.dat', dtype=float)
dist2 =  np.loadtxt('output2.dat', dtype=float)
#dist3 =  np.loadtxt('Pos +90.dat', dtype=float)
#dist4 =  np.loadtxt('Pos +180.dat', dtype=float)
#dist5 =  np.loadtxt('Pos +270.dat', dtype=float)


plt.xscale("linear")
plt.yscale('symlog')
plt.xlim(0, 300)  

plt.xlabel("tempo(ns)")
plt.ylabel("nº de fótons")

plt.hist(dist1, bins=251, histtype="step", label="0cm")
plt.hist(dist2, bins=251, histtype="step", label="036cm")
#plt.hist(dist3, bins=251, histtype="step", label="90cm")
#plt.hist(dist4, bins=251, histtype="step", label="180cm")
#plt.hist(dist5, bins=251, histtype="step", label="270cm")
plt.legend(loc="upper right")
plt.show()

