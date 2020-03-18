#!/usr/bin/python
# -*- coding: utf-8 -*-
import pathlib
 
path = pathlib.Path('music.mp3')
print(path.exists()) # True
print(path.is_file()) # True 
from tkinter import Tk, Frame, BOTH
 
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="green")   
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Окно")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place(x=50, y=50)
        
def main():
    root = Tk()
    root.geometry("800x600+100+10")
    app = Example(root)
    root.mainloop()  
 
if __name__ == '__main__':
    main()
