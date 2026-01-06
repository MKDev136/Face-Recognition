from tkinter import *
from settings import *
from paint import PaintApp

class Apps():
    def __init__(self):
        
        self.w = Tk()
        self.w.geometry(f"{WIDTH}x{HEIGHT}")
        self.w.resizable(False, False)
        self.w.title("Apps")

        self.name = ""

    def train(self):
        self.name = self.name_file.get()
        print(self.name)

    def title(self):
        self.title_frame = Frame(self.w, background="purple", width=WIDTH, height=100)
        self.title_frame.pack()

        title = Label(self.title_frame, text="Apps", bg="black", fg="white", width=75, height=2, font=50)
        title.pack()

    def face_app(self):
        self.btn_frame = Frame(self.w, bg="black", width=WIDTH, height=400)
        self.btn_frame.pack(expand=True)
        self.btn_frame.grid_propagate(False)

        for r in range(2):
            self.btn_frame.grid_rowconfigure(r, weight=1)
        for c in range(3):
            self.btn_frame.grid_columnconfigure(c, weight=1)

        buttons = [
            ("Paint", PaintApp),
            ("App 2", None),
            ("App 3", None),
            ("App 4", None),
            ("App 5", None),
            ("App 6", None)
        ]

        for index, (text, cmd) in enumerate(buttons):
            row = index // 3
            col = index % 3
            btn = Button(
                self.btn_frame,
                text=text,
                font=("Arial", 24),
                padx=40,
                pady=30,
                command=cmd
            )
            btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

    def run(self):
        self.title()
        self.face_app()
        
        self.w.mainloop()
