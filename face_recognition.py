import cv2

face_cascade = cv2.CascadeClassifier('C:/users/user/appdata/local/programs/python/python39/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/users/user/appdata/local/programs/python/python39/haarcascade_eye.xml')

get = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while(1) :
    ret, cam = get.read()
    gray = cv2.cvtColor(cam, cv2.COLOR_BGR2GRAY)
    
    face = face_cascade.detectMultiScale(gray, 1.1, 2)
    for x,y,w,h in face :
        cv2.rectangle(cam, (x ,y), (x+w, y+h), (0, 255,0), 3)
    
    eye = eye_cascade.detectMultiScale(gray, 1.1, 2)
    for x,y,w,h in eye :
        cv2.rectangle(cam, (x, y), (x+w, y+h), (255, 0, 255), 3)
    
    frame = cv2.flip(cam, 2)
    cv2.imshow('my camera', frame)
    k = cv2.waitKey(5) & 0xFF
    if k == ord('q'):
        get.release()
        cv2.destroyAllWindows()
        break
    
