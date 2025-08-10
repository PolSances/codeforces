def main():
    function1()

def function1():
    size = input().split()
    width = int(size[0])
    height = int(size[1])
    area = width*height
    dominoes = area//2
    print(dominoes)
    
main()