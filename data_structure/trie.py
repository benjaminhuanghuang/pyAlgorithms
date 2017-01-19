# http://www.jiuzhang.com/solutions/word-search-ii/
class Trie_9:
    def __init__(self):
        self.children = {}
        self.flag = False
        self.hasWord = False

    def put(self, key):
        if key == '':
            self.flag = True
            self.hasWord = True
            return

        if key[0] not in self.children:
            self.children[key[0]] = Trie_9()
        self.children[key[0]].put(key[1:])
        self.hasWord = True

    def pop(self, key):
        if key == '':
            self.flag = False
            self.hasWord = False
            return
        if key[0] not in self.children:
            return
        self.children[key[0]].pop(key[1:])
        # if any child.hasWord is true
        self.hasWord = any([child.hasWord for child in self.children.values()])

    def has(self, key):
        if key == '':
            return self.flag

        if not self.hasWord:
            return False
        if key[0] not in self.children:
            return False
        return self.children[key[0]].has(key[1:])


class TireNode:
    def __init__(self, char):
        self.children = []
        self.char = char

