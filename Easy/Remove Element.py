class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        counter = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[counter] = nums[j]
                counter += 1
        return counter
