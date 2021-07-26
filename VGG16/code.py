from keras.datasets import cifar10
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from keras.models import load_model

(x_train_image, y_train_label), (x_test_image, y_test_label) = cifar10.load_data()

label = {
    0: "airplain",
    1: "automobile",
    2: "bird",
    3: "cat",
    4: "deer",
    5: "dog",
    6: "frog",
    7: "horse",
    8: "ship",
    9: "truck"}

model = load_model('model.h5')

predictions = model.predict(x_test_image)


def ShowImage():
    fig = plt.gcf()
    fig.set_size_inches(15, 5)
    for i in range(0, 10):
        ax = plt.subplot(2, 5, i+1)
        x = np.random.randint(50000)
        ax.imshow(x_train_image[x])
        t = y_train_label[x][0]
        title = label[t]
        ax.set_title(title)
        ax.set_xticks([])
        ax.set_yticks([])
    plt.show()


def PrintHyperparameters():
    print("hyperparameters:")
    print("batch size: 64")
    print('learning rate: '+'0.001')
    print("optimizer: "+'adam')


def ShowModel():
    model.summary()


def ShowAL():
    df = pd.read_json('history.json')
    epoch_range = range(1, 31)
    plt.subplot(1, 2, 1)
    plt.plot(epoch_range, df['accuracy'])
    plt.plot(epoch_range, df['val_accuracy'])
    plt.title('accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')

    plt.subplot(1, 2, 2)
    plt.plot(epoch_range, df['loss'])
    plt.title('loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.show()


def Test(num):
    labellist = ['plain', 'car', 'bird', 'cat',
                 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

    fig = plt.gcf()
    fig.set_size_inches(20, 5)

    plt.subplot(1, 2, 1)
    plt.bar(labellist, predictions[num])

    plt.subplot(1, 2, 2)
    plt.imshow(x_test_image[num])

    plt.show()
