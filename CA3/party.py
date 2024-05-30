import sys
import heapq

class Room:
    def __init__(self):
        self.beds = []

    def add_bed(self, args):
        self.beds.append([args[0], args[1]])
        pass
    
    def remove_bed(self, index):
        if index > len(self.beds) or index <= 0:
            return
        self.beds.pop(index - 1)
        pass

    def farrest_bed(self, args):
        max = 0
        for bed in self.beds:
            if abs(bed[0] - args[0]) + abs(bed[1] - args[1]) > max:
                max = abs(bed[0] - args[0]) + abs(bed[1] - args[1])
        print(max)
        pass
    
    def print_beds(self):
        print(self.beds)
        pass


q = int(input())
functions = []
room = Room()
operations = {'+' : room.add_bed, '-' : room.remove_bed, '?' : room.farrest_bed}

for _ in range(q):
    functions.append(input().split())
    if functions[-1][0] == '?' or functions[-1][0] == '+':
        y = int(functions[-1].pop())
        x = int(functions[-1].pop())
        functions[-1].append((x, y))
    else:
        functions[-1][1] = int(functions[-1][1])
    try:
        operations[functions[-1][0]](functions[-1][1])
    except:
        continue

# for func in functions:
#     operations[func[0]](func[1])

