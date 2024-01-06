class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        v=len(nums1)-1

        p2=len(nums2)-1

        p1=v-p2-1


        while(v>=0):

            if p1==-1:
                break

            if p2==-1:
                break

            if nums1[p1]>=nums2[p2]:
                nums1[v]=nums1[p1]
                v-=1
                p1-=1
            else:
                nums1[v]=nums2[p2]
                v-=1
                p2-=1



        if p1==-1:
            while(v>=0 and p2>=0):
                nums1[v]=nums2[p2]
                p2-=1
                v-=1

        else:
            while(v>=0 and p1>=0):
                nums1[v]=nums1[p1]
                p1-=1
                v-=1

        
        