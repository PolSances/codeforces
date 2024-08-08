def main():
    change_order()


def change_order():
    n = int(input())
    for _ in range(n):
        word = input()
        modified = word.replace(" ","")
        print(modified[3] + modified[1] + modified[2] + " " + modified[0] + modified[4] + modified[5])   


main()