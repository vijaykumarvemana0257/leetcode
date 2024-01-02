class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        o=s.split()
        return(len(o[len(o)-1]))
            
        


        