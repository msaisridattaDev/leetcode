class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l=[]
        p=0

        while(p<=len(tokens)-1):

            if tokens[p].isdigit() or tokens[p][1::].isdigit():
                l.append(tokens[p])
                
            else:

                k=l.pop()
                q=l.pop()
                        
                if tokens[p]== '+':
                    a=int(k)+int(q)
                    l.append(a)
                elif tokens[p]== '-':
                    a=int(q)-int(k)
                    l.append(a)

                elif tokens[p]== '*':
                    a=int(k)*int(q)
                    l.append(a)
                else:
                    a=int(q)/int(k)
                    l.append(a)

            p+=1

        
        return int(l[0])



