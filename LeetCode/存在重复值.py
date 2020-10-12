from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        # for i in range(len(nums)):
        i=0
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                return True
            i+=1
        return False

if __name__=="__main__":
    a=Solution().containsDuplicate([1,2,1,3,4])
    print(a)