import tkinter
from tkinter import *
from tkinter import messagebox


def proceed(v):
    if v == 1:
        click1()
    elif v == 2:
        click2()


def weight_status(bmi):
    if bmi < 18.5:
        status = 'underweight!'
    elif 18.5 <= bmi < 25:
        status = 'healthy!'
    elif 25 <= bmi < 30:
        status = 'overweight!'
    else:
        status = 'obese!'
    return status


def american():
    foot = int(e.get())
    inches = int(e2.get())
    pound = int(e3.get())
    if inches > 12:
        foot = foot + inches // 12
        inches = inches - (inches // 12) * 12
    inches = inches + foot * 12
    bmi = 703 * pound / (inches ** 2)
    stat = weight_status(bmi)
    messagebox.showinfo('Result!', 'Your BMI is ' + str(round(bmi, 2)) + '\nYou are ' + stat)


def metric():
    cm = int(e.get())
    kg = int(e2.get())
    m = cm / 100
    bmi = kg / (m ** 2)
    stat = weight_status(bmi)
    messagebox.showinfo('Result!', 'Your BMI is ' + str(round(bmi, 2)) + '\nYou are ' + stat)


def click1():
    label1 = tkinter.Label(frame, text='Height:')
    label1.grid(row=3, column=0)
    label2 = tkinter.Label(frame, text='Feet:')
    label2.grid(row=4, column=0)
    label3 = tkinter.Label(frame, text='Inches:')
    label3.grid(row=4, column=1)

    global e
    e = tkinter.Entry(frame, borderwidth=2, width=20)
    e.grid(row=5, column=0)
    global e2
    e2 = tkinter.Entry(frame, borderwidth=2, width=20)
    e2.grid(row=5, column=1)

    label4 = tkinter.Label(frame, text=' ')
    label4.grid(row=6, column=0)
    label5 = tkinter.Label(frame, text='Weight(lbs):')
    label5.grid(row=7, column=0)

    global e3
    e3 = tkinter.Entry(frame, borderwidth=2, width=20)
    e3.grid(row=8, column=0)

    label6 = tkinter.Label(frame, text=' ')
    label6.grid(row=9, column=0)

    b = tkinter.Button(frame, text='Calculate BMI', padx=20, pady=3, command=american)
    b.grid(row=10, column=2)

    label7 = tkinter.Label(frame, text=' ')
    label7.grid(row=11, column=0)


def click2():
    label2 = tkinter.Label(frame, text='Height(cm):')
    label2.grid(row=12, column=0)
    label3 = tkinter.Label(frame, text='Weight(kg):')
    label3.grid(row=13, column=0)

    global e
    e = tkinter.Entry(frame, borderwidth=2, width=20)
    e.grid(row=12, column=1)
    global e2
    e2 = tkinter.Entry(frame, borderwidth=2, width=20)
    e2.grid(row=13, column=1)

    label4 = tkinter.Label(frame, text=' ')
    label4.grid(row=14, column=0)

    b = tkinter.Button(frame, text='Calculate BMI', padx=20, pady=3, command=metric)
    b.grid(row=15, column=2)


window = tkinter.Tk()
window.title('BMI Calculator')
frame = tkinter.Frame(window, padx=5, pady=5)
frame.pack(padx=10, pady=10)

var = tkinter.IntVar()

tkinter.Radiobutton(frame, text='American units', variable=var, value=1).grid(row=0, column=0)
tkinter.Radiobutton(frame, text='Metric units', variable=var, value=2).grid(row=0, column=1)

b2 = tkinter.Button(frame, text='Proceed', padx=30, pady=3, command=lambda: proceed(var.get()))
b2.grid(row=2, column=2)

window.mainloop()