class TrieNode():

    def __init__(self):
        self.children={}
        self.end_of_the_word=False
    
    
class Trie():

    def __init__(self):
        self.root=TrieNode()
    
    
    def insert(self,word):
        
        node=self.root
        
        for char in word:
            if char not in node.children.keys():
                node.children[char]=TrieNode()
                node=node.children[char]
            else:
                node=node.children[char]
        node.end_of_the_word=True
        
    def search(self,word):
    
        Node=self.search_with_prefix(word)
        return Node is not None and Node.end_of_the_word
    
    def starts_with(self,prefix):
    
        Node=self.search_with_prefix(prefix)
        return Node is not None 
        
    def search_with_prefix(self,prefix):
    
        node=self.root
        
        for char in prefix:
            if char in node.children.keys():
                node=node.children[char]
            else:
                return None
        return node
        
    def words_with_prefix(self,prefix):
        
        Node=self.search_with_prefix(prefix)

        
        words=[]
        if Node:
            words=self.get_words_using_dfs(Node,prefix)
            
            return words
        return[]
        
    def get_words_using_dfs(self,Node,prefix):


        words=[]
        if Node.end_of_the_word:
            words.append(prefix)
    
    
        for char,node in Node.children.items():

            words+=self.get_words_using_dfs(node,prefix+char)
                
        return words
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t=Trie()
        p=products
        p.sort()

        i=0
        for i in p:
            t.insert(i)

        w=""
        res=[]
        for j in searchWord:
            w+=j
            res+=[t.words_with_prefix(w)[0:3]]

        #print(res)

        return res



