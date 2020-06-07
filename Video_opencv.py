import cv2

cam = cv2.VideoCapture("video.mkv")# your video path or name at the palce of 'video.mkv'

while True:
    rel, frame = cam.read()
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
