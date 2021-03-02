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
    updated_dictionary = {}  # Dictionary to return
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
    for i in range(start, len(final_exp), 1):
        for j in range(0, len(final_exp[i]), 1):
            print(final_exp[i])
