import cv2 as cv
import numpy as np
from datas import PEOPLE
from apps import Apps

class Recognition:
    def __init__(self):
        
        self.haar = cv.CascadeClassifier("./Face/haarcascade_frontalface_default (1).xml")

        self.face_recognizer = cv.face.LBPHFaceRecognizer_create()
        self.face_recognizer.read("face_trained.yml")

        self.cap = cv.VideoCapture(0)
        self.apps = Apps()

        self.name = ""

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            frame = cv.flip(frame, 1)

            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            faces = self.haar.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in faces:
                face_roi = gray[y:y+h, x:x+w]
                face_roi = cv.resize(face_roi, (200, 200))
                label, confidence = self.face_recognizer.predict(face_roi)

                self.name = PEOPLE[label] if confidence < 100 else "Unknown"

                cv.putText(
                    frame,
                    f"{self.name} ({int(confidence)})",
                    (x, y - 10),
                    cv.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 255, 0),
                    2
                )
                cv.putText(
                    frame,
                    f"User detected, Press N to access APPS",
                    (x-100, y - 50),
                    cv.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 255, 255),
                    2
                )
                cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            cv.imshow("Face Recognition", frame)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break
            if cv.waitKey(1) & 0xFF == ord('n') and self.name != "Unknown":
                self.apps.run()

        self.cap.release()
        cv.destroyAllWindows()
