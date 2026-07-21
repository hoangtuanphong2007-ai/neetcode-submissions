class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        HM1 = {}
        HM2 = {}

        for i in range(len(s)):
            HM1[s[i]] = 1 + HM1.get(s[i], 0)
            HM2[t[i]] = 1 + HM2.get(t[i], 0)

        return HM1 == HM2