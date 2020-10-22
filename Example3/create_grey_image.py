#!/usr/bin/env python3
"""
Gray image creation
"""

import numpy as np
import matplotlib.pyplot as plt
import itertools


if __name__=="__main__":
	rows, columns = 100, 200
	P = np.zeros((rows, columns), dtype=np.uint8)
	Q = np.zeros((rows, columns), dtype=np.uint8)

	x = np.arange(columns)
	y = np.arange(rows)
	for (i,j) in itertools.product(x,y):
		if (i%20) // 10 == (j%20) // 10:
			Q[j, i] = 0
		else:
			Q[j, i] = 255

	plt.imshow(Q)
	plt.show(block=False)
	plt.pause(2)
	plt.close()
