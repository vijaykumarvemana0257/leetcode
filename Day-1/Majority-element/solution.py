class Solution:
    #using hash map
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        for num in nums:
            h[n]=1+h.get(n,0)
        for key,value in h.items():
            if value>len(nums)/2:
                return key
class Solution:
    # boyers alogorithm 
    def majorityElement(self, nums: List[int]) -> int:
        res,count=0,0
        # we have a count varibale to keeep track of coount
        # we increment the count if the initial res and the elemnt in teh array are same 
        # if not we will decrement 
        # if the count is 0 we will chaabge the res to the next number in that array
        for num in nums:
            if count==0:
                res=num
            count+=(1 if num==res else -1)
        return res
