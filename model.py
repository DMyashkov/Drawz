import numpy as np
from sklearn.model_selection import train_test_split
from os import walk, getcwd
import h5py
from dynamic import txt_name_list, mypath

print(txt_name_list)

x_train = []
x_test = []

y_train = []
y_test = []

xtotal = []
ytotal = []

slice_train = int(80000/len(txt_name_list))  ###Setting value to be 80000 for the final dataset
i = 0
seed = np.random.randint(1, 10e6)

##Creates test/train split with quickdraw data
for txt_name in txt_name_list:
    txt_path = mypath + txt_name
    x = np.load(txt_path)
    x = x.astype('float32') / 255.    ##scale images
    y = [i] * len(x)
    np.random.seed(seed)
    np.random.shuffle(x)
    np.random.seed(seed)
    np.random.shuffle(y)
    x = x[:slice_train]
    y = y[:slice_train]
    if i != 0: 
        xtotal = np.concatenate((x,xtotal), axis=0)
        ytotal = np.concatenate((y,ytotal), axis=0)
    else:
        xtotal = x
        ytotal = y
    i += 1
x_train, x_test, y_train, y_test = train_test_split(xtotal, ytotal, test_size=0.2, random_state=42)

print(x_train.shape)

# Convert the target labels to one-hot encoded vectors
from keras.utils import to_categorical
num_classes = len(txt_name_list)
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

# ##Saves this out as hdf5 format
# data_to_write = x_test
# with h5py.File('x_test.h5', 'w') as hf:
#     hf.create_dataset("name-of-dataset",  data=data_to_write)
# data_to_write = x_train
# with h5py.File('x_train.h5', 'w') as hf:
#     hf.create_dataset("name-of-dataset",  data=data_to_write)
# data_to_write = y_test
# with h5py.File('y_test.h5', 'w') as hf:
#     hf.create_dataset("name-of-dataset",  data=data_to_write)
# data_to_write = y_train
# with h5py.File('y_train.h5', 'w') as hf:
#     hf.create_dataset("name-of-dataset",  data=data_to_write)


from keras.models import Sequential
from keras.layers import Dense, Flatten

model = Sequential()
# Reshape the training data
print(x_train.shape)
x_train = np.reshape(x_train, (x_train.shape[0], 28, 28, 1))

model.add(Flatten(input_shape=(28, 28, 1)))
model.add(Dense(128, activation='relu'))
num_classes = len(txt_name_list)
model.add(Dense(num_classes, activation='softmax'))


model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5, batch_size=32)

model.save('model.h5')
