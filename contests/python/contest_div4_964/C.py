def main():
    function()
 
def function():
    my_list = []
    t = int(input())
    for _ in range(t):
        numbers = input()
        numbers_wo_spaces = numbers.replace(" ", "")
        n = int(numbers_wo_spaces[0])
        s = int(numbers_wo_spaces[1])
        if len(numbers) > 3:
            m = str(numbers_wo_spaces[2] + numbers_wo_spaces[3])
            realm = int(m)
        else:
            realm = int(numbers_wo_spaces[2])
        for _ in range(n):
            tasktime = input()
            tasktime_wo = tasktime.replace(" ", "")
            my_list.append(int(tasktime_wo[0]))
            if len(tasktime_wo) > 1:
                my_list.append(int(tasktime_wo[1]))
        if my_list[0] >= s or my_list[2] - my_list[1] >= s or my_list[4] - my_list[3] >= s or realm - my_list[5] >= s:
            print("YES")
        else:
            print("NO")
        my_list.clear()


main()
 