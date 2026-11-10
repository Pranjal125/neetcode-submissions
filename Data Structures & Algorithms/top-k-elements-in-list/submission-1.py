class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={} #dict
        for n in nums:
            counts[n] = counts.get(n,0)+1

        ranked = sorted(counts.keys(),          # Action 1: rank by count
                        key=lambda n: counts[n],
                        reverse=True)

        return ranked[:k]
        