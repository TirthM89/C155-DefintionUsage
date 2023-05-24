from tkinter import *

root = Tk()
root.title("Dictionary")
root.geometry("600x400")
root.configure(bg = "skyblue")

labelm = Label(root, bg = "skyblue")
labeli = Label(root, bg = "skyblue")
labelt = Label(root, bg = "skyblue")

dictionary = {"mutable":"Values that can be changed, like a list.",
              "immutable":"Values that can not be changed, like tuples.",
              "tkinter":"It is the GUI library of Python"}

def mut():
    labelm["text"] = dictionary["mutable"]
    
def imm():
    labeli["text"] = dictionary["immutable"]
    
def tki():
    labelt["text"] = dictionary["tkinter"]
    
btn1 = Button(root, text = "Definition of Mutable", command = mut, bg = "yellow")
btn1.place(relx = 0.48, rely = 0.2, anchor = CENTER)
labelm.place(relx = 0.51, rely = 0.3, anchor = CENTER)

btn2 = Button(root, text = "Definition of Immutable", command = imm,  bg = "yellow")
btn2.place(relx = 0.5, rely = 0.4, anchor = CENTER)
labeli.place(relx = 0.47, rely = 0.5, anchor = CENTER)

btn3 = Button(root, text = "Definition of tkinter", command = tki, bg = "yellow")
btn3.place(relx = 0.53, rely = 0.6, anchor = CENTER)
labelt.place(relx = 0.49, rely = 0.7, anchor = CENTER)

root.mainloop()