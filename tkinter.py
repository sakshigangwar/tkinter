from curses import window
from tkinter import *
window = Tk()
def send():
    send="   "+"You :" +e.get()
    txt.insert(END,"\n"+send)
    if (e.get()=="Hey"):
        txt.insert(END,"\n"+"                                       "+"sakshi : Hii ")
    elif (e.get()=="Hii"):
        txt.insert(END,"\n"+"sakshi : Hey ")
    elif (e.get()=="how are you"):
        txt.insert(END,"\n"+"                                      "+"sakshi: fine and u ")
    elif (e.get()=="i'am also fine"):
        txt.insert(END,"\n"+"                                      "+"sakshi: nice to hear ")
    elif (e.get()=="where are you"):
        txt.insert(END,"\n"+"                                      "+"sakshi:Me at Home")
    elif (e.get()=="what are you doing"):
        txt.insert(END,"\n"+"                                      "+"sakshi:nothing")
    elif (e.get()=="ok"):
        txt.insert(END,"\n"+"                                      "+"sakshi:Bye")
    else:
        txt.insert(END,"\n"+"sakshi : sorry i didn't get it ")
    e.delete(0,END)
txt=Text(window)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(window,width=100)
send=Button(window,text="Send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
window.title("CHATBOT")
window.mainloop()
