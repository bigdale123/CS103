import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
def histogram():
    #read image
    #img = cv2.imread("grayscale_image.png",1)
    img = cv.imread("grayscale_image.png",1)
    cv.imshow('grayscale', img)
    print(img.shape)
    bins = np.zeros(256, np.int32)
    for i in range(0,img.shape[0]):
        for j in range (0,img.shape[1]):
            value = img[i,j]
            bins[value]+=1
    # plotting the points
    plt.plot(bins)
    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
    # giving a title to my graph
    plt.title(' graph exercise 103!')
    # function to show the plot
    plt.show()

def test_function(n):
    img = cv.imread("grayscale_image.png",0)
    cv.imshow("Grayscale Image",img)
    height,width = img.shape

    img2 = np.zeros((height,width))

    for i in range(height):
        for j in range(width):
            if img[i,j]<=n:
                img2[i,j]=0
            else:
                img2[i,j]=255
    cv.imshow("Binary Image",img2)
    cv.waitKey(5000)

test_function(200)
#histogram()
