class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = defaultdict(int)      

        for i in nums:
            if i in freq_table:
                freq_table[i] += 1
            else:
                freq_table[i] = 1

        top_keys = heapq.nlargest(k, freq_table, key = freq_table.get)

        return top_keys

        