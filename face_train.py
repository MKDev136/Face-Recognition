import cv2 as cv
import numpy as np
import os
from datas import PEOPLE


class Train:
    def __init__(self, name):
        self.name = name

        PEOPLE.append(self.name)

        DATA_DIR = "camera_faces"
        os.makedirs(DATA_DIR, exist_ok=True)

        self.haar = cv.CascadeClassifier("./Face/haarcascade_frontalface_default (1).xml")

        self.features = []
        self.labels = []

        self.cap = cv.VideoCapture(0)

        self.current_person = PEOPLE.index(self.name)
        self.samples_per_person = 500
        self.count = 0

    def save_datas(self):
        with open("./Face/datas.py", "w", encoding="utf-8") as f:
                    f.write("PEOPLE = [\n")
                    for p in PEOPLE:
                        f.write(f"    {repr(p)},\n")
                    f.write("]\n")

    def train_model(self):
        labels = np.array(self.labels, dtype=np.int32)

        face_recognizer = cv.face.LBPHFaceRecognizer_create()
        face_recognizer.train(self.features, labels)

        face_recognizer.save("face_trained.yml")
        np.save("features.npy", self.features)
        np.save("labels.npy", labels)

        self.save_datas()

        print("Training completed and saved.")

    def draw_rects(self, gray, frame):
        faces = self.haar.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
                face_roi = gray[y:y+h, x:x+w]
                face_roi = cv.resize(face_roi, (200, 200))
                cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

                if self.count < self.samples_per_person:
                    self.features.append(face_roi)
                    self.labels.append(self.current_person)
                    self.count += 1
                    print(f"Captured {self.count}/{self.samples_per_person} for {PEOPLE[self.current_person]}")
        
        cv.putText(
            frame,
            f"Person: {PEOPLE[self.current_person]} ({self.count}/{self.samples_per_person})",
            (20, 30),
            cv.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    def run(self):
        print("Press N for next person, Q to quit")

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            frame = cv.flip(frame, 1)
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            self.draw_rects(gray, frame)


            cv.imshow("Training", frame)

            key = cv.waitKey(1) & 0xFF
            if key == ord('n'):
                self.current_person += 1
                self.count = 0
                if self.current_person >= len(PEOPLE):
                    break
            elif key == ord('q'):
                break

        self.cap.release()
        cv.destroyAllWindows()

        self.train_model()
