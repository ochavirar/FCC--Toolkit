from tkinter import *
import tkinter as tk
import ExpressionSplitter
import ExpressionsProcessing

# Tkinter Window Nav Configuration

window = Tk()
window.geometry("1500x700")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

Frame1 = tk.Frame(window)
Frame2 = tk.Frame(window)

logicalexpression= tk.StringVar()

canvas1 = Canvas(Frame1, width=1472, height=730)
canvas2 = Canvas(Frame2, width=1472, height=730)
background = PhotoImage(file='bg1check.ppm')
background2 = PhotoImage(file='bg2check.ppm')
canvas1.pack()
canvas2.pack()


def show_frame(frame):
    frame.tkraise()


def use_logical_expression(frame):
    frame.tkraise()
    expression = logicalexpression.get()
    # Testing Only Should Delete
    expression = expression.lower()
    print(expression)
    literals = ExpressionSplitter.look_for_literals(expression)
    print(literals)
    denied_literals = ExpressionSplitter.look_for_denied_literals(expression)
    print(denied_literals)
    final_expression = ExpressionSplitter.get_final_expression(expression)
    print(final_expression)
    booleans_dictionary = ExpressionsProcessing.get_main_literals_values(literals)
    print(booleans_dictionary)
    n_d_booleans = ExpressionsProcessing.get_denied_literals_values(booleans_dictionary, denied_literals)
    print(n_d_booleans)
    full_dict = ExpressionsProcessing.split_subexpressions(n_d_booleans, final_expression, literals, denied_literals,
                                                           expression)
    print(full_dict)
    createTable(final_expression, full_dict, frame)

""" def createTable(final_expression, full_dict, frame):
    canvasTable = tk.Canvas(frame, width =1000, height =500)
    i = 0
    x= 0
    relativex= 0
    relativey= 0
    for variable in final_expression:
        e = tk.Label(canvasTable, text=variable,font= "times 10")
        e.pack()
        e.place(relx=relativex,rely=relativey)
        relativey = relativey + .01
        for boolean in full_dict.get(i):
            t = tk.Label(canvasTable, text=full_dict.get(i)[x]w,font= "times 10")
            t.pack()
            t.place(relx=relativex, rely=relativey)
            x=x+1
        relativex= relativex + .2    
        i +=1
        e = 0
        t = 0
    canvasTable.pack(fill='both',expand=True) """

            
def createTable(final_expression, full_dict, frame):
    canvasTable = tk.Canvas(frame, width =1000, height =500)
    relativex= 0
    relativey= 0

    for variable in final_expression:
        e = tk.Label(canvasTable, text=variable,font= "times 10")
        e.pack()
        e.place(relx=relativex,rely=relativey)
        for bools in full_dict.get(variable):
            relativey= relativey + .2    
            if bools == False:
                t = tk.Label(canvasTable, text="False",font= "times 10")
                t.pack()
                t.place(relx=relativex, rely=relativey)    
            if bools == True:
                t = tk.Label(canvasTable, text="True",font= "times 10")
                t.pack()
                t.place(relx=relativex, rely=relativey)              
        relativex= relativex +.2 
        relativey = 0
        e = 0
        t = 0
    canvasTable.pack(fill='both',expand=True)
    frame.create_window(100, 100, anchor=NW, window=canvasTable)

    





for frame in (Frame1, Frame2):
    frame.grid(row=0,column=0,sticky='nsew')

    
# Canvas 1 Code 

canvas1_title = tk.Label(canvas1, text="Welcome to FCC ToolKit", font= "times 35")
canvas1_title.pack()
canvas1_title.place(relx= .33 , rely= .1)

canvas1_btn = tk.Button(canvas1,height= 3, width= 20, text = "Get Table", command=lambda: use_logical_expression(Frame2))
canvas1_btn.pack(ipady=15)
canvas1_btn.place(relx= .45 , rely= .45)

canvas1_label= tk.Label(canvas1, text="Type a Logical Expression ", font = "times 20")
canvas1_label.pack()
canvas1_label.place(relx=.40, rely=.35)

canvas1_property= tk.Label(canvas1, text="Created by Omar Chavira, Gabriel Olvera  ", font = "times 10")
canvas1_property.pack()
canvas1_property.place(relx=.85, rely=.9)

canvas1_entry = tk.Entry(canvas1,width=64, textvariable=logicalexpression)
canvas1_entry.pack()
canvas1_entry.place(relx=.37, rely=.4)

canvas1.create_image(0,0,anchor=NW, image=background)

canvas1.pack(fill='both',expand=True)


# Canvas 2 Code 

canvas2_title = tk.Label(canvas2, text="Truth Table: " ,font= "times 35")
canvas2_title.pack()
canvas2_title.place(relx= .05 , rely= .05)

canvas2_btn = tk.Button(canvas2,height= 3, width= 20, text = "Back to Main Menu ", command=lambda:show_frame(Frame1))
canvas2_btn.pack()
canvas2_btn.place(relx= .8 , rely= .9)


canvas2.create_image(0,0,anchor=NW, image=background2)
canvas2.pack(fill='both',expand=True)


show_frame(Frame1)
window.mainloop()
