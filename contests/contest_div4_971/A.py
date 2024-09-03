def main():
    function1()

def function1():
    t = int(input())
    for _ in range(t):
        list1 = []
        numbers = input().split(" ")
        a = int(numbers[0])
        b = int(numbers[1])
        for j in range(a, b + 1):
            list1.append((j - a) + (b - j))
        print(min(list1))

main()
