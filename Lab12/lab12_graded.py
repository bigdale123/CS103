import cv2

def removeRedEye():
    img = cv2.imread("lab12_image.png",1)
    height,width,channels = img.shape
    print(img)
    print(img[50,50,0])
    print(img[50,50,1])
    print(img[50,50,2])


    for i in range(height):
        for j in range(width):
            if img[i,j,0] < 20 and img[i,j,1] < 20 and img[i,j,2] > 0:
                img[i,j,2] = 0

    cv2.imshow("Corrected Image",img)
    cv2.waitKey(0)


removeRedEye()
