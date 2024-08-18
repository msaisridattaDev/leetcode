class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        hash_map = collections.defaultdict(int)
        max_len = 0
        left=0

        for r, c in enumerate(s):
            hash_map[c] +=1

            if len(hash_map)<=k:
                max_len += 1
                print()
            else:
                hash_map[s[left]]-=1
                if hash_map[s[left]] == 0:
                    del hash_map[s[left]]
                left+=1
    

        return max_len


        