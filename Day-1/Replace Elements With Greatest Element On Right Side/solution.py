class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        smax=-1
        for i in range(len(arr)-1,-1,-1):
            newMax=max(smax,arr[i])
            arr[i]=smax
            smax=newMax
        return(arr)            