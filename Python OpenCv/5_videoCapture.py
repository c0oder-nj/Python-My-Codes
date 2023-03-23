import cv2 as cv

cap = cv.VideoCapture(r"E:\Naruto\season 4\[Toonworld4all] Naruto - 082 [480p BD x264 Multi Audio] ESub.mkv")

print("cap",cap)

while True:
    ret,frame = cap.read() # it returns two values first one is boolean value which i stored in ret and second one is my image i.e. frame
    cv.resize(frame,(700,600))
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY) # in order to get the grey scale image
    cv.imshow("frame is ",frame)
    cv.imshow("gray frame is",gray)
    k = cv.waitKey(25)

    # in order to break the loop or stoping the video playback
    if k == ord('q'):
        break

cap.release() # inorder to release captured vidoe
cv.destroyAllWindows()