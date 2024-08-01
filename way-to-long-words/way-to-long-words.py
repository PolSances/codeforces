def main():
    get_letters()


def get_letters():
    x = str(input())
    n = len(x)
    if n > 10:
        print(f"{x[0]}{n}{x[n-1]}")
    else:
        print(x)


main()
