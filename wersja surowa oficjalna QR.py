#Autor: Damian Popławski
from tkinter import *
from tkinter import messagebox
import pyqrcode
import os

window = Tk()
window.title("QRCode ver. 3.0")


# coed generation
def generate():
    if len(subject.get()) != 0:
        global myQr
        myQr = pyqrcode.create(subject.get())
        qrImage = myQr.xbm(scale=6)
        global photo
        photo = BitmapImage(data=qrImage)
    else:
        messagebox.showinfo("Błąd!", "Wpisz zawartość kodu QR")
    try:
        showCode()
    except:
        pass


# code showing
def showCode():
    global photo
    notificationLabel.config(image=photo)
    subLabel.config(text="Zawartość kodu: " + subject.get())


def save():
    # folder to save all the codes
    dir = path1 = os.getcwd() + "\\Tu jest twój kod"

    # create a folder is it doesn't exist
    if not os.path.exists(dir):
        os.makedirs(dir)

    try:
        if len(name.get()) != 0:
            qrImage = myQr.png(os.path.join(dir, name.get() + ".png"), scale=6)
        else:
            messagebox.showinfo("Błąd!", "QR musi mieć nazwę!")
    except:
        messagebox.showinfo("Błąd", "Najpierw wygeneruj kod!")


lab1 = Label(window, text="Wpisz treść kodu QR", font=("Helvetica", 12))
lab1.grid(row=0, column=0, sticky=N + S + E + W)

lab2 = Label(window, text="Wybierz nazwę pliku", font=("Helvetica", 12))
lab2.grid(row=1, column=0, sticky=N + S + E + W)

subject = StringVar()
subjectEntry = Entry(window, textvariable=subject, font=("Helvetica", 12))
subjectEntry.grid(row=0, column=1, sticky=N + S + E + W)

name = StringVar()
nameEntry = Entry(window, textvariable=name, font=("Helvetica", 12))
nameEntry.grid(row=1, column=1, sticky=N + S + E + W)

createButton = Button(window, text="Wygeneruj kod QR", font=("Helvetica", 12), width=15, command=generate)
createButton.grid(row=0, column=3, sticky=N + S + E + W)

notificationLabel = Label(window)
notificationLabel.grid(row=2, column=1, sticky=N + S + E + W)

subLabel = Label(window, text="")
subLabel.grid(row=3, column=1, sticky=N + S + E + W)

showButton = Button(window, text="Zapisz jako PNG", font=("Helvetica", 12), width=15, command=save)
showButton.grid(row=1, column=3, sticky=N + S + E + W)

# Making responsive layout:
totalRows = 3
totalCols = 3

for row in range(totalRows + 1):
    window.grid_rowconfigure(row, weight=1)

for col in range(totalCols + 1):
    window.grid_columnconfigure(col, weight=1)

# looping the GUI
window.mainloop()
