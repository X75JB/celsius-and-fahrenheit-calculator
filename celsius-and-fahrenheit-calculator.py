#A celsius and fahrenheit calculator
#Jackson Blackman
#21-11-2022

from tkinter import *

def convert():
  if fahrenheit.get() == '':
    c = float(celsius.get())
    f = 1.8*c+32
    fahrenheit.insert(END, str(f))
  elif celsius.get() == '':
    f = float(fahrenheit.get())
    c = (f-32)/1.8
    fahrenheit.insert(END, str(f))

window = Tk()
window.geometry('500x400')

Label(text = 'The temp in celsius: ').place(x = 10, y = 10)

celsius = Entry(window)
celsius.place(x = 200, y = 10)

Label(text = 'The temp in fahrenheit: ').place(x = 10, y = 60)

fahrenheit = Entry(window)
fahrenheit.place(x = 200, y = 60)

Button(window, text = 'Convert', command = convert).place(x = 100, y = 100)
