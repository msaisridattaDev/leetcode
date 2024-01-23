class SparseVector:
    def __init__(self, nums: List[int]):
        self.d={}

        for i,v in enumerate(nums):

            if v!=0:
                self.d[i]=v

        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:

        w=0
        for i in self.d.keys():
            if i in vec.d.keys():  
                w+=self.d[i]*vec.d[i]
                
        return w
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)