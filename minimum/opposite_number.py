import keras
from  keras.layers import Dense
model =  keras.models.Sequential()
model.add(Dense(1, input_shape=(1,)))
model.compile(loss='mse', optimizer='adam')

import numpy as np
data_input  = np.random.normal(size=100000)
data_label  =-(data_input)

model.layers[0].get_weight()

model.fit(data_inp, label_inp)

model.predict([2,5])

model.layers[0].get_weight()