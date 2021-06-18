# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 19:59:13 2021

@author: Manuel
"""

import pandas as pd

DF=pd.read_csv("data.csv")

X=pd.DataFrame(DF[['Apellido','Nombre','Codigo']])

correos=['jairo.custodio@utec.edu.pe','manuel.carita@utec.edu.pe']

correo=[correos[i%2] for i in range(DF.shape[0])]

X['Correo']=correo

X=X.dropna()

X['Codigo']=X['Codigo'].astype(int)

X.to_csv('Base_de_datos.csv')


    













