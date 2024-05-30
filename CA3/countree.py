class Tree:
    class Node:
        def __init__(self, value, l = None, r = None):
            self.value = value
            self.l = l
            self.r = r

    def __init__(self):
        self.root = None
        pass

    def insert(self, value, left, right):
        if self.root == None:
            l = Tree.Node(None if left == -1 else left)
            r = Tree.Node(None if right == -1 else right)
            self.root = Tree.Node(value, l, r)
            return

        temp = self.find(value)

        if temp == None:
            self.root = Tree.Node(value, left, right)

        # cur = self.root
        # while True:
        #     if value < cur.value:
        #         if cur.l == None:
        #             cur.l = Tree.Node(value, p = cur)
        #             break
        #         cur = cur.l
        #     else:
        #         if cur.r == None:
        #             cur.r = Tree.Node(value, p = cur)
        #             break
        #         cur = cur.r
        pass

    def find(self, value):
        if self.root == None:
            return None
        cur = self.root
        while cur != None:
            if value < cur.value:
                cur = cur.l
            elif value > cur.value:
                cur = cur.r
            else:
                return cur
        return None

n = int(input())

tree = Tree()

for i in range(n):
    tree.insert(int(input()))
