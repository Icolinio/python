import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('ceny41.xlsx')

p1 = data.query('`Rodzaje towarów i usług`.str.startswith("marchew")', engine="python").reset_index(level=0)
p2 = data.query('`Rodzaje towarów i usług`.str.startswith("cebula")', engine="python").reset_index(level=0)
p3 = data.query('`Rodzaje towarów i usług`.str.startswith("ziemniaki")', engine="python").reset_index(level=0)
print("Produkt 1 - ", p1['Wartosc'].mean().round(2))
print("Produkt 2 - ", p2['Wartosc'].mean().round(2))
print("Produkt 3 - ", p3['Wartosc'].mean().round(2))
plt.plot(p1['Wartosc'], label = "Marchew")
plt.plot(p2['Wartosc'], label = "Cebula")
plt.plot(p3['Wartosc'], label = "Ziemniaki")
plt.annotate(xy=[0.1, 1], text="166234")
plt.legend()
plt.title("Ceny produktów w roku 2017")
plt.xlabel("Miesiąc", color="blue")
plt.ylabel("Wartość w zł", color="red")
plt.savefig("zad2.png")
plt.show()
print(d1)
