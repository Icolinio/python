import matplotlib.pyplot as plt
import numpy as np

wyk1 = [39, 40, 16, 45, 37]
wyk2 = [-37, -36, -16, -33, -37]
Y = np.arange(5)
plt.subplot(1, 2, 1)
plt.barh(Y, wyk1, color=['lightblue', 'pink', 'orange', 'gray', 'purple'], height=0.75, label="A", )
plt.title("Wykres lewy")
plt.yticks(Y, ['A', 'B', 'C', 'D', 'E'])
plt.subplot(1, 2, 2)
plt.barh(Y, wyk2, color=['pink', 'blue', 'lightblue', 'brown', 'yellow'], height=0.75, label="B")
plt.title("Wykres lewy")
plt.yticks(Y, ['A', 'B', 'C', 'D', 'E'])
plt.show()
