__author__ = 'Per-Arne'
import os
import random
import math
import numpy as np
import mnist_loader
import Network
from PIL import Image


paths = {
    'faces': './faces',
}

desired_output = {
    'up': 0,
    'left': 1,
    'right': 2,
    'straight': 3
}

image_type = '2' # either null, 2 or 4
image_size = 960
training_percent = 0.80





def getFiles(type):

    ending = ""
    if type is not None:
        ending = "_" + type

    images = []

    for categories in os.listdir(paths['faces']):
        category_path = paths['faces'] + '/' + categories

        # Skip files
        if not os.path.isdir(category_path):
            continue

        for file in os.listdir(category_path):
            file_path = category_path + '/' + file

            # Split extension and file path
            split = os.path.splitext(file_path)
            file = split[0]
            ext = split[1]

            if file.endswith(ending):
                images.append(file_path)

    random.shuffle(images)
    return images

def load(files):

    # Determine how many files to use for training
    training_length = int(math.floor(len(files) * training_percent))


    # Define list which have "ALL data"
    all_pixel = []
    all_expect = []

    # Parse pixel data and expectation
    for file in files:

        # Get pixel data from file
        im = Image.open(file)
        pixelData = np.array(list(im.getdata()), dtype= np.float32)

        # Add pixe data and expectation (answer) to list
        all_pixel.append(pixelData)
        all_expect.append(desired_output[file.split("_")[1]])

    # First element to training_length   |0 ---> training_length|
    training = (np.array(all_pixel[0:training_length], dtype= np.float32), np.array(all_expect[0:training_length], dtype= np.float32))

    # From training_length to end of the array
    test = (np.array(all_pixel[training_length:len(all_pixel)], dtype= np.float32), np.array(all_expect[training_length:len(all_expect)], dtype= np.float32))

    # Dont use validation, set to test
    validation = test

    # Return data
    return (training, validation, test)

# Fetch path to all image files
files = getFiles(image_type)

# Identify size of images loaded
image_size = len(Image.open(files[0]).getdata())

tr_d, va_d, te_d = load(files)

training_data, validation_data, test_data = mnist_loader.load_data_wrapper(tr_d, va_d, te_d, image_size)

net = Network.Network([image_size, 30, 30 , 4])

net.SGD(training_data, 30, 10, 3.1, test_data=test_data)
