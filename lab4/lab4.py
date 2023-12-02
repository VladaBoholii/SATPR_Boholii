import numpy as np

def read_matrix_from_file(file_name):
    matrix = []
    with open(file_name, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split())) 
            matrix.append(row)
    return matrix

def find_pessimistic_values(matrix):
    pessimistic_values = []
    for row in matrix:
        min_val = min(row) 
        pessimistic_values.append(min_val)
    return pessimistic_values

def find_optimistic_values(matrix):
    optimistic_values = []
    for row in matrix:
        max_val = max(row)  
        optimistic_values.append(max_val)
    return optimistic_values

def find_gurvitz_criterion(matrix, alpha):
    gurvitz_values = []
    for row in matrix:
        min_val = min(row) 
        max_val = max(row)
        gurvitz_val = alpha * min_val + (1 - alpha) * max_val
        gurvitz_values.append(gurvitz_val)
    return gurvitz_values

def find_laplace_criterion(matrix):
    laplace_values = []
    for row in matrix:
        mean_val = np.mean(row) 
        laplace_values.append(mean_val)
    return laplace_values

def find_bayes_laplace_criterion(matrix, p):
    bayes_laplace_values = []
    for row in matrix:
        bayes_laplace_val = np.dot(p, row)
        bayes_laplace_values.append(bayes_laplace_val)
    return bayes_laplace_values

def find_hodge_Lehmann_criterion(bayes_laplace_values, pessimistic_values, alpha):
    hodge_Lehmann_values = []
    for i in range(len(bayes_laplace_values)):
        hodge_Lehmann_val = pessimistic_values[i] * alpha + bayes_laplace_values[i] * (1 - alpha)
        hodge_Lehmann_values.append(hodge_Lehmann_val)
    return hodge_Lehmann_values

def print_pessimistic_values(matrix):
    pessimistic_values = find_pessimistic_values(matrix)
    print("Песимістичні значення  матриці:")
    for idx, val in enumerate(pessimistic_values, start=1):
        print(f"Рядок {idx}: {val}")
    min_pessimistic_val = min(pessimistic_values)
    alternative_index = pessimistic_values.index(min_pessimistic_val) + 1
    print(f'Обираємо альтернативу {alternative_index}\n')

def print_optimistic_values(matrix):
    optimistic_values = find_optimistic_values(matrix)
    print("\nОптимістичні значення матриці:")
    for idx, val in enumerate(optimistic_values, start=1):
        print(f"Рядок {idx}: {val}")
    max_optimistic_val = max(optimistic_values)
    alternative_index_optimistic = optimistic_values.index(max_optimistic_val) + 1
    print(f'Обираємо альтернативу {alternative_index_optimistic}\n')

def print_gurvitz_values(matrix, alpha):
    gurvitz_values = find_gurvitz_criterion(matrix, alpha)
    print("\nЗначення за критерієм Гурвіца з параметром α =", alpha)
    for idx, val in enumerate(gurvitz_values, start=1):
        print(f"Рядок {idx}: {val}")
    max_gurvitz_val = max(gurvitz_values)
    alternative_index_gurvitz = gurvitz_values.index(max_gurvitz_val) + 1
    print(f'Обираємо альтернативу {alternative_index_gurvitz} \n')

def print_laplace_values(matrix):
    laplace_values = find_laplace_criterion(matrix)
    print("\nЗначення за критерієм Лапласа:")
    for idx, val in enumerate(laplace_values, start=1):
        print(f"Рядок {idx}: {val}")
    max_laplace_val = max(laplace_values)
    alternative_index_laplace = laplace_values.index(max_laplace_val) + 1
    print(f'Обираємо альтернативу {alternative_index_laplace}\n')

def print_bayes_laplace_values(matrix, p):
    bayes_laplace_values = find_bayes_laplace_criterion(matrix, p)
    print("\nЗначення за критерієм Байєса-Лапласа:")
    for idx, val in enumerate(bayes_laplace_values, start=1):
        print(f"Рядок {idx}: {val}")
    max_bayes_laplace_val = max(bayes_laplace_values)
    alternative_index_bayes_laplace = bayes_laplace_values.index(max_bayes_laplace_val) + 1
    print(f'Обираємо альтернативу {alternative_index_bayes_laplace}\n')

def print_hodge_Lehmann_values(bayes_laplace_values, pessimistic_values, alpha):
    hodge_Lehmann_values = find_hodge_Lehmann_criterion(bayes_laplace_values, pessimistic_values, alpha)
    print("\nЗначення за критерієм Ходжа-Лемана:")
    for idx, val in enumerate(hodge_Lehmann_values, start=1):
        print(f"Рядок {idx}: {val}")
    max_hodge_Lehmann_val = max(hodge_Lehmann_values)
    alternative_index_hodge_Lehmann = hodge_Lehmann_values.index(max_hodge_Lehmann_val) + 1
    print(f'Обираємо альтернативу {alternative_index_hodge_Lehmann}\n')


file_name = 'lab4_1.txt'
matrix = read_matrix_from_file(file_name)
print('Задача 1\n')
print_pessimistic_values(matrix)
print_optimistic_values(matrix)
print_gurvitz_values(matrix, 0.07)
print_laplace_values(matrix)
p1 = 0.1
p2 = 0.2
alpha = 0.07
p3 = alpha
p4 = alpha + 0.1
p5 = 1 - p1 - p2 - p3 - p4
p = [p1, p2, p3, p4, p5]
print_bayes_laplace_values(matrix, p)
print_hodge_Lehmann_values(find_bayes_laplace_criterion(matrix, p), find_pessimistic_values(matrix), alpha)
#################################
print('Задача 2\n')
file_name = 'lab4_2.txt'
matrix = read_matrix_from_file(file_name)
print_pessimistic_values(matrix)
print_optimistic_values(matrix)
print_gurvitz_values(matrix, 0.07)
print_laplace_values(matrix)
p = [0.3, 0.7]
print_bayes_laplace_values(matrix, p)
print_hodge_Lehmann_values(find_bayes_laplace_criterion(matrix, p), find_pessimistic_values(matrix), alpha)
