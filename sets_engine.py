def get_sets(seta, setb, setc):
    # inputs are obtained in TK inter graphical display
    input_set_a = seta
    input_set_b = setb
    input_set_c = setc
    set_a = input_set_a.split(",")
    set_b = input_set_b.split(",")
    set_c = input_set_c.split(",")
    
    return set_a, set_b, set_c


def get_requested_union(operation, option, seta, setb, setc):
    set_a, set_b, set_c = get_sets(seta, setb, setc)
    if int(operation) == 1:
        if int(option) == 1:
            requested_union = get_union(set_a, set_b)
        elif int(option) == 2:
            requested_union = get_union(set_b, set_c)
        elif int(option) == 3:
            requested_union = get_union(set_a, set_c)
        elif int(option) == 4:
            requested_union = get_union(set_a, get_union(set_b, set_c)) 
    elif int(operation) == 2:
        if int(option) == 1:
            requested_union = get_intersection(set_a, set_b)
        elif int(option) == 2:
            requested_union = get_intersection(set_b, set_c)
        elif int(option) == 3:
            requested_union = get_intersection(set_a, set_c)
        elif int(option) == 4:
            requested_union = get_intersection(set_a, get_intersection(set_b, set_c))
    elif int(operation) == 3:
        if int(option) == 1:
            requested_union = get_difference(set_a, set_b)
        elif int(option) == 2:
            requested_union = get_difference(set_b, set_c)
        elif int(option) == 3:
            requested_union = get_difference(set_a, set_c)
    elif int(operation) == 4:
        if int(option) == 1:
            requested_union = get_symmetric_difference(set_a, set_b)
        elif int(option) == 2:
            requested_union = get_symmetric_difference(set_b, set_c)
        elif int(option) == 3:
            requested_union = get_symmetric_difference(set_a, set_c) 
    print("Requested Main UNin ", requested_union)
    return requested_union


def get_operative_set(operation, seta, setb, setc):
    # operation is obtained in TK inter graphical display
    """ operation = input("Operación a realizar: \n1.- Unión\n2.- Intersección"
                      "\n3.- Diferencia\n4.- Diferencia simétrica\n &>") """
    set_a, set_b, set_c = get_sets(seta, setb, setc)
    if int(operation) == 1:
        first_possible = "1.- A U B"
        second_possible = "2.- B U C"
        third_possible = "3.- A U C"
        fourth_possible = "4.- A U (B U C)"

        return first_possible, second_possible, third_possible, fourth_possible
    elif int(operation) == 2:
        first_possible = "1.- A INT B"
        second_possible = "2.- B INT C"
        third_possible = "3.- A INT C"
        fourth_possible = "4.- A INT (B INT C)"

        return first_possible, second_possible, third_possible, fourth_possible
    elif int(operation) == 3:
        first_possible = "1.- A - B"
        second_possible = "2.- B - C"
        third_possible = "3.- A - C"
        fourth_possible = " "

        return first_possible, second_possible, third_possible, fourth_possible
    elif int(operation) == 4:
        first_possible = "1.- A delta B"
        second_possible = "2.- B delta C"
        third_possible = "3.- A delta C"
        fourth_possible = " "

        return first_possible, second_possible, third_possible, fourth_possible
    

def get_union(set_1, set_2):
    union_array = set_1  # Result array is declared
    for i in set_2:  # For every element in set 2
        if i not in set_1:  # If i is no tin set 1
            union_array.append(i)  # Append i
    return union_array


def get_intersection(set_1, set_2):
    union_array = []  # Final array

    for i in set_1:  # For every i in set 1
        for j in set_2:  # For every j in set 2
            if i == j:  # If they are the same
                union_array.append(i)  # Append i
    return union_array


def get_difference(set_1, set_2):  # Get the difference in two sets
    union_array = []
    print(set_1, " - ", set_2)
    for i in set_2:  # For every element in set 2
        if i not in set_1:  # If one element is not in set 1
            union_array.append(i)  # Append to result set
    return union_array


def get_symmetric_difference(set_a, set_b):  # Gets symmetric difference between two sets
    partial_1 = get_difference(set_a, set_b)  # gets difference between a and b
    partial_2 = get_difference(set_b, set_a)  # gets difference between b and a
    union_array = get_union(partial_1, partial_2)  # Gets union between the two differences
    return union_array
