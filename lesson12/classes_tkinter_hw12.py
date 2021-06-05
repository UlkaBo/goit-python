from tkinter import *


class Screen:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x500')

        self.general_entry = Entry(self.root, width=700)
        self.general_entry.grid(row=0, column=0)
        self.general_entry.bind('<Return>', as_input)

        self.but_ok_general_entry = Button(self.root, text='ok')
        self.but_ok_general_entry.grid(row=0, column=1)
        self.but_ok_general_entry.bind('<Button-1>', as_input)

        self.but_create_rec = Button(
            self.root, text='create new record', command=open_frame_create_rec)
        self.but_create_rec.grid(row=1, column=0)

        self.frame_create_rec = Frame(self.root)

        self.but_add_phone = Button(
            self.root, text='add phone', command=open_frame_add_phone)
        self.but_add_phone.grid(row=10, column=0)

        self.frame_add_phone = Frame(self.root)

        self.but_change_bd = Button(
            self.root, text='change birthday', command=open_frame_change_bd)
        self.but_change_bd.grid(row=20, column=0)

        self.frame_change_bd = Frame(self.root)
