from tkinter import * 
window = Tk()
window.title("Test")
window.geometry("350x200")

def click():
    ref = "Welcome " + txt.get()
    lbl.configure(text = ref)

lbl = Label(window, text = "Hello", font=("Arial Bold", 50))
lbl.grid(column = 0, row = 0)

btn = Button(window, text = "Change title", command = click)
btn.grid(column = 3, row = 0)


txt = Entry(width = 10)
txt.grid(column = 2, row = 0)

lbl2 = Label(window, text = "1+1 = ?")
lbl2.grid(column = 0, row = 1)

txt2 = Entry(width = 10)
txt2.grid(column = 1, row = 1)

def sumbit():
    if txt2.get() == "2":
        lbl2.configure(text = "Corect!")
    else:
        lbl2.configure(text = "Incorect")


btn2 = Button(window, text = "Sumbit", command = sumbit)
btn2.grid(column = 2, row = 1)


window.mainloop()
