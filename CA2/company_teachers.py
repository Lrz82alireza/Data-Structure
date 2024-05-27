from collections import deque

def make_slots(arr):
    n = len(arr)
    gap = []
    stack = []
    for i, val in enumerate(arr):
        while(len(stack) != 0 and arr[stack[-1]] >= val):
            stack.pop()
        if(len(stack) == 0):
            gap.append([-1])
        else:
            gap.append([stack[-1]])
        stack.append(i)
        # print("stack: ", stack)
    
    stack.clear()
    arr.reverse()
    for i, val in enumerate(arr):
        # print(i, val)
        while(len(stack) != 0 and arr[stack[-1]] >= val):
            stack.pop()
        if(len(stack) == 0):
            gap[n - i - 1].append(n)
        else:
            gap[n - i - 1].append(n - stack[-1] - 1)
        stack.append(i)
        
    arr.reverse()
    return gap

def max_billboard(building_h, slots, n):
    max = 0
    # print(building_h)
    # print(slots)
    for i in range(n):
        temp = building_h[i] * (slots[i][1] - slots[i][0] - 1)
        if temp > max: max = temp
    return max


n = int(input())
building_h = [int(chr) for chr in input().split()]

print(max_billboard(building_h, make_slots(building_h), n))