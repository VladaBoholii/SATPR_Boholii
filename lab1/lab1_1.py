def read_matrix_from_file(file_name):
    matrix = []
    with open(file_name, 'r') as file:
        for line in file:
            row = list(map(float, line.strip().split()))
            matrix.append(row)
    return matrix

def calculate_decision(matrix):
    weights = matrix[0] 
    alternatives = matrix[1:] 

    print("Початкова матриця:")
    for row in matrix:
        print(row)
    print("\nВаги критеріїв:", weights)

    weighted_matrix = []
    for alternative in alternatives:
        weighted_alternative = [alternative[i] * weights[i] for i in range(len(weights))]
        weighted_matrix.append(weighted_alternative)

    print("\nПроміжна матриця:")
    for row in weighted_matrix:
        print(row)

    sums = [sum(row) for row in weighted_matrix]

    print("\nСуми альтернатив:")
    for i, s in enumerate(sums, start=1):
        print(f"{i}: {s}")

    max_sum_index = sums.index(max(sums))

    chosen_alternative = max_sum_index + 1
    print(f"\nОбрана альтернатива: {chosen_alternative}")
    return chosen_alternative

file_name = 'lab1_1.txt'
matrix = read_matrix_from_file(file_name)
chosen_alternative = calculate_decision(matrix)

