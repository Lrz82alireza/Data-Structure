import sys
from collections import deque

comm_order = {"back": "popleft()", "front": "pop()", "reverse": "reverse()", "push_back" : "appendleft", "push_front" : "append" }

queue = deque()

n = int(input())

for _ in range(n):
    command = input().split()

    code = "queue." + comm_order[command[0]]
    if len(command) > 1:
        code += f"({command[1]})"
    
    try:
        result = eval(code)
        if result != None:
            print(result)
    except:
        print("No job")

