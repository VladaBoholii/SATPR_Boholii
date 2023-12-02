import numpy as np

file_path = 'lab6.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

matrix = []
for line in lines:
    row = list(map(int, line.strip().split()))
    matrix.append(row)

matrix = np.array(matrix)

row_min = matrix.min(axis=1, keepdims=True)
matrix -= row_min
col_min = matrix.min(axis=0, keepdims=True)
matrix -= col_min

assignments = []

for i in range(5):
    row = matrix[i, :]
    top_2_indices = np.argsort(row)[:2]
    assignments.append((i, top_2_indices[0], i, top_2_indices[1]))

for assignment in assignments:
    group_1, org_1, group_2, org_2 = assignment
    print(f"Група {group_1 + 1}: Організація {org_1 + 1} та Організація {org_2 + 1}")
