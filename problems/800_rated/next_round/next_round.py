def main():
    function1()

def function1():
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1]) - 1 
    next = 0
    points = input()
    point_separated = points.split()
    points_list = []
    for i in point_separated:
        points_list.append(int(i))
    for j in range(n):
        if points_list[j] >= points_list[k] and points_list[j] != 0:
            next += 1
    
    print(next)

main()
