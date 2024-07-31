def main():
    x = get_weight()
    even(x)

def even(x):
    div = x % 2
    if div == 0:
        print("YES")
    else:
        print("NO")

def get_weight():
    while True: 
        x = int(input())
        if 1 <= x <= 100:
            break
        else:
            continue
    return x

main()
