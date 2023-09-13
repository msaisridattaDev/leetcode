class Solution:
    def arrangeWords(self, text: str) -> str:

        t={}
        s=""
        text=text[0].lower()+text[1::]
        for i in text.split():
            p=len(i)
        
            if p in t.keys():
                t[p]+=[i]
            else:
                t[p]=[i]

        for w in sorted(t.items()):
            s+=" ".join(w[1])
            s+=" "

        text=(s[0].upper()+s[1::]).rstrip()
        
        return text

