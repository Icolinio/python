import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np
import math
df=pd.read_csv('nieruchomosci2.csv',header=0,sep=';',decimal='.').T
df = df.reset_index(level=0)
df['index'] = df['index'].str.replace(r'.1$','', regex=True)
df['index'] = df['index'].str.replace(r'.2$','', regex=True)
df['index'] = df['index'].str.replace(r'.3$','', regex=True)
"""df.columns = df.iloc[0]
df=df[0:]""" #Gdyby 1 wiersz df był nazwami kolumn
df.rename(columns={"index":"Rynek"}, inplace=True)
df.rename(columns={0:"Metraż"}, inplace=True)
df.rename(columns={1:"Rok"}, inplace=True)
df.rename(columns={2:"Ilość"}, inplace=True)
df['Ilość'] = df['Ilość'].str.replace(r' ','', regex=True)
print(df)
pierw = df.query('Rynek == "rynek pierwotny"')
wtorny = df.query('Rynek == "rynek wtórny"')
y = pierw['Ilość'].to_numpy().astype(float)
y2 = wtorny['Ilość'].to_numpy().astype(float)
print(y)
plt.figure(1)
labels = ['do 40m2','od 40,1 do 60 m2','od 60,1 do 80 m2', 'od 80,1 m2']
mycolours = ["red", "orange", "cyan", "white", "blue", "green"]#kolory
plt.pie(y,colors=mycolours, autopct='%1.1f%%',startangle=20,labels=labels, shadow=True)#zastosowanie funkcji, autopct-ustalenie liczb po przcinku w procentach(drugi procent daje symbol procentu
plt.title('Ilośc mieszkań na rynku pierwotnym w 2018 roku')
plt.legend(loc='lower left')
plt.figure(2)
mycolours = ["red", "orange", "cyan", "white", "blue", "green"]#kolory
plt.pie(y2,colors=mycolours, autopct='%1.1f%%',startangle=20,labels=labels, shadow=True)#zastosowanie funkcji, autopct-ustalenie liczb po przcinku w procentach(drugi procent daje symbol procentu
plt.title('Ilośc mieszkań na rynku wtórnym w 2018 roku')
plt.legend()
plt.show() #pokazanie wykesu
