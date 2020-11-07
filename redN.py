import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#from sklearn.model_selection import train_test_split
#from sklearn.metrics import classification_report, accuracy_score

#from keras.models import Sequential
#from keras.layers import Dense, Activation, Input, Dropout, Convolution2D, MaxPooling2D, Flatten

#Data
data = pd.read_excel('./data/dataexc.xlsx')
data = data.rename_axis(None
                        )
print(data.sample(5))
print(list(data))

b = data['nCoches']
print(b[0:5])
