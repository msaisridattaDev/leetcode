class TrieNode:
    def __init__(self):

        self.children={}
        self.is_it_end_of_word=False


class Trie:

    def __init__(self):

        self.root=TrieNode()
        

    def insert(self, word: str) -> None:

        node=self.root

        for j in word:
            if j not in node.children:
                node.children[j]=TrieNode()
            node=node.children[j]


        node.is_it_end_of_word=True 

    def search(self, word: str) -> bool:

        node=self.root

        for j in word:
            if j not in node.children:
                return False
            node=node.children[j]

        return node.is_it_end_of_word

    def startsWith(self, prefix: str) -> bool:

        node=self.root

        for j in prefix:
            if j not in node.children:
                return False
            node=node.children[j]

        return True


        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)