class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = sorted(s)
        tlist = sorted(t)
        return slist == tlist
                

            