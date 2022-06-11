import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

y = np.array([16.81, 18.07, 13.87, 14.71, 17.23, 19.33]) #wpisywanie danych do wyresu
mycolours = ["red", "orange", "cyan", "white", "blue", "green"]#kolory
myxplode = [0, 0.1, 0, 0, 0, 0]#wysunięcie kawałka "ciasta"
plt.pie(y,colors=mycolours, explode=myxplode, autopct='%1.2f%%',startangle=20,labeldistance=2)#zastosowanie funkcji, autopct-ustalenie liczb po przcinku w procentach(drugi procent daje symbol procentu
plt.title('Wykres')                                                             #startangle - obracanie wykresu   #labeldistance - odleglosc labeli (nie dawac wievej niz 2
plt.text(-1, -1, 'LD')
plt.text(-1, 1, 'LG')
plt.text(1, -1, 'PD')
plt.text(1, 1, 'PG')
plt.show() #pokazanie wykesu