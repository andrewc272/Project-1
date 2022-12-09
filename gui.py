from tkinter import *
from controller import *

class GUI:
    def __init__(self, window):
        self.window = window

        self.frame_first = Frame(self.window)
        self.label_first = Label(self.frame_first, text='First Name')
        self.entry_first = Entry(self.frame_first, width=40)
        self.label_first.pack(padx=5, side='left')
        self.entry_first.pack(padx=15, side='right')
        self.frame_first.pack(anchor='w', pady=10)

        self.frame_second = Frame(self.window)
        self.label_second = Label(self.frame_second, text='Last Name')
        self.entry_second = Entry(self.frame_second, width=40)
        self.label_second.pack(padx=5, side='left')
        self.entry_second.pack(padx=15, side='right')
        self.frame_second.pack(anchor='w', pady=10)

        self.frame_third = Frame(self.window)
        self.label_third = Label(self.frame_third, text='Street Address')
        self.entry_third = Entry(self.frame_third, width=40)
        self.label_third.pack(padx=5, side='left')
        self.entry_third.pack(padx=15, side='right')
        self.frame_third.pack(anchor='w', pady=10)

        self.frame_forth = Frame(self.window)
        self.label_forth = Label(self.frame_forth, text='Voter ID')
        self.entry_forth = Entry(self.frame_forth, width=40)
        self.label_forth.pack(padx=5, side='left')
        self.entry_forth.pack(padx=15, side='right')
        self.frame_forth.pack(anchor='w', pady=10)

        canidates = get_candidates()
        self.frame_operation = Frame(self.window)
        self.label_operation = Label(self.frame_operation, text='Choose a Candidate\t')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_candidate1 = Radiobutton(self.frame_operation, text=canidates[0], variable=self.radio_1, value=1)
        self.candidate2 = Radiobutton(self.frame_operation, text=canidates[1], variable=self.radio_1, value=2)
        self.label_operation.pack(side='left', padx=5)
        self.radio_candidate1.pack(side='left')
        self.candidate2.pack(side='left')
        self.frame_operation.pack(anchor='w', pady=10)

        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result)
        self.label_result.pack(pady=10)
        self.frame_result.pack()

        self.frame_button = Frame(self.window)
        self.button_compute = Button(self.frame_button, text='VOTE', command=self.vote)
        self.button_compute.pack(pady=10)
        self.frame_button.pack()

    def vote(self):
        first_name = self.entry_first.get()
        last_name = self.entry_second.get()
        street_address = self.entry_third.get()
        voter_ID = self.entry_forth.get()
        vote = self.radio_1.get()

        message = count_vote([first_name, last_name, street_address, voter_ID], vote)
        if message != 'Please select someone to vote for':
            self.clear()
        self.label_result.config(text=message)



    def clear(self):
        self.entry_second.delete(0, END)
        self.entry_third.delete(0, END)
        self.entry_forth.delete(0, END)
        self.entry_first.delete(0, END)
        self.radio_1.set(0)
