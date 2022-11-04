# -*- coding: utf-8 -*-
"""
@author: CRISTIAN
"""


#USO DE REGRESION MULTI LAYER PERCEPTRON

import numpy as np 
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split

"""Se tiene dos conjuntos de datos un tiempo y una nota,
el tiempo e lo que se demoro en estudiar para un examen y la nota
lo que obtuvo por estudiar ese tiempo, se quiere predecir cuanto sacaria
estudian x tiempo """ 

tiempo = [0,4,8,12,14,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100,104,108,112,116,120,124,128,132,135,136,2,170,173]
nota = [0,0,0.5,0.5,6.7,1,1,2.2,3,2,2.8,3.5,3.7,4,5,5.5,6,3,6,6,6,7,7.2,8,6.9,7,7.4,7.5,7,8,8.2,8.5,4.2,9,4.3,7.2,2,9.3,7,10]
 
x = tiempo
y = nota
 
x = mean_data = np.array(x)
X=x[:,np.newaxis]
 
while True:
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    mlr=MLPRegressor(solver="lbfgs",alpha=1e-5,hidden_layer_sizes=(3,3), random_state=1)
    mlr.fit(X_train, y_train)
    print(mlr.score(X_train, y_train))
    if mlr.score(X_train,y_train) > 0.95:
        break
 
print("Basándonos en exámenes anteriores, vas a sacar aprox: ")
print(mlr.predict(np.array(70).reshape(1, 1)))