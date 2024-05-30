



import re

INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'


class MinHeap:
    # class Node:
    #     pass

    def __init__(self):
        self.heap = list()
        self.len = 0
        pass

    def bubble_up(self, index):
        if type(index) != int:
            raise Exception(INVALID_INDEX)
        if index < 0 or index >= self.len:
            raise Exception(OUT_OF_RANGE_INDEX)
        if self.len == 0:
            raise Exception(EMPTY)
        while index > 0:
            parent = ((index + 1) // 2) - 1
            if parent >= 0 and self.heap[parent] > self.heap[index]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            else:
                break
            index = parent
        pass

    def bubble_down(self, index):
        if type(index) != int:
            raise Exception(INVALID_INDEX)
        if index < 0 or index >= self.len:
            raise Exception(OUT_OF_RANGE_INDEX)
        if self.len == 0:
            raise Exception(EMPTY)
        
        left = 2 * (index + 1) - 1
        right = 2 * (index + 1)
        min_index = index

        if left < self.len:
            if self.heap[left] < self.heap[min_index]:
                min_index = left

        if right < self.len:
            if self.heap[right] < self.heap[min_index]:
                min_index = right

        if min_index != index:
            self.heap[min_index], self.heap[index] = self.heap[index], self.heap[min_index]
            self.bubble_down(min_index)

        pass

    def heap_push(self, value):
        self.heap.append(value)
        self.len += 1
        self.bubble_up(self.len - 1)
        pass

    def heap_pop(self):
        if self.len == 0:
            raise Exception(EMPTY)
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        ret_val = self.heap.pop()
        self.len -= 1
        if self.len != 0:
            self.bubble_down(0)
        return ret_val

    def find_min_child(self, index):
        if type(index) != int:
            raise Exception(INVALID_INDEX)
        if index < 0 or index >= self.len:
            raise Exception(OUT_OF_RANGE_INDEX)
        if self.len == 0:
            raise Exception(EMPTY)
        left = 2 * (index + 1) - 1
        right = 2 * (index + 1)

        if right >= self.len:
            if left < self.len:
                return left
        if left >= self.len:
            if right < self.len:
                return right
        else:
            return right if self.heap[right] < self.heap[left] else left

    def heapify(self, *args):
        for arg in args:
            self.heap_push(arg)


class HuffmanTree:
    class Node:
        def __init__(self, value, char = None, l = None, r = None, p = None):
            self.value = value
            self.char = char
            self.l = l
            self.r = r
            self.p = p
        pass

    def __init__(self):
        self.letters = list()
        self.repetitions = list()
        pass

    def set_letters(self, *args):
        self.letters.extend(args)
        pass

    def set_repetitions(self, *args):
        self.repetitions.extend(args)
        pass

    def build_huffman_tree(self):
        self.chars = list(zip(self.letters, self.repetitions))
        self.chars.sort(key = lambda x: x[1])
        nodes = [HuffmanTree.Node(x[1], x[0]) for x in self.chars]
        while len(nodes) > 1:
            nodes.sort(key = lambda x: x.value)
            l = nodes.pop(0)
            r = nodes.pop(0)
            nodes.append(HuffmanTree.Node(l.value + r.value, l = l, r = r))
            l.p = nodes[-1]
            r.p = nodes[-1]
        
        self.code = dict()
        self.code_cost(nodes[0])
        pass

    def code_cost(self, tree, code = ''):
        if tree == None:
            return
        if tree.char != None:
            self.code[tree.char] = code
            return

        self.code_cost(tree.l, code + '0')
        self.code_cost(tree.r, code + '1')
        pass

    def get_huffman_code_cost(self):
        result = 0
        for char in self.chars:
            result += len(self.code[char[0]]) * char[1]
        return result

    def text_encoding(self, text):
        letter_count = dict()

        for letter in text:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        
        self.letters = list(letter_count.keys())
        self.repetitions = list(letter_count.values())
        self.build_huffman_tree()


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


class Runner:
    dsMap = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

    def __init__(self, inputSrc):
        self.input = inputSrc
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            actionMethod = getattr(self, action, None)
            if actionMethod is None:
                return
            actionMethod(param)

    def make(self, params):
        itemType, itemName = params.split()
        self.items[itemName] = self.dsMap[itemType]()

    def call(self, params):
        regexRes = self.callRegex.match(params)
        itemName, funcName, argsList = regexRes.groups()

        args = [x.strip() for x in argsList.split(',')] if argsList != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[itemName], funcName)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
