#!/usr/bin/env python3
"""
Binary image creation
"""

import numpy as np
import os
import matplotlib.pyplot as plt


def create_folder(folder_path):
	try:
		os.makedirs(folder_path)
	except OSError as e:
		print(e)

def binary_img(img_size=(512,512)):
	assert img_size is not None, "Need a integer 2-tuple"
	M = np.random.randint(1,256,img_size)
	M[M<150] = 0
	M[M>=150] = 1

	return M


if __name__=="__main__":
	image_size = [(1,1), (10,10), (50,50), (100,100), (250,250), (500,500), (750, 750), (1000,1000),(2000,2000)]
	folder_name = 'output1'
	create_folder(folder_name)
	path_name = os.path.join(os.getcwd(), folder_name)
	for i, item in enumerate(image_size):
		img = binary_img(item)
		plt.imshow(img, 'gray')
		plt.title('Image Size = {0}'.format(img.shape))
		plt.pause(2)
		f = path_name +'/' + str(i+1) + '.png'
		plt.savefig(f)
	plt.show(block=False)
	plt.close()
