class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Optimal is prolly using a min/max heap
        # rank = dict()
        # for i in nums:
        #     if i in rank.keys():
        #         rank[i] += 1
        #     else:
        #         rank[i] = 1
        # sort = list(reversed(sorted(rank.keys(), key=lambda x: rank[x])))
        # return sort[:k]

        # Works but most optimal: Bucket sort. 
        # Why better? Bc no need to sort the dict keys manually for worst case nlogn time. Instead can just create buckets right away (O(n) space) and iterate in reverse order for O(n) time. 

        buckets = [[] for _ in range(len(nums)+1)]
        rank = dict() # O(n) space
        for i in nums:
            if i in rank.keys():
                rank[i] += 1
            else:
                rank[i] = 1
        # Bucket: index is num times those numbers r repeated
        # Rank: mapping from each num to its num times seen.
        # TODO: Use rank to fill out buckets
        # dude wtf 
        for num, seen in rank.items():
            buckets[seen].append(num)
            # Super easy
        # Now its homestretch -- iterate in reverse order
        result = []
        for j in range(len(nums),0,-1):
            for e in buckets[j]:
                result.append(e)
                if len(result) == k:
                    return result


