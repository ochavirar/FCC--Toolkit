""" import main
from tkinter import *
import tkinter as tk

def get_summation(expr, i_l, s_l):
    result = eval(expr, {"x": s_l})
    main.canvas4_text.insert(END, result)
    if s_l > i_l:
        return result + get_summation(expr, i_l, s_l-1)
    else:
        return result


def get_multiplicative(expr, i_l, s_l):
    result = eval(expr, {"x": s_l})
    if s_l > i_l:
        return result * get_multiplicative(expr, i_l, s_l-1)
    else:
        return result

 """