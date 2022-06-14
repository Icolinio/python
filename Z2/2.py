import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np
import math

df = pd.read_excel("ceny2.xlsx")

print(df)
r = df.loc[df["Rodzaje towarów"]== "ryż - za 1kg"]
m = df.loc[df["Rodzaje towarów"]== "mąka pszenna - za 1kg"]
print(r)

cenar  = r["Wartość"]
miesiacr = r["Rok"]
cenam  = m["Wartość"]
miesiacm = m["Rok"]

print("mąka pszenna - za 1kg : ", m["Wartość"].mean().round(2))
print("ryż - za 1kg : ", r["Wartość"].mean().round(2))


plt.plot(miesiacm, cenam, ls='--' ,label='mąka', color = "orange")
plt.plot(miesiacr, cenar, ls='-.' ,label='ryż', color = "red")
plt.xlabel("Miesiące")
plt.ylabel("Ceny w zł")
plt.text(0,1, "162647")
plt.grid()
plt.legend()
plt.title("Cena towaru za 1 kg rok 2017")
plt.savefig("excel.jpg")
plt.show()
