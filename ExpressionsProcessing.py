import ExpressionSplitter


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


def split_subexpressions(dictionary, final_exp, literals, denied_literals, exp):  # Splits all of the
    # expression into smaller expressions.
    t1, t2, is_div = ExpressionSplitter.parentheses_indexes_search(exp)
    start = (len(denied_literals) + len(literals))
    temp_array = []
    step = 0
    if is_div is False:  # When the operation is divided in two by a → operator.
        for i in range(start, len(final_exp), 1):
            temp_array.clear()
            print(final_exp[i])
            j = 0
            if step >= 1:
                temp_array.append(final_exp[i - 1])
                j += len(final_exp[i - 1])
            while j < len(final_exp[i]):
                if (111 < ord(final_exp[i][j]) <= 122) and (ord(final_exp[i][j]) != 118):
                    if final_exp[i][j - 1] == '~':
                        temp_array.append(final_exp[i][j - 1:j + 1])
                    else:
                        temp_array.append(final_exp[i][j])
                elif (final_exp[i][j] == 'v' or final_exp[i][j] == '^' or final_exp[i][j] == '→' or
                      final_exp[i][j] == '↔'):
                    temp_array.append(final_exp[i][j])
                j += 1
            step += 1
            count = i
            result = evaluate(dictionary, temp_array, final_exp, count)
            dictionary[final_exp[i]] = result
        return dictionary
    else:  # When the operation is not divided
        for i in range(start, len(final_exp), 1):
            bigger = 0
            blocked = False
            temp_array.clear()
            j = 0
            if i == (len(final_exp)-1):
                blocked = True
                substring_1, substring_2 = "", ""
                to_append = ""
                for k in range(0, len(final_exp[i]), 1):
                    if (final_exp[i][k] == 'v' or final_exp[i][k] == '^' or final_exp[i][k] == '→' or
                            final_exp[i][k] == '↔') and (final_exp[i][k-1] == ')'):
                        substring_1 = final_exp[i][0:k]
                        symbol = final_exp[i][k]
                    if (final_exp[i][k] == 'v' or final_exp[i][k] == '^' or final_exp[i][k] == '→' or
                            final_exp[i][k] == '↔') and (final_exp[i][k+1] == '('):
                        substring_2 = final_exp[i][k+1:len(final_exp[i])]
                    elif (final_exp[i][k] == 'v' or final_exp[i][k] == '^' or final_exp[i][k] == '→' or
                            final_exp[i][k] == '↔') and (final_exp[i][k+1] == '~'):
                        substring_2 = final_exp[i][k+1:len(final_exp[i])]
                temp_array.append(substring_1)
                temp_array.append(symbol)
                temp_array.append(substring_2)
            elif step >= 1:
                if final_exp[i].find(final_exp[i - 1]) != -1:
                    temp_array.append(final_exp[i - 1])
                    j += len(final_exp[i - 1])
            while j < len(final_exp[i]) and blocked is False:
                if ((111 < ord(final_exp[i][j]) <= 122) and (ord(final_exp[i][j]) != 118)) \
                        or ord(final_exp[i][j]) == '(':
                    if final_exp[i][j - 1] == '~':
                        temp_array.append(final_exp[i][j - 1:j + 1])
                    else:
                        temp_array.append(final_exp[i][j])
                elif (final_exp[i][j] == 'v' or final_exp[i][j] == '^' or final_exp[i][j] == '→' or
                      final_exp[i][j] == '↔'):
                    temp_array.append(final_exp[i][j])
                j += 1
            step += 1
            print("TA:", temp_array)
            count = i
            result = evaluate(dictionary, temp_array, final_exp, count)
            dictionary[final_exp[i]] = result
        return dictionary


def evaluate(dictionary, array, exp, count):  # Evaluates every expression from the dictionary
    exp1, exp2 = dictionary.get(array[0]), dictionary.get(array[2])  # Assign two dictionaries for local use
    string = str(array[0])
    print("String:", string)
    print("Exp:", exp[count][0:2])
    index = 0
    result = False
    array_support = []
    array_2 = []
    visited = False
    for i in range(len(exp1)):
        if array[1] == 'v':  # OR logical expression
            if (exp1[index] or exp2[index]) is True:
                array_2.append(True)
            else:
                array_2.append(False)
        if array[1] == '^':  # AND logical expression
            if (exp1[index] and exp2[index]) is True:
                array_2.append(True)
            else:
                array_2.append(False)
        if array[1] == '→':  # Therefore evaluation
            if (exp1[index] is True) and (exp2[index] is False):
                array_2.append(False)
            else:
                array_2.append(True)
        if array[1] == '↔':  # If only evaluation
            if ((exp1[index] is True) and (exp2[index] is True)) or \
                    ((exp1[index] is False) and (exp2[index] is False)):
                array_2.append(True)
            else:
                array_2.append(False)
        print("Exp cnt", exp[count])
        if exp[count][0:1] == '~':  # NOT evaluation, taking the previous character to the expression
            visited = True
            if array_2[index] is True:
                result = False
            else:
                result = True
            array_support.append(result)
        index += 1
    if visited is True:
        array_2 = array_support
    return array_2
