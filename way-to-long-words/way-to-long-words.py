def main():
    input_user()


def input_user():
    n = int(input())
    for _ in range(n):
        palabra = input()
        if len(palabra) > 10:
            abreviacion = palabra[0] + str(len(palabra) - 2) + palabra[-1]
            print(abreviacion)
        else:
            print(palabra)

main()