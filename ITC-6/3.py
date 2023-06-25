def pascal(n):
    triangle = [[1]]

    for _ in range(n-1):
        temp = [0] + triangle[-1] + [0]
        row = []
        for j in range(len(triangle[-1])+1):
            row.append(int(temp[j]) + int(temp[j+1]))
        triangle.append(row)

    return triangle

print(pascal(6))
