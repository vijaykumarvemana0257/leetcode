class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        for num in nums:
            h[n]=1+h.get(n,0)
        for key,value in h.items():
            if value>len(nums)/2:
                return key
