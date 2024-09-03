
#############3############
class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def decode_ways(index, path):

           # print(index,path)
            if index == len(s):
                print("Valid decoding:", ' -> '.join(path))
                return 1
            if s[index] == '0':
                return 0

            if index in memo:
                # Print paths from memoization, if needed (not typical for DP)
                return memo[index]

            result = 0
            # Single character decoding
            if 1 <= int(s[index:index+1]) <= 9:
                result += decode_ways(index + 1, path + [s[index:index+1]])

            # Two character decoding
            if index + 1 < len(s) and 10 <= int(s[index:index+2]) <= 26:
                result += decode_ways(index + 2, path + [s[index:index+2]])

            memo[index] = result


            print(memo)
            return result

        total_ways = decode_ways(0, [])
        print("Total ways:", total_ways)
        return total_ways