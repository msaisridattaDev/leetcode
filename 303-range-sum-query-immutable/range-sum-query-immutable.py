class NumArray:

    def __init__(self, nums: List[int]):
        self.l=nums

        for j in range(1,len(self.l)):
            self.l[j]=self.l[j-1]+self.l[j]

    def sumRange(self, left: int, right: int) -> int:

        if left!=0:
            return self.l[right]-self.l[left-1]
        else:
            return self.l[right]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)