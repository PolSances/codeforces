list1 = []
list2 = []

def main():
    function1()

def function1():
    while True:
        t = int(input())
        if 1 <= t <= 500:
            break
        else: 
            continue
    for i in range(t):
        n = int(input())
        s = input()
        string_lenght = n//2
        k = int(n/string_lenght)
        for i in range(n):
            list1.append(s[i])
        if k >= 2 and s[0] != s[len(s)-1]:
            print("YES")
        else:
            print("NO")

    
main()
