class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if not nums:
        #     return False
        # counter = dict()
        # for i in nums:
        #     if i in counter:
        #         counter[i] += 1
        #     else:
        #         counter[i] = 1
        # return max(counter.values()) > 1

        # Crazy tech
        return len(set(nums)) < len(nums)