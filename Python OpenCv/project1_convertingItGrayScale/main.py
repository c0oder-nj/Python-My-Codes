import cv2 as cv
path = input(r"Enter your image path ")
# path = path
print(path)
img1 = cv.imread(path,0) # 0 as a flag for converting image into grayScale

cv.imshow("My window",img1)

# cv.waitKey() # default value is 0

# in order to save image into system
k = cv.waitKey() # default value is 0
if k==ord('s'):
    cv.imwrite('D:\Python\Python OpenCv\project1_convertingItGrayScale\outputImage\output.png',img1)
else:
    cv.destroyAllWindows()

    
