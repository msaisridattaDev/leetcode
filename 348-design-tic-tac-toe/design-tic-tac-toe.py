class TicTacToe:

    def __init__(self, n: int):

        self.r={}
        self.c={}
        self.n=n
        self.d1={}
        self.d2={}

        for i in range(n):
            self.r[i]=[]
            self.c[i]=[]

            self.d1[(i,i)]=""
            self.d2[(n-i-1,i)]=""

        print(self.d1,self.d2)

        

    def move(self, row: int, col: int, player: int) -> int:

        if player==1:

            if row in self.r.keys():
                self.r[row]+=["X"]
            if col in self.c.keys():
                self.c[col]+=["X"]

            if (row,col) in self.d1.keys():
                self.d1[(row,col)]="X"
            
            if (row,col) in self.d2.keys():
                self.d2[(row,col)]="X"

        else:
            if row in self.r.keys():
                self.r[row]+=["o"]
            if col in self.c.keys():   
                self.c[col]+=["o"]

            if (row,col) in self.d1.keys():
                self.d1[(row,col)]="o"
            
            if (row,col) in self.d2.keys():
                self.d2[(row,col)]="o"

        if row in self.r.keys() and len(set(self.r[row]))==2:
            self.r.pop(row)

        elif row in self.r.keys() and len(set(self.r[row]))==1 and len(self.r[row])==self.n:
            return player
        
        if col in self.c.keys() and len(set(self.c[col]))==2:
            self.c.pop(col)
        elif col in self.c.keys() and len(set(self.c[col]))==1 and len(self.c[col])==self.n:
            return player


        if len(set(self.d1.values()))==1 and len(self.d1.values())==self.n and "" not in list(self.d1.values()):
            return player

        if len(set(self.d2.values()))==1 and len(self.d2.values())==self.n and "" not in list(self.d2.values()):
            return player

        
        #print(self.d1.values(),self.d2.values())



        return 0
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)