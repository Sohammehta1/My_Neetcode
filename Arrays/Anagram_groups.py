class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group_index = {}
        groups = []
        for i,s in enumerate(strs):
            temp = ''.join(sorted(s))
            if temp in group_index.keys():
                groups[group_index[temp]].append(s)
            else:
                groups.append([s])
                group_index[temp] = len(groups)-1
        return groups
