class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        unique = defaultdict(list)
        results= []
        for i in strs:
            v = "".join(sorted(i))
            if(v not in unique):
                unique[v] = []
                unique[v].append(i)
            else:
                unique[v].append(i)
        
        for key, value in unique.items():
            results.append(value)

        return results
