class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Optimal is prolly using a min/max heap
        rank = dict()
        for i in nums:
            if i in rank.keys():
                rank[i] += 1
            else:
                rank[i] = 1
        sort = list(reversed(sorted(rank.keys(), key=lambda x: rank[x])))
        return sort[:k]