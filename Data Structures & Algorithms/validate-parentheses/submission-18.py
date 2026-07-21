class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        HM = {'(':')', '[':']', '{':'}'}
        lst = []
        for i in range(len(s)):
            if(s[i] == '(' or s[i] == '[' or s[i] == '{'):
                lst.append(s[i])
            else:
                if(len(lst) == 0): return False
                else:
                    k = lst.pop()
                    if s[i] != HM[k]:
                        return False
        return len(lst) == 0