class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.usage = 0


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def check(self, word):
        node = self.root
        for i in range(len(word)):
            c = word[i]
            if c not in node.children:
                new_node = TrieNode()
                new_node.usage = 1
                node.children[c] = new_node
            else:
                if len(node.children[c].children) == 0:  # c is last char of another word
                    return False
                elif i == len(word) - 1:  # c is the last char of word
                    return False
                else:
                    node.children[c].usage += 1
            node = node.children[c]
        return True


trie = Trie()

# n = int(raw_input())
n = 4
input = [
    "aab",
    "aac",
    "aacghgh",
    "aabghgh"
]

for i in range(n):
    # word = raw_input().strip()
    word = input[i]
    if not trie.check(word):
        print "BAD SET"
        print word
        break
else:
    print "GOOD SET"
