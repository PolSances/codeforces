def main():
    matrix = []
    for i in range(5):
        row = input().split()
        matrix.append(row)
    coordinates = []
    for j in range(5):
        for k in range(5):
            if matrix[j][k] == "1":
                coordinates += [j,k]
                break
            else:
                continue
    print(abs(coordinates[0]-2) + abs(coordinates[1]-2) )

main()