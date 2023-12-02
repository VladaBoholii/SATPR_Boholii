def find_prices(matrix):
    def find_lower_price(matrix):
        max_values = [min(row) for row in matrix]
        return max(max_values)

    def find_upper_price(matrix):
        min_values = [max(col) for col in zip(*matrix)]
        return min(min_values)

    lower_price = find_lower_price(matrix)
    upper_price = find_upper_price(matrix)

    return lower_price, upper_price

def optimal_strategies(matrix):
    lower_price, upper_price = find_prices(matrix)
    rows = len(matrix)
    cols = len(matrix[0])
    
    optimal_strategies_player1 = []
    optimal_strategies_player2 = []
    
    for i in range(rows):
        if min(matrix[i]) == lower_price:
            optimal_strategies_player1.append(i+1)
    
    for j in range(cols):
        col_values = [matrix[i][j] for i in range(rows)]
        if max(col_values) == upper_price:
            optimal_strategies_player2.append(j+1)
    
    return optimal_strategies_player1, optimal_strategies_player2, lower_price, upper_price

def print_results(matrix):
    optimal_strategies_player1, optimal_strategies_player2, lower_price, upper_price = optimal_strategies(matrix)

    print("Нижня ціна гри:", lower_price)
    print("Верхня ціна гри:", upper_price)

    print("Оптимальна стратегія для A:", optimal_strategies_player1)
    print("Оптимальна стратегія для B:", optimal_strategies_player2)

    if lower_price == upper_price:
        print("Рівновага існує.")
    else:
        print("Рівновага не існує.")

with open('lab5_1.txt', 'r') as file:
    lines = file.readlines()
    matrix = []
    for line in lines:
        row = list(map(float, line.strip().split()))
        matrix.append(row)

print("Задача 1:")
print_results(matrix)

with open('lab5_2.txt', 'r') as file:
    lines = file.readlines()
    matrix = []
    for line in lines:
        row = list(map(float, line.strip().split()))
        matrix.append(row)

print("\nЗадача 2:")
print_results(matrix)
