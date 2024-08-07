def main():
    function()

def function():
    n = int(input())
    x = 0
    for _ in range(n):
        operation = input()
        if operation == "x++" or operation == "++x" or operation == "X++" or operation == "++X":
            x += 1
        if operation == "x--" or operation == "--x" or operation == "X--" or operation == "--X":
            x -= 1
        else:
            continue
    print(x)


main()