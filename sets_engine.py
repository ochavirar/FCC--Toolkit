def get_sets():
    input_set_a = input("Set A: ")
    input_set_b = input("Set B: ")
    input_set_c = input("Set C: ")
    set_a = input_set_a.split(",")
    set_b = input_set_b.split(",")
    set_c = input_set_c.split(",")
    print(set_a, set_b, set_c)
    return set_a, set_b, set_c


def get_operative_set():
    operation = input("Operación a realizar: \n1.- Unión\n2.- Intersección"
                      "\n3.- Diferencia\n4.- Diferencia simétrica\n &>")
    set_a, set_b, set_c = get_sets()
    requested_union = []
    if int(operation) == 1:
        print("1.- A U B")
        print("2.- B U C")
        print("3.- A U C")
        print("4.- A U (B U C)")
        option = input("Conjunto: ")
        if int(option) == 1:
            requested_union = get_union(set_a, set_b)
        elif int(option) == 2:
            requested_union = get_union(set_b, set_c)
        elif int(option) == 3:
            requested_union = get_union(set_a, set_c)
        elif int(option) == 4:
            requested_union = get_union(set_a, get_union(set_b, set_c))
    elif int(operation) == 2:
        print("1.- A INT B")
        print("2.- B INT C")
        print("3.- A INT C")
        print("4.- A INT (B INT C)")
        option = input("Conjunto: ")
        if int(option) == 1:
            requested_union = get_intersection(set_a, set_b)
        elif int(option) == 2:
            requested_union = get_intersection(set_b, set_c)
        elif int(option) == 3:
            requested_union = get_intersection(set_a, set_c)
        elif int(option) == 4:
            requested_union = get_intersection(set_a, get_intersection(set_b, set_c))
    elif int(operation) == 3:
        print("1.- A - B")
        print("2.- B - C")
        print("3.- A - C")
        option = input("Conjunto: ")
        if int(option) == 1:
            requested_union = get_difference(set_a, set_b)
        elif int(option) == 2:
            requested_union = get_difference(set_b, set_c)
        elif int(option) == 3:
            requested_union = get_difference(set_a, set_c)
    elif int(operation) == 4:
        print("1.- A delta B")
        print("2.- B delta C")
        print("3.- A delta B")
        option = input("Conjunto: ")
        if int(option) == 1:
            requested_union = get_symmetric_difference(set_a, set_b)
        elif int(option) == 2:
            requested_union = get_symmetric_difference(set_b, set_c)
        elif int(option) == 3:
            requested_union = get_symmetric_difference(set_a, set_c)
    return requested_union


def get_union(set_1, set_2):
    print(set_1, "U", set_2)
    union_array = set_1
    for i in set_2:
        if i not in set_1:
            union_array.append(i)
    return union_array


def get_intersection(set_1, set_2):
    union_array = []
    print(set_1, "INT", set_2)
    for i in set_1:
        for j in set_2:
            if i == j:
                union_array.append(i)
    return union_array


def get_difference(set_1, set_2):
    union_array = []
    print(set_1, " - ", set_2)
    for i in set_2:
        if i not in set_1:
            union_array.append(i)
    return union_array


def get_symmetric_difference(set_a, set_b):
    partial_1 = get_difference(set_a, set_b)
    partial_2 = get_difference(set_b, set_a)
    union_array = get_union(partial_1, partial_2)
    return union_array
