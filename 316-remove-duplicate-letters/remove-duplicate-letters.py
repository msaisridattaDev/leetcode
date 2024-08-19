class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        

        stack=[]
        seen=set()

        last_occ={c:j for j,c in enumerate(s)}

        for i,v in enumerate(s):


            if v not in seen:
                while stack and v < stack[-1] and i< last_occ[stack[-1]]:

                    p=stack.pop()
                    seen.remove(p)
                seen.add(v)
                stack.append(v)

 

        return "".join(stack)


