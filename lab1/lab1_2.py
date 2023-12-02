import numpy as np


file_name = 'lab1_2.txt' 

matrix = np.loadtxt(file_name)

weights = matrix[0]
alternatives = matrix[1:]

print("Початкова матриця:")
print(matrix)

print("\nВаги критеріїв:", weights)

max_values = np.max(alternatives, axis=0)
min_values = np.min(alternatives, axis=0)

max_values = np.max(alternatives, axis=0)
min_values = np.min(alternatives, axis=0)

normalized_values = []
for row in alternatives:
    normalized_row = []
    for i, val in enumerate(row):
        min_val = min_values[i]
        max_val = max_values[i]

        if i == 1: 
            normalized_row.append(round(((max_val - val) / (max_val - min_val)),2))
        else:
            normalized_row.append(round(((val - min_val) / (max_val - min_val)),2))
    normalized_values.append(normalized_row)

print("\nНормалізовані значення:")
print(np.array(normalized_values))

results  = np.dot(normalized_values, weights)
max_result = np.max(results)
max_result_position = np.argmax(results) + 1

print("\nРезультати:")
print(results)
print(f'Обираємо альтернативу {max_result_position}')
