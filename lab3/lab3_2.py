import numpy as np

price = 2400
production_cost = -1500

file_name = 'lab3_2.txt'

matrix = np.loadtxt(file_name)

probability = matrix[0]
demand = matrix[1]

print("Матриця ймовірностей:")
print(probability)

print("\nМатриця доходу:")
print(demand)

result = np.zeros(demand.shape[0])  

for i in range(len(demand)):
    result[i] = demand[i]*(price+production_cost)*probability[i]

print("Очікуваний прибуток", result)

max_demand_index = np.argmax(result) 

print(f"Очікуваний дохід від виробництва {demand[max_demand_index]} т більший")
