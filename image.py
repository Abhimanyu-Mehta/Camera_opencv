import cv2

img = cv2.imread('image.png', -1)# your image path or name at te palce of 'image.png'

cv2.imshow("image", img)
k = cv2.waitKey(0)
if k == 27:
   cv2.destroyAllWindows()
elif k == ord('s'):
   cv2.imwrite('forest.png', img)
cv2.destroyAllWindows()
#To print text on the image view "Text_opencv" file 
