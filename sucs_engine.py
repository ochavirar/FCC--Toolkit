def get_summation(expr, i_l, s_l):
    result = eval(expr, {"x": s_l})
    print("Partial result", result)
    if s_l > i_l:
        return result + get_summation(expr, i_l, s_l-1)
    else:
        return result


def get_multiplicative(expr, i_l, s_l):
    result = eval(expr, {"x": s_l})
    print("Partial result", result)
    if s_l > i_l:
        return result * get_multiplicative(expr, i_l, s_l-1)
    else:
        return result


expression = input("Type a formula: ")
superiorLimit = int(input("Superior limit: "))
inferiorLimit = int(input("Inferior limit: "))

multiplicative = get_multiplicative(expression, inferiorLimit, superiorLimit)
print("multiplicative:", multiplicative)
summation = get_summation(expression, inferiorLimit, superiorLimit)
print("Summation:", summation)
