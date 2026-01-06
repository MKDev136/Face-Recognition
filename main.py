from tkinter import *
from settings import *
from face_train import Train
from face_recognition import Recognition
from datas import PEOPLE

class App:
    def __init__(self):
        
        self.w = Tk()
        self.w.geometry(f"{WIDTH}x{HEIGHT}")
        self.w.resizable(False, False)
        self.w.title("Apps Reco")

        self.name = ""

    def train(self):
        self.name = self.name_file.get()
        if not self.name in PEOPLE:
            Train(self.name).run()
        else:
            print("Name Already taken")

    def reco(self):
        recognition = Recognition()
        recognition.run()

    def title(self):
        self.title_frame = Frame(self.w, background="purple", width=WIDTH, height=100)
        self.title_frame.pack()

        title = Label(self.title_frame, text="APPS VERIFICATION", bg="black", fg="white", width=75, height=2, font=50)
        title.pack()

    def face_app(self):
        self.btn_frame = Frame(self.w, bg="black", width=WIDTH, height=400)
        self.btn_frame.pack(expand=True)
        self.btn_frame.grid_propagate(False)

        # Center grid
        self.btn_frame.grid_rowconfigure(0, weight=1)
        self.btn_frame.grid_rowconfigure(1, weight=1)
        self.btn_frame.grid_columnconfigure(0, weight=1)

        self.name_file = Entry(self.btn_frame, textvariable=self.name)
        self.name_file.place(x=250, y=20)
        self.train = Button(
            self.btn_frame,
            text="New user",
            font=("Arial", 24),
            padx=60,
            pady=30,
            command=self.train
        )
        self.train.grid(row=0, column=0)

        self.recognition = Button(
            self.btn_frame,
            text="Recognition",
            font=("Arial", 24),
            padx=60,
            pady=30,
            command=self.reco
        )
        self.recognition.grid(row=1, column=0)

    def run(self):
        self.title()
        self.face_app()
        
        self.w.mainloop()

if __name__ == "__main__":
    App().run()
