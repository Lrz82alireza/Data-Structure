class Bst:
    class Node:
        def __init__(self, value, p = None, l = None, r = None):
            self.value = value
            self.l = l
            self.r = r
            self.p = p
        pass

    def __init__(self):
        self.root = None
        pass

    def set_root(self, node):
        if node == None:
            return None
        cur = node
        while True:
            if cur.p == None:
                break
            cur = cur.p
        pass
        self.root = cur

    def find(self, key):
        if self.root == None:
            return None
        
        result = None

        cur = self.root
        while True:
            if key < cur.value:
                if cur.l == None:
                    break
                cur = cur.l

            elif key > cur.value:
                if cur.r == None:
                    break
                cur = cur.r
            
            else:
                result = cur
                break
        return result

    def insert(self, key):
        if self.root == None:
            self.root = Bst.Node(key)
            return

        cur = self.root
        while True:
            if key < cur.value:
                if cur.l == None:
                    cur.l = Bst.Node(key, p = cur)
                    break
                cur = cur.l
            else:
                if cur.r == None:
                    cur.r = Bst.Node(key, p = cur)
                    break
                cur = cur.r
        pass

    def inorder(self, root = None, first = True):
        if first:
            root = self.root
            first = False
            self.inorder_out = ''
        if root == None:
            return

        self.inorder(root.l, False)
        self.inorder_out += str(root.value) + ' '
        self.inorder(root.r, False)

        return self.inorder_out
        pass


n = int(input())

cities = {}
city = {}
bst = Bst()

for i in range(n):
    city[i] = [int(x) for x in input().split()]
    cities[i + 1] = Bst.Node(city[i][0])

for i in range(n):
    parent = cities[i + 1]
    left = city[i][1]
    right = city[i][2]
    if left != -1:
        cities[i + 1].l = cities[left]
        cities[left].p = parent
    if right != -1:
        cities[i + 1].r = cities[right]
        cities[right].p = parent

bst.set_root(cities[1])

mistakes = 0
for i in range(n):
    test = bst.find(city[i][0]) == None
    if test:
        mistakes += 1
print(mistakes)

