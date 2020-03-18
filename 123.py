from tkinter import *
import time
def tick():
    label.after(200, tick)
    label['text'] = time.strftime('%H:%M:%S')
def button_clicked():
    label2['text']=label['text']
    return

root=Tk()
label = Label(font='sans 20')
label2 = Label(font='sans 20')
label2['text'] = "qwert"
label.pack()
label.after_idle(tick)
label2.pack()
label2.after_idle(tick)
button = Button(root, command=button_clicked )
button['text']="Заморозить время"
button.pack()
root.mainloop()
