class Room:
    def __init__(self):
        self.beds = set()
        self.beds_index = {}
        self.len_bed = 0

    def add_bed(self, args):
        x, y = args
        self.beds.add((x, y))
        self.len_bed += 1
        self.beds_index[self.len_bed] = (x, y)
        pass
    
    def remove_bed(self, index):
        if index not in self.beds_index:
            return
        bed = self.beds_index[index]
        self.beds.discard(bed)

    def farthest_bed(self, args):
        max_bed = max(self.beds, key=lambda bed: abs(bed[0] - args[0]) + abs(bed[1] - args[1]))
        max_distance = abs(max_bed[0] - args[0]) + abs(max_bed[1] - args[1])
        print(max_distance)
        pass
    
    def print_beds(self):
        print(self.beds)
        pass


q = int(input())
functions = []
room = Room()
operations = {'+' : room.add_bed, '-' : room.remove_bed, '?' : room.farthest_bed}

for _ in range(q):
    functions = input().split()
    if functions[0] == '?' or functions[0] == '+':
        y = int(functions.pop())
        x = int(functions.pop())
        functions.append((x, y))
    else:
        functions[1] = int(functions[1])
    try:
        operations[functions[0]](functions[1])
    except:
        continue

# for func in functions:
#     operations[func[0]](func[1])

