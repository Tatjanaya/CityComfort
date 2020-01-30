import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image


def test_gray2color():
    #img = cv2.imread(filename, 0)
    img = np.loadtxt("./datas/result.txt", dtype=float)

    m_mean = np.nanmean(img)
    
    plt.figure()
    plt.imshow(img, cmap="rainbow", vmax=25, vmin=15)
    plt.colorbar()
    plt.savefig("./datas/result.png")
    plt.show()
