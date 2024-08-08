def main():
    function()

def function():
    t = int(input())
    while t > 0:
        w = 0
        result = str(input())
        normal = result.replace(" ","")
        if t != 3 and t != 2:
            if int(normal[0]) > int(normal[2]) and int(normal[1]) > int(normal[3]):
                w += 1
            if int(normal[0]) > int(normal[3]) and int(normal[1]) >int(normal[2]):
                w += 1
            if int(normal[1]) > int(normal[2]) and int(normal[0]) >int(normal[3]):
                w += 1
            if int(normal[1]) > int(normal[3]) and int(normal[0]) >int(normal[2]):
                w += 1
            print(w)
main()