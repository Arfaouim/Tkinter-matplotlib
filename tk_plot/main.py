# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:26:15 2021

@author: arfao
"""

#------- start
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np

class MyWindow:
    def __init__(self, win):
        x0, xt0, y0 = 10, 100, 50
        #---- First label and entry -------
        self.lbl0 = Label(win, text='Initial instant')
        self.lbl0.config(font=('Arial', 9))
        self.lbl0.place(x=x0, y=y0)
        self.t0 = Entry()
        self.t0.place(x=xt0, y=y0)
        self.t0.insert(END, str(0))
        self.t_0 = float(self.t0.get())

        #---- Second label and entry -------
        self.lbl1 = Label(win, text='Final instant')
        self.lbl1.config(font=('Arial', 10))
        self.lbl1.place(x=x0, y=y0 + 40)
        self.t1 = Entry()
        self.t1.place(x=xt0, y=y0 + 40)
        self.t1.insert(END, str(1))
        self.t_1 = float(self.t1.get())
        
        #---- a entry -------
        self.lbl2 = Label(win, text='a')
        self.lbl2.config(font=('Arial', 10))
        self.lbl2.place(x=x0, y=y0 + 80)
        self.a1 = Entry()
        self.a1.place(x=xt0, y=y0 + 80)
        self.a1.insert(END, str(1))
        self.a = float(self.a1.get())

        #---- Compute button -------
        self.btn = Button(win, text='Compute')
        self.btn.bind('<Button-1>', self.plot)
        self.btn.place(x=xt0, y=y0 + 120)

        self.figure = Figure(figsize=(4.5, 3), dpi=100)

        #---- subplot 1 -------
        self.subplot1 = self.figure.add_subplot(211)
        self.subplot1.set_xlim(self.t_0, self.t_1)

        #---- subplot 2 -------
        # self.subplot2 = self.figure.add_subplot(212)
        # self.subplot2.set_xlabel('$Time(s)$', fontsize=11)
        # self.subplot2.set_xlim(self.t_0, self.t_1)

        #---- Show the plot-------
        self.plots = FigureCanvasTkAgg(self.figure, win)
        self.plots.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=0)

    def data(self):
        self.t_0 = float(self.t0.get())
        self.t_1 = float(self.t1.get())
        t = np.linspace(self.t_0, self.t_1, 100)
        func1 = self.a*t**0.5
        return t, func1

    def plot(self, event):
        t, func1 = self.data()
        self.t_0 = float(self.t0.get())
        self.t_1 = float(self.t1.get())
        self.subplot1.set_xlim(self.t_0, self.t_1)
        self.subplot1.plot(t, func1, 'r', lw=2.5)
        self.plots.draw()

if  __name__=="__main__":

    window = Tk()
    mywin = MyWindow(window)
    window.title('My model')
    window.geometry("800x600+10+10")
    window.mainloop()