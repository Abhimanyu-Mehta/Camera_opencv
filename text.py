import cv2

cam = cv2.VideoCapture(0)

while True:
    rel, frame = cam.read()
    if rel == True:
        font = cv2.FONT_HERSHEY_COMPLEX
        text = str("TEXT HERE")
        frame = cv2.putText(frame, text, (10, 50), font, 1, (255, 0, 0), 4, cv2.LINE_AA)
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
