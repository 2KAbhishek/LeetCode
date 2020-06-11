class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, hmap, maxlen = 0, {0:0}, 0
        for index, value in enumerate(nums):
            count += 2*value -1
            if count in hmap:
                maxlen = max(maxlen,index+1-hmap[count])
            else:
                hmap[count] = index+1
        return maxlen

