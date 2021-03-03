from tkinter import *
import tkinter as tk
import ExpressionSplitter
import ExpressionsProcessing

Expression = input("Type a logical expression:")
Expression = Expression.lower()
Literals = ExpressionSplitter.look_for_literals(Expression)
print(Literals)
DeniedLiterals = ExpressionSplitter.look_for_denied_literals(Expression)
print(DeniedLiterals)
FinalExpression = ExpressionSplitter.get_final_expression(Expression)
print(FinalExpression)
BooleansDictionary = ExpressionsProcessing.get_main_literals_values(Literals)
print(BooleansDictionary)
NDBooleans = ExpressionsProcessing.get_denied_literals_values(BooleansDictionary, DeniedLiterals)
print(NDBooleans) 

# Tkinter Window Nav Configuration

window = Tk()
window.state('zoomed')

window.rowconfigure(0,weight=1)
window.columnconfigure(0, weight=1)

Frame1= tk.Frame(window)
Frame2= tk.Frame(window)

canvas1 = Canvas(Frame1, width=1472, height=729)
canvas2 = Canvas(Frame2, width=1472, height=729)
background = PhotoImage(file='bg.ppm')
background2 = PhotoImage(file='bg2.ppm')
canvas1.pack()
canvas2.pack()


def show_frame(frame):
    frame.tkraise()

for frame in (Frame1, Frame2):
    frame.grid(row=0,column=0,sticky='nsew')
# Canvas 1 Code 

canvas1_title = tk.Label(canvas1, text="Welcome to FCC Toolkit")
canvas1_title.pack()
canvas1_btn = tk.Button(canvas1, text = "Enter", command=lambda:show_frame(Frame2))
canvas1_btn.pack()
canvas1.create_image(0,0,anchor=NW, image=background)
canvas1.pack(fill='both',expand=True)


# Canvas 2 Code 

canvas2_title = tk.Label(canvas2, text="This is your table")
canvas2_title.pack()
canvas2_btn = tk.Button(canvas2, text = "Enter", command=lambda:show_frame(Frame1))
canvas2_btn.pack()
canvas2.create_image(0,0,anchor=NW, image=background2)
canvas2.pack(fill='both',expand=True)





show_frame(Frame1)
window.mainloop()
