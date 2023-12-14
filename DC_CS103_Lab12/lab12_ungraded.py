import math
import cv2 as cv

def radDegree(f,s):
    if s.lower() == "radian":
        print(str(f)+" pi radians is equal to "+str(f*180)+" degrees.")
    elif s.lower() == "degree":
        print(str(f)+" degrees is equal to "+str(f/180)+" pi radians.")

def grayscale2binary(n):
    img = cv.imread("grayscale_image.png",0)
    cv.imshow("Grayscale Image",img)
    height,width = img.shape

    for i in range(height):
        for j in range(width):
            if img[i,j]<=n:
                img[i,j]=0
            else:
                img[i,j]=255
    cv.imshow("Binary Image",img)
    cv.waitKey(0)





radDegree(45,"degree")
grayscale2binary(200)
