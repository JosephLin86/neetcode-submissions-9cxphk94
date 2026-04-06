class Solution:
    def isPalindrome(self, s: str) -> bool:
        first, last = 0, len(s)-1
        while first < last:
            while first < last and s[first].isalnum() == False:
                first += 1
            while first < last and s[last].isalnum() == False:
                last -= 1

            
            if s[first].lower() != s[last].lower():
                return False
            first += 1
            last -= 1
            
        return True