from collections import deque

def max_billboard(building_h):
    temp = 0
    hight = []
    weight = []
    max = 0
    for val in building_h:
        if len(hight) != 0:
            if hight[-1] < val:
                hight.append(val)
                weight.append(1)
            else:
                temp = 0
                while(len(hight) != 0 and hight[-1] >= val):
                    s = hight[-1] * (weight[-1] + temp)
                    temp = temp + weight[-1]
                    if s > max: max = s
                    hight.pop()
                    weight.pop()
                hight.append(val)
                weight.append(temp + 1)
        else:
            hight.append(val)
            weight.append(1)

    temp = 0
    while(len(hight) != 0):
        s = hight[-1] * (weight[-1] + temp)
        temp = temp + weight[-1]
        if s > max: max = s
        hight.pop()
        weight.pop()
    return max
        


n = int(input())
building_h = [int(chr) for chr in input().split()]

print(max_billboard(building_h))