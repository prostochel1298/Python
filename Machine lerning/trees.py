from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.datasets import mnist
from tensorflow.keras import utils
import matplotlib.pyplot as plt


(x_train_org, y_train_org), (x_test_org, y_test_org) = mnist.load_data() # Подгрузка изображения с сервера
n = 143
plt.imshow(x_train_org[n], cmap='gray')
x_train = x_train_org.reshape(x_train_org.shape[0], -1) # Изменение формы входных картинок с 28х28 на 784
                                                        # первая ось остается без изменения, остальные складываются в вектор
x_test = x_test_org.reshape(x_test_org.shape[0], -1)
x_train = x_train.astype('float32') / 255    # Изменение формы входных картинок с 28х28 на 784
x_test = x_test.astype('float32') / 255
CLASS_COUNT = 10 # Задание константы количества распознаваемых классов
y_train = utils.to_categorical(y_train_org, CLASS_COUNT) #Преобразование ответов в формат one_hot_encoding
y_test = utils.to_categorical(y_test_org, CLASS_COUNT)


model = Sequential()
model.add(Dense(800,input_dim=784,activation='relu'))
model.add(Dense(400,activation='relu'))
model.add(Dense(CLASS_COUNT, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=128, epochs=15, verbose=1) #Обучение нейорсети
model.save_weights('model.h5')
model.load_weights('model.h5')

n_rec = np.random.randint(x_test_org.shape[0])
plt.imshow(x_test_org[n_rec], cmap='gray')
plt.show()