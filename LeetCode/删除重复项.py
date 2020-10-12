from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        for i in range(len(nums)):
            if nums[i]!=nums[j]:
                j+=1
                if i-j>0:
                    nums[j]=nums[i]
            # print(nums)
        return nums[:j+1]




if __name__=="__main__":
    a=Solution().removeDuplicates([1,1,1,2,2,3])
    print(a)