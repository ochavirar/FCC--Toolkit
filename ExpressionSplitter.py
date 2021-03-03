def look_for_literals(exp):  # This functions looks for literals and returns the array (ignoring the OR[v]).
    literals = []  # Array that will be returned.
    for i in exp:  # Goes through the string (obtained from user).
        if (111 < ord(i) <= 122) and (ord(i) != 118):  # if it is a letter and it is not v then...
            literals.append(i)  # Literal will be added to the array.
    literals = unrepeated_literals(literals)  # Calls a function to avoid repeated literals.
    return literals


def unrepeated_literals(literals):
    literals.sort()  # Sorted
    final_literals = literals  # Gets a copy from the original array
    index_i = 0
    index_j = 0
    for i in final_literals:  # For every element in the array
        index_j = 0
        for j in final_literals:  # For every element in the array
            if i == j and (index_j != index_i):
                literals.remove(i)
            index_j += 1
        index_i += 1
    return literals


def look_for_denied_literals(exp):  # This function Locates denied literals.
    denied_literals = []  # Array to be returned.
    for i in range(0, len(exp), 1):  # Goes from 0 to the array's length-1.
        if exp[i] == '~' and ((111 < ord(exp[i+1]) < 122) and (i != 'v')):  # If a ~ is found then...
            denied_literals.append(exp[i:i+2])  # denied literal will be added.
    return denied_literals


def parentheses_indexes_search(exp):
    is_divided = False
    open_parentheses = []  # Array to be returned
    closed_parentheses = []  # Array to be returned
    closed_parentheses_2 = []
    for i in range(0, len(exp), 1):  # Goes from 0 to the array's length-1
        if (exp[i] == '→' or exp[i] == '↔' or exp[i] == 'v' or exp[i] == '^') \
                and (exp[i - 1] == ')' and exp[i + 1] == '('):
            open_parentheses.clear()
            closed_parentheses.clear()
            for j in range(i, len(exp), 1):
                if exp[j] == '(':
                    open_parentheses.append(j)
                    print(open_parentheses)
                elif exp[j] == ')':
                    closed_parentheses.append(j)
                    print(closed_parentheses)
            closed_parentheses.reverse()
            for j in range(0, i, 1):
                if exp[j] == '(':
                    open_parentheses.append(j)
                    print(open_parentheses)
                elif exp[j] == ')':
                    closed_parentheses_2.append(j)
                    print(closed_parentheses)
                closed_parentheses_2.reverse()
            closed_parentheses += closed_parentheses_2
            closed_parentheses = [len(exp)-1] + closed_parentheses
            open_parentheses = [0] + open_parentheses
            print("CP", closed_parentheses, "OP:", open_parentheses)
            is_divided = True
            return open_parentheses, closed_parentheses, is_divided
        elif exp[i] == '(':  # If an opening parentheses is found then...
            open_parentheses.append(i)  # Open parentheses' index is added.
        elif exp[i] == ')':  # If an closing parentheses is found then...
            closed_parentheses.append(i)  # Closing parentheses' index is added
    closed_parentheses.reverse()
    # Closing parentheses is reversed to pair the opening and closing indexes
    is_divided = False
    return open_parentheses, closed_parentheses, is_divided


def split_parentheses_expression(exp):
    split_expression = []  # Array for split expressions
    open_parentheses, closed_parentheses, trial = parentheses_indexes_search(exp)  # Gets opening an closing indexes
    for i in range(len(open_parentheses)-1, -1, -1):  # For i in parentheses' array length, decreasing
        expression_to_append = exp[open_parentheses[i]:closed_parentheses[i]+1]  # Gets the expression to append
        split_expression.append(expression_to_append)  # Appends expression within range
    return split_expression


def get_final_expression(exp):
    final_array = []  # Array to be returned
    temp = look_for_literals(exp)  # Used to append elements individually
    length_support = len(look_for_literals(exp))
    for i in range(0, length_support, 1):  # For i in denied literals
        final_array.append(temp[i])  # Appends Literals.
    temp.clear()
    temp = look_for_denied_literals(exp)
    length_support = len(look_for_denied_literals(exp))
    for i in range(0, length_support, 1):  # For i in denied literals
        final_array.append(temp[i])  # Appends denied literals.
    temp.clear()
    temp = split_parentheses_expression(exp)
    length_support = len(split_parentheses_expression(exp))
    for i in range(0, length_support, 1):  # For i in parentheses
        final_array.append(temp[i])
    return final_array
