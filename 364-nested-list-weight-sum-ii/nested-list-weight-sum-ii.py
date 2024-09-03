# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution(object):
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:

        q = collections.deque()

        q.append((0, nestedList))

        vl = collections.defaultdict(int)
		
        d = 0
        while q:
            l, lst = q.popleft()
		
            itmlst = []
			
            for i in lst:
                if i.isInteger():
                    vl[l] += i.getInteger()
                else:
             
                    itmlst.extend(i.getList())
			
            if itmlst:
                q.append((l + 1, itmlst))
            d += 1
        
        total = 0
        
        for k, v in vl.items():
            total += (d - k) * v
            
        return total