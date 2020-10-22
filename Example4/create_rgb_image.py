#!/usr/bin/env python3
"""
Color subplot image creation
"""

import numpy as np
import matplotlib.pyplot as plt


if __name__=="__main__":
	rows, columns, channels = 100, 100, 3
	M = np.zeros((2*rows, 2*columns, channels), dtype=np.uint8)
	# (1,1) - Red
	M[:rows, :columns, 0] = 255
	# (1,2) - Blue
	M[:rows, columns:, 1] = 255
	# (2,1) - Green
	M[rows:, :columns, 2] = 255
	M[(rows+45):(rows+55), :columns, 1] = 255
	M[rows:, (columns-65):(columns-55), 1] = 255
	# (2, 2) - White
	M[rows:, columns:, :] = 255


	plt.imshow(M)
	plt.show(block=False)
	plt.pause(2)
	plt.close()