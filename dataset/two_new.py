import cv2
import os
# f = open('./check/read.txt', 'r')
for i in range(1,901):
    if os.path.exists("./masks/" + str(i) + ".mask.0.png"):
        img = cv2.imread("./masks/" + str(i) + ".mask.0.png")
        GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, th1 = cv2.threshold(GrayImage, 50, 255, cv2.THRESH_BINARY)
        cv2.imwrite("./annotations/"+str(i)+".png",th1)
print("finish")





