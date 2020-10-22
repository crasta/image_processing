#!/usr/bin/env python3
"""
How to create an image
"""

import numpy as np
import os
import matplotlib.pyplot as plt


def create_folder(folder_path):
	try:
		os.makedirs(folder_path)
	except OSError as e:
		print(e)

def create_image(img_size):
	return np.random.randint(256, size=img_size)

if __name__=="__main__":
	image_size = [(1,1), (10,10), (50,50), (100,100), (250,250), (500,500), (750, 750), (1000,1000),(2000,2000)]
	folder_name = 'output2'
	create_folder(folder_name)
	path_name = os.path.join(os.getcwd(), folder_name)
	for idx, item in enumerate(image_size):
		M = create_image(item)
		plt.imshow(M)
		plt.title('Image Size = {0}'.format(M.shape))
		plt.pause(2)
		f = path_name +'/' + str(idx+1) + '.png'
		plt.savefig(f)
	plt.show(block=False)
	plt.close()
