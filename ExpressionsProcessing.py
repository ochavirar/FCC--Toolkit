def get_main_literals_values(literals):
    values_p_literal = 2**len(literals)  # Total values per literal
    final_evaluation = []  # Array to return
    partial_evaluation = []  # Array to complete final_evaluation
    dictionary = {}
    sequence = values_p_literal  # Sequence between true and false,
    for i in range(0, len(literals), 1):  # For i in every literal
        sequence /= 2  # Sequence is reduced
        found_booleans = 0  # Found booleans
        step = 0  # Step starting in zero
        partial_evaluation.clear()  # Clears array to use again later
        while found_booleans < values_p_literal:  # While found booleans is less than 2^n spaces...
            if step < sequence:  # If step is less than the sequence...
                partial_evaluation.append(bool(1))  # Appends true
                found_booleans += 1  # One boolean was found
                step += 1  # Step increases
            elif step >= sequence:  # Else If step is greater or equal than the sequence...
                partial_evaluation.append(bool(0))  # Appends false
                found_booleans += 1  # One boolean was found
                step += 1  # Step increases
            if step >= sequence*2:  # If step is less than the double of the sequence...
                step = 0  # Step resets
        support_variable = partial_evaluation.copy()  # Partial evaluation is stored in a variable
        final_evaluation.append(support_variable)  # Appends support variable to the final array
        dictionary[literals[i]] = support_variable
    return dictionary


def get_denied_literals_values(normal_dictionary, denied_literals):
    support_variable = []  # Support var
    for i in denied_literals:  # For every denied literal
        substring = i[1]
        support = normal_dictionary.get(str(substring))  # Support variables
        support_variable.clear()
        for j in support:  # For every element in support
            if j:  # If true then...
                support_variable.append(not j)  # Append false
            else:  # If false then...
                support_variable.append(not j)  # Append true
        support = support_variable.copy()  # Partial evaluation is stored in a variable
        normal_dictionary[i] = support
    return normal_dictionary


def evaluate_expression(dictionary, final_exp, literals, denied_literals):
    start = (len(denied_literals)+len(literals))
    temp_array = []
    step = 0
    for i in range(start, len(final_exp), 1):
        temp_array.clear()
        print(final_exp[i])
        j = 0
        result = []
        if step >= 1:
            temp_array.append(final_exp[i - 1])
            j += len(final_exp[i - 1])
        while j < len(final_exp[i]):
            if (111 < ord(final_exp[i][j]) <= 122) and (ord(final_exp[i][j]) != 118):
                if final_exp[i][j-1] == '~':
                    temp_array.append(final_exp[i][j - 1:j+1])
                else:
                    temp_array.append(final_exp[i][j])
            elif final_exp[i][j] == 'v':
                temp_array.append(final_exp[i][j])
            elif final_exp[i][j] == '^':
                temp_array.append(final_exp[i][j])
            elif final_exp[i][j] == '→':
                temp_array.append(final_exp[i][j])
            elif final_exp[i][j] == '↔':
                temp_array.append(final_exp[i][j])
            j += 1
        step += 1
        result = evaluate(dictionary, temp_array)
        dictionary[final_exp[i]] = result
    return dictionary


def evaluate(dictionary, array):
    exp1, exp2 = dictionary.get(array[0]), dictionary.get(array[2])
    array_2 = []
    index = 0
    for i in range(len(exp1)):
        if array[1] == 'v':
            if (exp1[index] or exp2[index]) is True:
                array_2.append(True)
            else:
                array_2.append(False)
        if array[1] == '^':
            if (exp1[index] and exp2[index]) is True:
                array_2.append(True)
            else:
                array_2.append(False)
        if array[1] == '→':
            if (exp1[index] is True) and (exp2[index] is False):
                array_2.append(False)
            else:
                array_2.append(True)
        if array[1] == '↔':
            if ((exp1[index] is True) and (exp2[index] is True)) or ((exp1[index] is False) and (exp2[index] is False)):
                array_2.append(True)
            else:
                array_2.append(False)
        index += 1
    return array_2
