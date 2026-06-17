class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if (sorted_s not in hash):
                hash[sorted_s] = [s]
            else:
                hash[sorted_s].append(s)
        return list(hash.values())