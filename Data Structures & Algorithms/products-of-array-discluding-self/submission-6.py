class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Naive: For each element, just iterate through again to find the product. This is not O(n) though, it's O(n^2).I think i remember smth about prefix and suffix products? Yeah like, iterate through the array once and compute some products (preprocessing) before doing the rest. 

        # [1,2,4,6] -> prefix arr: [1,2,8,48], suffix arr: [48,48,24,6] or [6,24,48,48] reversed
        # Yes, each output elem would just be the product of the pref and suff sums on either side! Fucking huge. 
        pref, suff = [], []
        n = len(nums)
        curr = 1
        for i in nums:
            pref.append(i * curr)
            curr = i * curr
        curr = 1
        for j in range(1,n+1):
            elem = nums[-1*j]
            suff.append(elem * curr)
            curr = elem * curr
        result = []
        # suff = suff[::-1]
        for k in range(n):
            if k == 0:
                result.append(suff[n-2-k])
            elif k == n-1:
                result.append(pref[k-1])
            else:
                result.append(pref[k-1] * suff[n-2-k])
        return result

