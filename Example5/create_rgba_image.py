import numpy as np
import matplotlib.pyplot as plt


if __name__=="__main__":
    rows, columns, channels = 100, 200, 3
    N = np.zeros((rows, columns, 4), dtype=np.uint8)
    N[:, :columns//2] = [255, 128, 0, 255] # orange left
    N[:, columns//2:] = [0, 0, 255, 255] # blue right

    for i in range(columns):
        for j in range(rows):
            N[j, i, channels] = i


    plt.imshow(N)
    plt.show(block=False)
    plt.pause(2)
    plt.close()

