import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_excel('wyn12.xlsx')  #wczytywanie plku xlsx
print(data)

z = data["Wartość"] #przypisywanie kolumny do zmiennej aby mozna ją było yużyć w wykresie
y = data["Rok"] #to samo co wyżej
k = ["grey", "red", "green", "yellow", "pink", "cyan"]
print(z)
plt.bar(y, z, color=k) #pierwsze to jest określenie osi x, drugie osi y, czyli w pierwszym dajemy podpis kolumny, a w drugim dane które chcemy wyświetlić
plt.xlabel('Rok')
plt.ylabel('Wartości(zł)')
plt.title("Polska")
plt.annotate(xy=[2019.5, 5000], text="11.06.2022")
plt.savefig('Polska.pdf')
plt.show()