import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.5, 10, 1)
y = np.log(2 * x)
y1 = -4 * x + 2
y2 = np.cos(x) * 2
plt.plot(x, y, 'm:', label="log(2x)")
plt.plot(x, y1, 'c--', label="-4x+2")
plt.plot(x, y2, 'y-.', label="2cos(x")
plt.title("Wykres funkcji trygonometrycznych")
plt.xlabel("oś dolna", color="blue")
plt.ylabel("oś lewa", color="red")
plt.legend(loc='lower left')
plt.grid()
plt.savefig("zad1.png")
plt.show()
