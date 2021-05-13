def get_coordinates(streng):
    coordinates = streng
    string_arrays = coordinates.split(' ')
    coordinate_array = []
    final_array = []
    temp_array = []
    for i in range(0, len(string_arrays), 1):
        coordinate_array.clear()
        x_value = int(string_arrays[i][0])
        y_value = int(string_arrays[i][2])
        coordinate_array.append(x_value)
        coordinate_array.append(y_value)
        temp_array = coordinate_array.copy()
        final_array.append(temp_array)
    final_array.sort()
    return final_array


def get_reflexivity(arr):
    reflexivity = 1  # Assuming reflexivity from the start
    found = 1
    for i in range(0, len(arr), 1):  # For every element in the array
        current_x = arr[i][0]  # Current x is found
        if found == 0:  # If not found for reflexivity, cycle ends and reflexivity is false
            reflexivity = 0
            break
        found = 0  # Found value restarted
        for j in range(0, len(arr), 1):
            if arr[j][0] == current_x and arr[j][1] == current_x:  # If x = c_x and y = c_x
                found = 1  # Reflexivity is achieved
    return reflexivity


def get_symmetry(arr):
    symmetry = 1  # Symmetry assumed as true
    found = 1
    for i in range(0, len(arr), 1):  # For every element in the array
        current_x = arr[i][0]
        current_y = arr[i][1]
        if found == 0:
            symmetry = 0
            break
        found = 0
        for j in range(0, len(arr), 1):
            if arr[j][0] == current_y and arr[j][1] == current_x:  # If symmetry is found...
                found = 1
    return symmetry


def get_transitivity(arr):
    transitivity = 1  # Transitivity assumed as true
    for i in range(0, len(arr), 1):  # For every element in the array
        current_x = arr[i][0]
        current_y = arr[i][1]
        if transitivity == 0:
            break
        for j in range(0, len(arr), 1):  # For every element in the array
            if arr[j][0] == current_y:  # If an x equals current_y
                current_z = arr[j][1]
                for k in range(0, len(arr), 1):  # For every element in the array
                    if arr[k][0] == current_x and arr[k][1] == current_z:  # If (current_x, current_z) is found...
                        transitivity = 1
                        break
                    else:
                        transitivity = 0
    return transitivity


def get_domain(arr):
    new_array = []
    for i in range(0, len(arr), 1):
        new_array.append(arr[i][0])  # Appends every x
    new_array.sort()
    for i in range(len(arr)-1, 0, -1):
        if len(arr) > 1 and new_array[i-1] == new_array[i]:
            new_array.remove(new_array[i])  # Deletes repetitions
    return new_array


def get_co_domain(arr):
    new_array = []
    for i in range(0, len(arr), 1):
        new_array.append(arr[i][1])  # Appends every x
    new_array.sort()
    for i in range(len(arr) - 1, 0, -1):
        if len(arr) > 1 and new_array[i - 1] == new_array[i]:
            new_array.remove(new_array[i])  # Deletes repetitions
    return new_array


def function_or_not(arr):
    function = 1
    for i in range(0, len(arr), 1):  # For every element in the array
        times = 0
        current_x = arr[i][0]  # X to look for
        for j in range(0, len(arr), 1):  # For every element in the array
            if arr[j][0] == current_x:  # if an x
                times += 1
        if times > 1:
            function = 0
            break
    return function
