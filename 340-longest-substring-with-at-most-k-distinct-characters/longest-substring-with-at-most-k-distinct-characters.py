class Solution:
    def lengthOfLongestSubstringKDistinct(self,s: str, k: int) -> int:
        left, count = 0, {}
        for right, char in enumerate(s):
            count[char] = count.get(char, 0) + 1
            if len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
        return len(s) - left


        