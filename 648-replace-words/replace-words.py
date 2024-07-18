class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        t={}
        w=""
        v=False

        dictionary.sort()

        for i in dictionary:

            if i[0]  in t.keys():
                t[i[0]]+=[i]
            else:
                t[i[0]]=[i]

        s=sentence.split()

        for j in s:

            p=j[0]

            if p in t.keys():

                for h in t[p]:

                    n=len(h)
                   # print(j,v)
                    if j[0:n]==h:
                        #print(j[0:n],h)
                        w+=h+" "
                        
                        v=True
                        break
                #print(j,v)
                if not v:
                    w+=j+" "
                else:
                    v=False
            else:
                w+=j+" "

            #print("w is",w)

        

        return w[:-1]
                



        

