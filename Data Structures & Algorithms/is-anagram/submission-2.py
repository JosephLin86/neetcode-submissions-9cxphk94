class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in counter:
                counter[s[i]] = 1
            else:
                counter[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in counter or counter[t[i]] == 0:
                return False
            counter[t[i]] -= 1
        return True