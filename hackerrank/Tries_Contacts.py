from collections import defaultdict


class Node(object):
    __slots__ = ['children', 'num_usage']  # save memory

    def __init__(self):
        self.children = defaultdict(Node)  # good
        self.num_usage = 0


class Trie(object):
    def __init__(self):
        self.root = Node()

    def add(self, word):
        node = self.root
        for char in word:
            node = node.children[char]   # default node
            node.num_usage += 1

    def find(self, partial):
        node = self.root
        for char in partial:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.num_usage


class TireNode:
    def __init__(self):
        self.children = {}
        self.count = 0


class Tire(object):
    def __init__(self):
        self.root = TireNode(None)

    def add(self, name):
        node = self.root

        for char in name:
            if char in node.children:
                node = node.children[char]
                node.count += 1
            else:
                new_node = TireNode()
                node.children[char] = new_node
                node = new_node

    def find(self, name):
        node = self.root
        for char in name:
            if char in node.children:
                node = node.children[char]
            else:
                return 0
        return node.count


class TireNode:
    def __init__(self, char):
        self.children = [None for i in range(26)]
        self.char = char
        if self.char:
            self.count = 1
        else:
            self.count = 0


class Tire(object):
    def __init__(self):
        self.root = TireNode(None)

    def add(self, name):
        node = self.root6

        for char in name:
            if node.children[ord(char) - ord("a")]:
                node = node.children[ord(char) - ord("a")]
                node.count += 1
            else:
                new_node = TireNode(char)
                node.children[ord(char) - ord("a")] = new_node
                node = new_node

    def find(self, name):
        if not name:
            return 0

        node = self.root
        for char in name:
            if node.children[ord(char) - ord("a")]:
                node = node.children[ord(char) - ord("a")]
            else:
                return 0
        return node.count


'''
add hack
add hackerrank
find hac
find hak

out put
2
0
'''

contacts = Tire()
# contacts.add("hack")
# contacts.add("hackerrank")
# contacts.add("abc")
# contacts.add("abd")
print contacts.find("wdgy")
print contacts.find("hak")
print contacts.find("ab")
