## Load data
import pickle
from pathlib import Path
import numpy as np
import math
import csv

training_file = '/data/traffic-signs-data/train.p'
validation_file = '/data/traffic-signs-data/valid.p'
testing_file = '/data/traffic-signs-data/test.p'

with open(training_file, mode='rb') as f:
    train = pickle.load(f)
with open(validation_file, mode='rb') as f:
    valid = pickle.load(f)
with open(testing_file, mode='rb') as f:
    test = pickle.load(f)

X_train, y_train = train['features'], train['labels']
X_valid, y_valid = valid['features'], valid['labels']
X_test, y_test = test['features'], test['labels']

#load mappings from label number to label name
signNames = {}
with open('/data/traffic-signs-data/sign_names.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         signNames[row['ClassId']]=row['SignName']


 ## Basic Stats
 n_train = len(X_train)
n_validation = len(X_valid)
n_test = len(X_test)

image_shape = X_train[0].shape

# Number of unique labels/classes
n_classes = len(set(y_train))

print("Number of training examples =", n_train)
print("Number of validation examples =", n_validation)
print("Number of testing examples =", n_test)
print("Image data shape =", image_shape)
print("Number of classes =", n_classes)

# Class distribution
import random
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
%matplotlib inline
plt.rcParams['figure.figsize'] = (7,7)

#visualize label distribution
plt.subplot(1,2,1).hist(y_train,43);
plt.xlim(0,42)
plt.title('Training Data Labels');
plt.subplot(1,2,2).hist(y_test,43);
plt.title('Testing Data Labels');
plt.xlim(0,42)
plt.tight_layout();

# visualize images
plt.subplots_adjust(hspace=0.1, wspace=0.1, bottom=0.1)

def get_random_images(images, how_many):
     rnd = random.sample(range(len(X_train)), how_many)
     return images[rnd]

def plot_images(images, rows, cols):
    """Samples images randomly"""
    gs = gridspec.GridSpec(rows, cols, top=1.0, bottom=.0, right=.7, left=0., hspace=0.3,
                           wspace=0.1)

    for index, g in enumerate(gs):
        ax = plt.subplot(g)
        img = images[index]
        ax.imshow(img)
        plt.imshow(img, cmap=plt.get_cmap('gray'))
        ax.set_xticks([])
        ax.set_yticks([])

    plt.show()

plot_images(get_random_images(X_train, 90), 9, 10)

# view sequential images
# let's also display some consecutive images
plot_images(X_train, 10,10)
