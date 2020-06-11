class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapd = {}
        for item in strs:
            key = tuple(sorted(item))
            mapd[key] = mapd.get(key, []) + [item]
        return list(mapd.values())

