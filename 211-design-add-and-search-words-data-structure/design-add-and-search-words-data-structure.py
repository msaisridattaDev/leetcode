class WordDictionary:

    def __init__(self):
        self.root = {}
        
    def addWord(self, word: str) -> None:
        n = self.root
        for j in word:
            if j not in n:
                n[j] = {}
            n = n[j]
        n["*"] = None
        
    def search(self, word: str) -> bool:
        
        def dfs(node, index):
            if index == len(word):
                return "*" in node
            
            char = word[index]
            if char == '.':
                for key in node:
                    if key != "*" and dfs(node[key], index + 1):
                        return True
                return False
            else:
                if char in node:
                    return dfs(node[char], index + 1)
                return False
            
        return dfs(self.root, 0)
