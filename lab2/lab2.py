import numpy as np

def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        matrix = []
        for line in lines:
            row = list(map(float, line.strip().split()))
            matrix.append(row)
    return np.array(matrix)

def calculate_priority(matrix):
    n = matrix.shape[0]
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    max_eigenvalue_index = np.argmax(eigenvalues)
    eigenvector = np.real(eigenvectors[:, max_eigenvalue_index])
    priority_vector = eigenvector / eigenvector.sum()
    return priority_vector

criteria_matrix_file = 'lab2_criteria.txt'
criteria_matrix = read_matrix_from_file(criteria_matrix_file)
criteria_priority = calculate_priority(criteria_matrix)

criteria_vector = np.round(criteria_priority, 2)

print("Wнорм для критеріїв:")
print(criteria_vector)

alternatives_matrices = []
for i in range(1, 10):
    filename = f'lab2_alternative_{i}.txt'
    matrix = read_matrix_from_file(filename)
    alternatives_matrices.append(matrix)

alternative_priorities = []
for i, matrix in enumerate(alternatives_matrices):
    alternative_priority = calculate_priority(matrix)
    alternative_priorities.append(alternative_priority)

num_criteria = len(alternative_priorities[0])

priority_vectors = [[] for _ in range(num_criteria)]

for i in range(num_criteria):
    for j in range(len(alternative_priorities)):
        priority_vectors[i].append(round(alternative_priorities[j][i], 2))

for i, vector in enumerate(priority_vectors, start=1):
    print(f"Wнорм для альтернативи {i}:")
    print(vector)

results_vector = np.zeros(3) 

for i, vector in enumerate(priority_vectors):  
    result = np.dot(criteria_priority, vector)  
    results_vector[i] = result 

print("Результат:")
print(np.round(results_vector, 2))

print(f"Обираємо альтернативу {np.argmax(results_vector)+1}")

