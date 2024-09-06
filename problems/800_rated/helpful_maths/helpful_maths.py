list1 = []
def main():
    function1()


def function1():
    sum = input().split("+")
    for num in sum:
        list1.append(int(num))
    list1.sort()
    print("+".join(map(str, list1[0:(len(list1))])))

main()