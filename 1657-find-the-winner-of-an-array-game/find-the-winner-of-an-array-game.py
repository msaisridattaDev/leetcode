class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        w=0
        m=0

        if k > len(arr):
            return max(arr)
        while(w<k):

            if arr[0]<arr[1]:
                #print(arr[0],arr[1],m,"if",arr)
                

                if m!=arr[1]:
                  
                    m=arr[1]
                    w=1
                else:

                    w+=1
                arr.append(arr.pop(0))
                
                
            else:
                #print(arr[0],arr[1],m,"else",arr)

            

                if m!=arr[0]:
                  
                    m=arr[0]
                    w=1
                else:
                    w+=1

                arr.append(arr.pop(1))
         

        return m

