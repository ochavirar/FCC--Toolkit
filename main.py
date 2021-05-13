from tkinter import *
import tkinter as tk
import ExpressionSplitter
import ExpressionsProcessing
import sets_engine
import rfEngine


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
Frame4 = tk.Frame(window)
Frame5 = tk.Frame(window)

logicalexpression = tk.StringVar()
optionSets = tk.StringVar()
Seta = tk.StringVar()
Setb= tk.StringVar()
Setc = tk.StringVar()
Choice2= tk.StringVar()

formulaa = tk.StringVar()
lim_inf = tk.StringVar()
lim_sup = tk.StringVar()

coords = tk.StringVar()

canvas0 = Canvas(Frame0, width=1472, height=730)
canvas1 = Canvas(Frame1, width=1472, height=730)
canvas2 = Canvas(Frame2, width=1472, height=730)
canvas3 = Canvas(Frame3, width=1472, height=730)
canvas4 = Canvas(Frame4, width=1472, height=730)
canvas5 = Canvas(Frame5, width=1472, height=730)

background = PhotoImage(file='bg1check.ppm')
background2 = PhotoImage(file='bg2check.ppm')

canvas0.pack()
canvas1.pack()
canvas2.pack()
canvas3.pack()
canvas4.pack()
canvas5.pack()


def goToSucs():
    Frame4.tkraise()


def goToOps():
    Frame3.tkraise()


def goToTruths():
    Frame1.tkraise()


def show_frame(frame):
    frame.tkraise()

def goToRelyFu():
    Frame5.tkraise()


def get_summation(expr, i_l, s_l):  # Returns summation
    result = eval(expr, {"x": s_l})  # Evaluation from string, using "x"
    canvas4_text.insert(END, "Partial result: " + str(result) + "\n")
    if s_l > i_l:
        return result + get_summation(expr, i_l, s_l-1)  # Recursive function
    else:
        return result


def get_multiplicative(expr, i_l, s_l):  # Returns multiplicative
    result = eval(expr, {"x": s_l})  # Evaluation from string using "x"
    if s_l > i_l:
        return result * get_multiplicative(expr, i_l, s_l-1)  # Recursive function
    else:
        return result


def submitSucs():
    expression = formulaa.get()
    superiorlimite = lim_sup.get()
    inferiorlimite = lim_inf.get()
    multiplicable = get_multiplicative(expression,int(inferiorlimite), int(superiorlimite))
    summation = get_summation(expression, int(inferiorlimite), int(superiorlimite))
    canvas4_summation["text"] = summation
    canvas4_multiplication["text"] = multiplicable


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


def doRelyFuc():
    parejas=coords.get()
    arrey = []
    arrey = rfEngine.get_coordinates(parejas)
    if ( rfEngine.get_reflexivity(arrey) == 1):
        canvas5_reflexivity["text"]= "Reflexivity: Yes"
    else:
        canvas5_reflexivity["text"]= "Reflexivity: No"

    if ( rfEngine.get_symmetry(arrey) == 1):
        canvas5_simmetry["text"]= "Simmetry: Yes"
    else:
        canvas5_simmetry["text"]= "Simmetry: No"

    if ( rfEngine.get_transitivity(arrey) == 1):
        canvas5_transivity["text"]= "Transivity: Yes"
    else:
        canvas5_transivity["text"]= "Transivity: No"
    
    if ( rfEngine.function_or_not(arrey) == 1):
        canvas5_function["text"]= "Function: Yes"
    else:
        canvas5_function["text"]= "Function: No"

    canvas5_domain["text"] = str(rfEngine.get_domain(arrey))
    canvas5_codomain["text"] = str(rfEngine.get_co_domain(arrey))





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


for frame in (Frame0, Frame1, Frame2, Frame3, Frame4, Frame5):
    frame.grid(row=0,column=0,sticky='nsew')

# Canvas 0 Code 

canvas0_title= tk.Label(canvas0, text="Welcome to FCC ToolKit", font= "times 35")
canvas0_title.pack()
canvas0_title.place(relx=.33, rely=.1)

canvas0_Label =  tk.Label(canvas0, text="What Operation do you want?", font ="times 35")
canvas0_Label.pack()
canvas0_Label.place(relx=.30, rely=.2)

canvas0_Btn = tk.Button(canvas0, height=20, width= 30, text="Sucessions", command=lambda: goToSucs())
canvas0_Btn.pack(ipady=15)
canvas0_Btn.place(relx=.10, rely=.45)

canvas0_Btn = tk.Button(canvas0, height=20, width= 30, text="Sets Operations", command=lambda: goToOps())
canvas0_Btn.pack(ipady=15)
canvas0_Btn.place(relx=.33, rely=.45)

canvas0_BtnTruth = tk.Button(canvas0, height= 20, width =30 , text= "Truth Tables", command=lambda: goToTruths())
canvas0_BtnTruth.pack(ipady=15)
canvas0_BtnTruth.place(relx=.53, rely=.45)
canvas0.create_image(0, 0, anchor=NW, image=background)

canvas0_Bops = tk.Button(canvas0, height=20, width= 30, text="Relations and Functions", command=lambda: goToRelyFu())
canvas0_Bops.pack(ipady=15)
canvas0_Bops.place(relx=.73, rely=.45)

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

#Canvas 4 code 
canvas4_title = tk.Label(canvas4, text="Sets Operations", font= "times 35")
canvas4_title.pack()
canvas4_title.place(relx=.40, rely=.05)

canvas4_formulalabel = tk.Label(canvas4, text="Enter Formula", font="times 20")
canvas4_formulalabel.pack()
canvas4_formulalabel.place(relx = .1, rely=.1)

canvas4_formula = tk.Entry(canvas4,width=24, textvariable=formulaa)
canvas4_formula.pack()
canvas4_formula.place(relx=.1, rely=.16)

canvas4_limsuplabel = tk.Label(canvas4, text="Limite Superior", font="times 20")
canvas4_limsuplabel.pack()
canvas4_limsuplabel.place(relx = .1, rely=.3)

canvas4_limsup = tk.Entry(canvas4,width=24, textvariable=lim_sup)
canvas4_limsup.pack()
canvas4_limsup.place(relx=.1, rely=.36)

canvas4_liminflabel = tk.Label(canvas4, text="Limite Inferior", font="times 20")
canvas4_liminflabel.pack()
canvas4_liminflabel.place(relx = .1, rely=.50)

canvas4_liminf = tk.Entry(canvas4,width=24, textvariable=lim_inf)
canvas4_liminf.pack()
canvas4_liminf.place(relx=.1, rely=.56)

canvas4_buttonsubmit = tk.Button(canvas4,height=2, width=10,text="Submit",command=lambda: submitSucs())
canvas4_buttonsubmit.pack(ipady=10)
canvas4_buttonsubmit.place(relx=.11, rely=.66)

canvas4_text = Text(canvas4, font="times 6", height=50)
canvas4_text.pack()
canvas4_text.place(relx =.50, rely=.2)

canvas4_summa = tk.Label(canvas4, text="Summation: ", font="times 20")
canvas4_summa.pack()
canvas4_summa.place(relx = .3, rely=.38)

canvas4_summation = tk.Label(canvas4, text="", font= "times 20")
canvas4_summation.pack()
canvas4_summation.place(relx = .3, rely=.43)

canvas4_mult = tk.Label(canvas4, text="Multiplicative: ", font="times 20")
canvas4_mult.pack()
canvas4_mult.place(relx = .3, rely=.60)

canvas4_multiplication = tk.Label(canvas4, text="", font= "times 20")
canvas4_multiplication.pack()
canvas4_multiplication.place(relx = .3, rely=.65)

canvas4_bbtn = tk.Button(canvas4, height=3, width=20, text="Back to Main Menu ", command=lambda: show_frame(Frame0))
canvas4_bbtn.pack()
canvas4_bbtn.place(relx= .9 , rely= .9)

canvas4.create_image(0,0,anchor=NW, image=background2)
canvas4.pack(fill='both', expand=True)

# Canvas 5 Code
canvas5_title = tk.Label(canvas5, text="Functions and Relations", font= "times 35")
canvas5_title.pack()
canvas5_title.place(relx=.35, rely=.05)

canvas5_label = tk.Label(canvas5, text= "Enter Ordered couples:  ", font = "times 12")
canvas5_label.pack()
canvas5_label.place(relx=.15, rely =.2)

canvas5_parejasEntry = tk.Entry(canvas5,width=24, textvariable=coords)
canvas5_parejasEntry.pack()
canvas5_parejasEntry.place(relx=.15, rely =.27)

canvas5_reflexivity = tk.Label(canvas5, text = "Reflexivity : ")
canvas5_reflexivity.pack()
canvas5_reflexivity.place(relx=.15, rely =.35)

canvas5_simmetry = tk.Label(canvas5, text = "Symmetry : ")
canvas5_simmetry.pack()
canvas5_simmetry.place(relx=.15, rely =.42)

canvas5_transivity = tk.Label(canvas5, text = "Transivity : ")
canvas5_transivity.pack()
canvas5_transivity.place(relx=.15, rely =.49)

canvas5_function = tk.Label(canvas5, text = "Function: ")
canvas5_function.pack()
canvas5_function.place(relx=.15, rely =.56)

canvas5_domain = tk.Label(canvas5, text = "")
canvas5_domain.pack()
canvas5_domain.place(relx=.15, rely =.63)

canvas5_codomain = tk.Label(canvas5, text = "")
canvas5_codomain.pack()
canvas5_codomain.place(relx=.15, rely =.70)

canvas5_btn = tk.Button(canvas5, height=3, width=20, text="Submit", command=lambda: doRelyFuc())
canvas5_btn.pack()
canvas5_btn.place(relx = .35, rely = .27)


canvas5_bbtn = tk.Button(canvas5, height=3, width=20, text="Back to Main Menu ", command=lambda: show_frame(Frame0))
canvas5_bbtn.pack()
canvas5_bbtn.place(relx= .9 , rely= .9)

canvas5.create_image(0,0,anchor=NW, image=background2)
canvas5.pack(fill='both', expand=True)




show_frame(Frame0)
window.mainloop()

