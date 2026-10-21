class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedstrs = []
        ans = []
        for i in strs:
            if sorted(i) not in sortedstrs:
                sortedstrs.append(sorted(i))
                ans.append([])
            ans[sortedstrs.index(sorted(i))].append(i)
        return ans



        