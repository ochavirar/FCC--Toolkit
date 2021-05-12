def get_coordinates():
    n = int(input("Coordinates: "))
    final_array = []
    coordinate = []
    for i in range(0, n, 1):
        coordinate.clear()
        x_value = int(input("x value: "))
        y_value = int(input("y value: "))
        coordinate.append(x_value)
        coordinate.append(y_value)
        temp_array = coordinate.copy()
        final_array.append(temp_array)
    final_array.sort()
    return final_array


def get_reflexivity(arr):
    reflexivity = 1
    found = 1
    for i in range(0, len(arr), 1):
        current_x = arr[i][0]
        if found == 0:
            reflexivity = 0
            break
        found = 0
        for j in range(0, len(arr), 1):
            if arr[j][0] == current_x and arr[j][1] == current_x:
                found = 1
    return reflexivity


def get_symmetry(arr):
    symmetry = 1
    found = 1
    for i in range(0, len(arr), 1):
        current_x = arr[i][0]
        current_y = arr[i][1]
        if found == 0:
            symmetry = 0
            break
        found = 0
        for j in range(0, len(arr), 1):
            if arr[j][0] == current_y and arr[j][1] == current_x:
                found = 1
    return symmetry


def get_transitivity(arr):
    transitivity = 1
    for i in range(0, len(arr), 1):
        current_x = arr[i][0]
        current_y = arr[i][1]
        if transitivity == 0:
            break
        for j in range(0, len(arr), 1):
            if arr[j][0] == current_y:
                current_z = arr[j][1]
                for k in range(0, len(arr), 1):
                    if arr[k][0] == current_x and arr[k][1] == current_z:
                        transitivity = 1
                        break
                    else:
                        transitivity = 0
    return transitivity


def get_domain(arr):
    new_array = []
    for i in range(0, len(arr), 1):
        new_array.append(arr[i][0])
    new_array.sort()
    for i in range(len(arr)-1, 0, -1):
        if new_array[i-1] == new_array[i]:
            new_array.remove(arr[i][0])
    return new_array


def get_co_domain(arr):
    new_array = []
    for i in range(0, len(arr), 1):
        new_array.append(arr[i][1])
    new_array.sort()
    for i in range(len(arr)-1, 0, -1):
        if new_array[i-1] == new_array[i]:
            new_array.remove(arr[i][0])
    return new_array


def function_or_not(arr):
    function = 1
    for i in range(0, len(arr), 1):
        times = 0
        current_x = arr[i][0]
        for j in range(0, len(arr), 1):
            if arr[j][0] == current_x:
                times += 1
        if times > 1:
            function = 0
            break
    return function
