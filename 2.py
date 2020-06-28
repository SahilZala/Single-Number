class Solution(object):
    def singleNumber(self, nums):
        t = 0
        for i in range(0,nums.__len__()):
            p = 0
            for j in range(0,nums.__len__()):
                if i==j:
                    continue
                else:
                    if nums[i]==nums[j]:
                        p = 1

            if p == 0:
                t = nums[i]
        return t



s = Solution()
print (s.singleNumber([4,1,2,1,2]))