# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c1 = defaultdict(list)
        for i in strs:
            s = "".join(sorted(i))
            c1[s].append(i)
        output = []
        for v in c1.values():
            output.append(v)
        return output
