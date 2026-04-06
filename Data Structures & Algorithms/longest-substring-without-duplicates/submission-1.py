class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, maximum = 0, 0
        exist = {}
        first, second = 0, 0
        while second < len(s):
            if s[second] not in exist:
                exist[s[second]] = 1
                longest += 1
            else:
                while s[second] in exist:
                    if s[first] in exist:
                        exist.pop(s[first])
                    first += 1
                    longest -= 1
                exist[s[second]] = 1
                longest += 1
            if longest > maximum:
                maximum = longest
            second += 1
        return maximum
