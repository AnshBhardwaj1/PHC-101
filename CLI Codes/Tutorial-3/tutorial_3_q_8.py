def transpose():
    
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element ({i+1},{j+1}): "))
            row.append(element)
        matrix.append(row)
    return [[matrix[j][i] for j in range(rows)] for i in range(cols)]
result = transpose()
print(result)

