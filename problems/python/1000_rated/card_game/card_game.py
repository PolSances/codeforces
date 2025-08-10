def main():
    function()

def function():
    t = int(input())
    for i in range(t):
        w = 0
        result = (input()).strip()
        normal = result.split(" ")
        if int(normal[0]) > int(normal[2]) and int(normal[1]) > int(normal[3]):
            w += 1
        if int(normal[0]) > int(normal[3]) and int(normal[1]) >int(normal[2]):
            w += 1
        if int(normal[1]) > int(normal[2]) and int(normal[0]) >int(normal[3]):
            w += 1
        if int(normal[1]) > int(normal[3]) and int(normal[0]) >int(normal[2]):
            w += 1
        print(w)
        t -= 1
main()