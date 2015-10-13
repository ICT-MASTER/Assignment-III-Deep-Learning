import os
import itertools
import time
import random
import math
from PIL import Image
import numpy as np
import mnist_loader
import network
face_path = './faces'
image_type = '4' # either null, 2 or 4
image_size = 64*60
image_size = 32*30
desired_output = {
	'up': 0,
	'left': 1,
	'right': 2,
	'straight': 3
}

def getFiles(type):

	ending = ""
	if type is not None:
		ending = "_" + type
	
	images = []

	for categories in os.listdir(face_path):
		category_path = face_path + '/' + categories
		
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
	training_length = int(math.floor(len(files) * 0.83))
	
	# Define training, validation and test item
	#training = (np.array(), np.array())
	#validation = (np.array(), np.array())
	#test = (np.array(), np.array())
	
	# Define list which have "ALL data"
	all_pixel = []
	all_expect = []

	# Parse pixel data and expectation
	for file in files:
		# Get pixel data
		im = Image.open(file)
		pixelData = np.array(list(im.getdata()), dtype= np.float32)
		
		all_pixel.append(pixelData)
		all_expect.append(desired_output[file.split("_")[1]])
		
	# Distribute items to training, validation and test
	#
	
	training = (np.array(all_pixel[0:training_length], dtype= np.float32), np.array(all_expect[0:training_length], dtype= np.float32))
	test = (np.array(all_pixel[training_length:len(all_pixel)], dtype= np.float32), np.array(all_expect[training_length:len(all_expect)], dtype= np.float32))
	validation = test
	
	return (training, validation, test)

	
		

tr_d, va_d, te_d = load(getFiles(image_type))
training_data, validation_data, test_data = mnist_loader.load_data_wrapper(tr_d, va_d, te_d)
net = network.Network([image_size, 30, 30 , 4])
net.SGD(training_data, 10000, 10, 1.0, test_data=test_data)
