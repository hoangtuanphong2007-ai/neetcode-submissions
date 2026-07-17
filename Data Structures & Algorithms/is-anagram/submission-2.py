class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        HM1 = {}
        HM2 = {}

        for i in range(len(s)):
            if s[i] not in HM1:
                HM1.update({s[i]:1})
            else:
                HM1[s[i]] += 1

        for j in range(len(t)):
            if t[j] not in HM2:
                HM2.update({t[j]:1})
            else:
                HM2[t[j]] += 1

        if HM1 == HM2:
            return True
        else:
            return False