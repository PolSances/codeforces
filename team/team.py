def main():
    veredict()
    

def veredict():
    x = 0
    n = int(input())
    for _ in range(n):
        decision = input()
        no_spaces = decision.replace(" ","")
        sum = int(no_spaces[0]) + int(no_spaces[1]) +  int(no_spaces[2])
        if sum > 1:
            x += 1
        else: 
            continue
    print(x)
            

main()