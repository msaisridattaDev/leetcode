class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        self.g=""

        for i in strs:

            
            self.g+=i
            self.g+="α"

        
        return self.g        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        self.t=[]
    
        b=""
        for j in s:

            if j!="α":
                b+=j
            else:
                self.t.append(b)
                b=""


        return self.t
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))