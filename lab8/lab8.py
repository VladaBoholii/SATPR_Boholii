import numpy as np

def northwest_corner_method(supply, demand, costs):
    supply_copy = supply.copy()
    demand_copy = demand.copy()
    num_suppliers = len(supply)
    num_customers = len(demand)
    
    transportation_plan = np.zeros((num_suppliers, num_customers))
    
    i, j = 0, 0
    
    while i < num_suppliers and j < num_customers:
        if supply_copy[i] <= demand_copy[j]:
            transportation_plan[i][j] = supply_copy[i]
            demand_copy[j] -= supply_copy[i]
            i += 1
        else:
            transportation_plan[i][j] = demand_copy[j]
            supply_copy[i] -= demand_copy[j]
            j += 1
    
    return transportation_plan

supply = [230, 250, 170]
demand = [140, 90, 160, 110, 150]
costs = np.array([
    [40, 19, 25, 25, 35],
    [49, 26, 27, 18, 38],
    [46, 27, 36, 40, 45]
])

result = northwest_corner_method(supply, demand, costs)
print("Задача 1")
print("План за методом північно-західного кута:")
print(result)

supply = [200, 300, 250]
demand = [210, 150, 120, 135, 135]
costs = np.array([
    [20, 10, 13, 13, 18],
    [27, 19, 20, 16, 22],
    [26, 17, 19, 21, 23]
])

result = northwest_corner_method(supply, demand, costs)
print("\nЗадача 2")
print("План за методом північно-західного кута:")
print(result)