class Solution:
    #brute force 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range (i+1,len(nums)):
                x= int(nums[i])+int(nums[j])
                if x == target:
                    return [i,j]
# using hashsets
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i in range(0,len(nums)):
            cp=target-nums[i]
            if cp in hm:
                return [i,hm[cp]]
            hm[nums[i]]=i
                        