from gui import *

def main():
    window = Tk()
    window.title('Project 1')
    window.geometry('400x300')
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
