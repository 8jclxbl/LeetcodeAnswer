class Node:
    def __init__(self, val, is_word=False):
        self.val = val
        self.is_word = is_word
        self.next_ = {}

    def add(self, node):
        key = node.val
        self.next_[key] = node

    def to_word(self):
        self.is_word = True


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base = Node("")

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.base
        for i in word:
            if i in cur.next_:
                node = cur.next_[i]
            else:
                node = Node(i)
                cur.add(node)
            cur = node
        cur.to_word()

    def search_base(self, word):
        cur = self.base
        for i in word:
            if i in cur.next_:
                cur = cur.next_[i]
            else:
                return False, cur
        return True, cur

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        first_step, cur = self.search_base(word)
        if not first_step:
            return False
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        first_step, cur = self.search_base(prefix)
        return first_step


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == "__main__":
    solution = Trie()
    operations = [
        "insert", "insert", "insert", "insert", "insert", "insert", "search",
        "search", "search", "search", "search", "search", "search", "search",
        "search", "startsWith", "startsWith", "startsWith", "startsWith",
        "startsWith", "startsWith", "startsWith", "startsWith", "startsWith"
    ]
    params = [["app"], ["apple"], ["beer"], ["add"], ["jam"], ["rental"],
              ["apps"], ["app"], ["ad"], ["applepie"], ["rest"], ["jan"],
              ["rent"], ["beer"], ["jam"], ["apps"], ["app"], ["ad"],
              ["applepie"], ["rest"], ["jan"], ["rent"], ["beer"], ["jam"]]
    for f, v in zip(operations, params):
        a = getattr(solution, f)
        print(a(v[0]))
