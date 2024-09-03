
def main():
    function1()

def function1():
    t = input()
    for i in range(int(t)):
        n = input()
        notes = []
        for i in range(int(n)): 
            list1 = []
            line = str(input())
            list1.append(line)
            for i in range(0, len(line)):
                if "#" == line[i]:
                    notes.append(i+1)
                else:
                    continue
        print(" ".join(map(str, notes[::-1])))



            
        
        

main()