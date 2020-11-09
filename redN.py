import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

from keras.models import Sequential
from keras.layers import Dense, Activation, Input, Dropout, Convolution2D, MaxPooling2D, Flatten

#Data
data = pd.read_excel('./data/dataexc.xlsx')
#print(data.sample(5))
print(data.shape)
#print(data.iloc[0:6].values)

def extract_inputs():
    return data.iloc[:,0:7].values

def extract_outputs():
    return data.iloc[:,7:8].values

class Neural_net():
    def __init__(self):
        trainning_data = extract_inputs()
        target_data = extract_outputs()
        model = Sequential()
        model.add(Dense(150,input_dim=7,activation='relu'))
        model.add(Dense(130,activation='sigmoid'))
        model.add(Dense(100,activation='sigmoid'))
        model.add(Dense(50,activation='sigmoid'))
        model.add(Dense(40,activation='sigmoid'))
        model.add(Dense(25,activation='sigmoid'))
        model.add(Dense(1,activation='sigmoid'))
        model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
        model.fit(trainning_data,target_data,epochs=1000)
        self.model = model
        print(a)
    def prediction(self,predictionData):
        #Las predicciones no son totalmente malas
        #predictionData = np.array([[1,10,40,1.1,80,30,12]])
        a = self.model.predict(predictionData)
        return a
