import cv2 as cv
img1 = cv.imread(r"D:\Python\Python OpenCv\NIrajPhotoShoot.jpeg",1) # here r is used to produce raw string error hatane ke liye use kiya
print(img1)
cv.imshow("originalwindow",img1)
# cv.resize(img1,(1280,700)) # width * height tupple in resizing | it must return in order to update image so i should write like

img1 = cv.resize(img1,(1280,700)) # now my image is successfully resized
img2 = cv.imread(r"D:\Python\Python OpenCv\NIrajPhotoShoot.jpeg",0) # 0 read image as gray scale
img3 = cv.imread(r"D:\Python\Python OpenCv\NIrajPhotoShoot.jpeg",-1) # -1 increases the saturation value


 
cv.imshow("Resized image",img1)
cv.imshow("Gray Scale Image",img2)
cv.imshow("Image with more saturation",img3)
cv.waitKey()
cv.destroyAllWindows()
