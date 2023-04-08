# -*- coding: utf-8 -*-
"""Preprocessing Data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cqh-pSaXNFmyEBH8gqZWYwuRbifDqIqU
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""numpy merupakan library python digunakan untuk komputasi matriks. Matplotlib merupakan library pythin unutk presentasi data berupa grafik atau plot """

dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

"""pada variable x disini yang -1 mengartikan bahwa mengambil semua kolom data kecuali kolom terakhir pada data csv

pada variable y untuk menampung semua label pada kolom terakhir yg pada daa csv ini berlabel "Yes" dan "No"
"""

print(x)

print(y)

from sklearn.impute import SimpleImputer 
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

"""mengganti nilai nan menggunakan mean atau menguah nilai nan menjadi rata rata dari data yang ada"""

print(x)

"""mengubah column country ke dalam bentuk matrix menggunakan ColumnTransformer"""

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x))

print(x)

"""mengubah label yes no ke dalam bentuk numerik"""

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

print(y)

"""membagi dataset ke dalam training dan testing
0.2 disini bermaksud untuk 20% testing sisanya 80 %training
"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

print(x_train)

print(x_test)

print(y_train)

print(y_test)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])
x_test[:, 3:] = sc.transform(x_test[:, 3:])

"""menscaling atau membuat scala lebih dekat dan tidak terlalu jauh"""

print(x_train)

print(x_test)