import sys

class Queue:
    def __init__(self):
        self.queue = []
        pass

    def enqueue(self, value):
        self.queue.insert(0, value)
        pass

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def empty(self):
        return len(self.queue) == 0

    def one_line_str(self):
        line = ""
        for i in self.queue:
            line += str(i) + " "
        line = line[:-1]
        return line[::-1]


class Stack:
    def __init__(self, capacity=10):
        self.stack = [0 for _ in range(10)]
        self.top = -1
        pass

    def push(self, value):
        self.top += 1
        self.stack[self.top] = value
        pass

    def pop(self):
        if self.top != -1:
            self.top -= 1
        return self.stack[self.top + 1]

    def put(self, value):
        self.stack[self.top] = value
        pass

    def peek(self):
        return self.stack[self.top]

    def expand(self):
        self.stack += [0 for _ in range(len(self.stack))]
        pass

    def capacity(self):
        return len(self.stack)

    def size(self):
        return self.top + 1

    def empty(self):
        return self.top == -1

    def one_line_str(self):
        line = ""
        if self.top != -1:
            for i in range(self.top + 1):
                line += str(self.stack[i]) + " "
        return line
        


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        pass


class LinkedList:
    def __init__(self):
        self.head = None
        pass

    def insert_front(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
        pass

    def insert_back(self, value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = temp
        pass

    def reverse(self):
        pre = None
        cur = self.head

        while cur != None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        self.head = pre
        pass

    def one_line_str(self):
        temp = self.head
        line = ""
        while temp != None:
            line += str(temp.value) + " "
            temp = temp.next
        return line[:-1]


class_order = {"queue" : Queue, "stack" : Stack, "linkedlist" : LinkedList}

lines = []
for line in sys.stdin:
    if line == "\n":
        break
    lines.append(line)

for line in lines:
    
    command = line.split()

    if command[0] == "make":
        obj = class_order[command[1]]()
    elif command[0] == "call":
        code = "obj." + command[1].split('.')[1]
        result = eval(code)
        print(code, result)

    # Print the processed line
    # print("You entered:", command)