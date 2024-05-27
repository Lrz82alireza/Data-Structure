from collections import deque

def is_value(str):
    stack = deque()

    for chr in str:
        if chr.islower():
            n = len(stack)

            if n == 0:
                return False
            
            flag = False
            for _ in range(n):
                if (stack.pop().lower() == chr):
                    flag = True
                    break
            if not flag:
                return False
        else:
            stack.append(chr)
    
    return True if len(stack) == 0 else False

substring = []

serie = input()
n = int(input())

for i in range(n):
    substring.append(input().split())

serout = ""

for sub in substring:
    if is_value(serie[int(sub[0])-1:int(sub[1])]):
        serout += "1"
    else: serout += "0"
print(serout)