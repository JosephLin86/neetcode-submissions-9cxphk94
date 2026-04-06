class Solution:
    def isValid(self, s: str) -> bool:
        stackArray = []
        dictset = { "}" : "{", "]" : "[", ")" : "("}
        for i in range(len(s)):
            if s[i] in dictset:
                if not stackArray or stackArray.pop() != dictset[s[i]]:
                    return False
            else:
                stackArray.append(s[i])
        
        return not stackArray