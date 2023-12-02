import numpy as np

cereal = ['Кукурудза', 'Соя']

file_name = 'lab3_1.txt'

matrix = np.loadtxt(file_name)

probability = matrix[0]
income = matrix[1:]

print("Матриця ймовірностей:")
print(probability)

print("\nМатриця доходу:")
print(income)

result = np.zeros(income.shape[0])  

for i in range(income.shape[0]):
    result[i] = np.dot(probability, income[i])

print("Очікуваний прибуток", result)

max_income_index = np.argmax(result) 
max_income_crop = cereal[max_income_index] 

print(f"Очікуваний дохід від вирощування {max_income_crop} більший")
