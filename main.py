from tkinter import *
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

window = Tk()
window.title("FCC-Toolkit")
window.mainloop()
