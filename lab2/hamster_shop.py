def max_food_consuming(array):
    max = array[0]
    elements_count = len(array)
    for i in range (0,elements_count-1):
        j = 0
        if array[i] > max:
            max = array[i]
            j = i
    return j      


def hamster_farm(hamster_matrix, total_food, hamster_count):

    if hamster_count != len(hamster_matrix):
        print("Exception")
    
    neighbourgs = hamster_count - 1
    current_hamsters = []
    total_food_consumed = 0

    for i in range(hamster_count):
        total_food_consumed += hamster_matrix[i][0] + hamster_matrix[i][1] * neighbourgs

    while(total_food < total_food_consumed):
        for i in range(hamster_count):
            food_consumed = hamster_matrix[i][0] + hamster_matrix[i][1] * neighbourgs
            current_hamsters.append(food_consumed)
        max_idx = max_food_consuming(current_hamsters)
        del hamster_matrix[max_idx]
        hamster_count = hamster_count - 1
        neighbourgs = neighbourgs - 1
        total_food_consumed = 0
        for i in range(hamster_count):
            total_food_consumed += hamster_matrix[i][0] + hamster_matrix[i][1] * neighbourgs  
    return hamster_count
    
hamsters = [[1, 50000], [1, 60000]]
food = 2
hamster_count = 2
max_hamsters = hamster_farm(hamsters, food, hamster_count)
print(max_hamsters)