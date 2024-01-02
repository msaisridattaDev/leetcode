class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        t=[]

        for i in range(len(words)):

            if x in words[i]:
                t.append(i)

        return t