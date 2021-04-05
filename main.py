from tkinter import *
import tkinter as tk
import ExpressionSplitter
import ExpressionsProcessing
import sets_engine

# Tkinter Window Nav Configuration
decition = 0
window = Tk()
window.title("FCC ToolKit")
window.geometry("1500x700")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

Frame0 = tk.Frame(window)
Frame1 = tk.Frame(window)
Frame2 = tk.Frame(window)
Frame3 = tk.Frame(window)

logicalexpression = tk.StringVar()
optionSets = tk.StringVar()
Seta = tk.StringVar()
Setb= tk.StringVar()
Setc = tk.StringVar()
Choice2= tk.StringVar()


canvas0 = Canvas(Frame0, width=1472, height=730)
canvas1 = Canvas(Frame1, width=1472, height=730)
canvas2 = Canvas(Frame2, width=1472, height=730)
canvas3 = Canvas(Frame3, width=1472, height=730)
background = PhotoImage(file='bg1check.ppm')
background2 = PhotoImage(file='bg2check.ppm')
canvas0.pack()
canvas1.pack()
canvas2.pack()
canvas3.pack()

def goToOps():
    Frame3.tkraise()

def goToTruths():
    Frame1.tkraise()

def show_frame(frame):
    frame.tkraise()

def checkSubmitSet():
    decition = optionSets.get()
    set_a = Seta.get()
    set_b = Setb.get()
    set_c = Setc.get()
    FFirst, SSecond, TThird, FFourth = sets_engine.get_operative_set(decition,set_a,set_b,set_c)


    canvas3_label_First["text"] = FFirst
    canvas3_label_Second["text"] = SSecond
    canvas3_label_Third["text"] = TThird
    canvas3_label_Fourth["text"] = FFourth

    canvas3_Btn["state"] = "normal"
    canvas3_Btn["height"] = 2
    canvas3_Btn["width"] = 10

    canvas3_entry_choice2["width"] = 30

def continueProcedure():
    option = Choice2.get()
    decition = optionSets.get()
    set_a = Seta.get()
    set_b = Setb.get()
    set_c = Setc.get()
    requested = sets_engine.get_requested_union(decition,option,set_a,set_b,set_c)
    print("this is requested", requested)
    canvas3_requested["text"] = requested







def use_logical_expression(frame, canvas):
    frame.tkraise()
    expression = logicalexpression.get()
    expression = expression.lower()
    literals = ExpressionSplitter.look_for_literals(expression)
    denied_literals = ExpressionSplitter.look_for_denied_literals(expression)
    final_expression = ExpressionSplitter.get_final_expression(expression)
    booleans_dictionary = ExpressionsProcessing.get_main_literals_values(literals)
    n_d_booleans = ExpressionsProcessing.get_denied_literals_values(booleans_dictionary, denied_literals)
    full_dict = ExpressionsProcessing.split_subexpressions(n_d_booleans, final_expression, literals, denied_literals,expression)
    createTable(final_expression, full_dict, canvas)


def createTable(final_expression, full_dict, canvas):
    canvasTable = tk.Canvas(canvas, width =1000, height =500)
    relativex= 0
    relativey= 0
    augmentationVariable_x = 1000/len(final_expression)
    augmentationVariable_y = 500/(len(full_dict.get(final_expression[0]))+1)
    for variable in final_expression:
        e = tk.Label(canvasTable, text=variable,font= "times 10")
        e.pack()
        e.place(x=relativex,y=relativey)
        for bools in full_dict.get(variable):
            relativey= relativey + augmentationVariable_y   
            if bools == False:
                t = tk.Label(canvasTable, text="F",font= "times 10")
                t.pack()
                t.place(x=relativex, y=relativey)    
            if bools == True:
                t = tk.Label(canvasTable, text="V",font= "times 10")
                t.pack()
                t.place(x=relativex, y=relativey)              
        relativex = relativex + augmentationVariable_x
        relativey = 0
        e = 0
        t = 0
    canvasTable.pack(fill='both',expand=True)
    canvas.create_window(100, 100, anchor=NW, window=canvasTable)


for frame in (Frame0, Frame1, Frame2, Frame3):
    frame.grid(row=0,column=0,sticky='nsew')

# Canvas 0 Code 

canvas0_title= tk.Label(canvas0, text="Welcome to FCC ToolKit", font= "times 35")
canvas0_title.pack()
canvas0_title.place(relx=.33, rely=.1)

canvas0_Label =  tk.Label(canvas0, text="What Operation do you want?", font ="times 35")
canvas0_Label.pack()
canvas0_Label.place(relx=.30, rely=.2)

canvas0_Btn = tk.Button(canvas0, height=20, width= 30, text="Sets Operations", command=lambda: goToOps())
canvas0_Btn.pack(ipady=15)
canvas0_Btn.place(relx=.30, rely=.45)
canvas0_BtnTruth = tk.Button(canvas0, height= 20, width =30 , text= "Truth Tables", command=lambda: goToTruths())
canvas0_BtnTruth.pack(ipady=15)
canvas0_BtnTruth.place(relx=.55, rely=.45)
canvas0.create_image(0, 0, anchor=NW, image=background)

canvas0.pack(fill='both', expand=True)


# Canvas 1 Code 

canvas1_title = tk.Label(canvas1, text="Truth Table Generator", font= "times 35")
canvas1_title.pack()
canvas1_title.place(relx=.33, rely=.1)

canvas1_btn = tk.Button(canvas1,height= 3, width= 20, text = "Get Table", command=lambda: use_logical_expression(Frame2,canvas2))
canvas1_btn.pack(ipady=15)
canvas1_btn.place(relx=.45, rely=.45)

canvas1_label= tk.Label(canvas1, text="Type a Logical Expression ", font="times 20")
canvas1_label.pack()
canvas1_label.place(relx=.40, rely=.35)

canvas1_property= tk.Label(canvas1, text="Created by Omar Chavira, Gabriel Olvera  ", font="times 10")
canvas1_property.pack()
canvas1_property.place(relx=.85, rely=.9)

canvas1_entry = tk.Entry(canvas1,width=64, textvariable=logicalexpression)
canvas1_entry.pack()
canvas1_entry.place(relx=.37, rely=.4)

canvas1.create_image(0, 0, anchor=NW, image=background)

canvas1.pack(fill='both', expand=True)


# Canvas 2 Code 

canvas2_title = tk.Label(canvas2, text="Truth Table: ", font="times 35")
canvas2_title.pack()
canvas2_title.place(relx=.05, rely=.05)

canvas2_btn = tk.Button(canvas2, height=3, width=20, text="Back to Main Menu ", command=lambda: show_frame(Frame0))
canvas2_btn.pack()
canvas2_btn.place(relx= .8 , rely= .9)


canvas2.create_image(0, 0, anchor=NW, image=background2)
canvas2.pack(fill='both', expand=True)

# Canvas 3 Code 
canvas3_title = tk.Label(canvas3, text="Sets Operations", font= "times 35")
canvas3_title.pack()
canvas3_title.place(relx=.40, rely=.05)

canvas3_entry = tk.Entry(canvas3,width=24, textvariable=optionSets)
canvas3_entry.pack()
canvas3_entry.place(relx=.28, rely=.5)

canvas3_label_a = tk.Label(canvas3,font = "times 30", text= "Operations")
canvas3_label_a.pack()
canvas3_label_a.place(relx= .1 , rely=.15)

canvas3_label_b = tk.Label(canvas3,font = "times 20", text= "Choice : ")
canvas3_label_b.pack()
canvas3_label_b.place(relx= .17 , rely=.48)

canvas3_label_seta = tk.Label(canvas3,font = "times 20", text= "Set A: ")
canvas3_label_setb = tk.Label(canvas3,font = "times 20", text= "Set B: ")
canvas3_label_setc = tk.Label(canvas3,font = "times 20", text= "Set C: ")

canvas3_label_seta.pack()
canvas3_label_setb.pack()
canvas3_label_setc.pack()

canvas3_label_seta.place(relx= .17, rely= .60)
canvas3_label_setb.place(relx= .17, rely= .65)
canvas3_label_setc.place(relx= .17, rely= .70)

canvas3_entry_seta = tk.Entry(canvas3, width = 30 , textvariable = Seta)
canvas3_entry_setb = tk.Entry(canvas3, width = 30 , textvariable = Setb)
canvas3_entry_setc = tk.Entry(canvas3, width = 30 , textvariable = Setc)

canvas3_entry_seta.pack()
canvas3_entry_setb.pack()
canvas3_entry_setc.pack()

canvas3_entry_seta.place(relx= .25, rely= .62)
canvas3_entry_setb.place(relx= .25, rely= .67)
canvas3_entry_setc.place(relx= .25, rely= .72)

canvas3_buttonsubmit = tk.Button(canvas3, height=2, width=10,text="Submit",command=lambda: checkSubmitSet())
canvas3_buttonsubmit.pack(ipady=10)
canvas3_buttonsubmit.place(relx=.41, rely=.66)

canvas3_label_1 = tk.Label(canvas3,font = "times 20", text= "1- Union")
canvas3_label_2 = tk.Label(canvas3,font = "times 20", text= "2- Intersection")
canvas3_label_3 = tk.Label(canvas3,font = "times 20", text= "3- Diference")
canvas3_label_4 = tk.Label(canvas3,font = "times 20", text= "4- Symmetric Diference ")

canvas3_label_1.pack()
canvas3_label_2.pack()
canvas3_label_3.pack()
canvas3_label_4.pack()

canvas3_label_1.place(relx = .1, rely= .22)
canvas3_label_2.place(relx = .1, rely= .26) 
canvas3_label_3.place(relx = .1, rely= .30)
canvas3_label_4.place(relx = .1, rely= .34)

canvas3_label_First= tk.Label(canvas3, text="", font= "times 20")
canvas3_label_First.pack()
canvas3_label_First.place(relx=.7, rely=.22)

canvas3_label_Second= tk.Label(canvas3, text="", font= "times 20")
canvas3_label_Second.pack()
canvas3_label_Second.place(relx=.7, rely=.32)

canvas3_label_Third= tk.Label(canvas3, text="", font= "times 20")
canvas3_label_Third.pack()
canvas3_label_Third.place(relx=.7, rely=.42)

canvas3_label_Fourth= tk.Label(canvas3, text="", font= "times 20")
canvas3_label_Fourth.pack()
canvas3_label_Fourth.place(relx=.7, rely=.52)

canvas3_entry_choice2 = tk.Entry(canvas3, width=0, textvariable=Choice2)
canvas3_entry_choice2.pack()
canvas3_entry_choice2.place(relx=.7,rely=.58)

canvas3_Btn= tk.Button(canvas3, height=0, width=0,text="Submit",command=lambda:continueProcedure())
canvas3_Btn.pack(ipady=10)
canvas3_Btn.place(relx=.7,rely=.64)
canvas3_buttonsubmit = tk.Button(canvas3, height=2, width=10,text="Submit",command=lambda: checkSubmitSet())
canvas3_buttonsubmit.pack(ipady=10)
canvas3_buttonsubmit.place(relx=.41, rely=.66)

canvas3_requested = tk.Label(canvas3, text="", font= "times 20")
canvas3_requested.pack()
canvas3_requested.place(relx=.7, rely=.7)

canvas3_bbtn = tk.Button(canvas3, height=3, width=20, text="Back to Main Menu ", command=lambda: show_frame(Frame0))
canvas3_bbtn.pack()
canvas3_bbtn.place(relx= .8 , rely= .9)

canvas3.create_image(0, 0, anchor=NW, image=background2)
canvas3.pack(fill='both', expand=True)

show_frame(Frame0)
window.mainloop()
