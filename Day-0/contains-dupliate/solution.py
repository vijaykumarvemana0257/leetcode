class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Using a set to track seen numbers. 
        # This approach is efficient with O(n) time complexity, 
        # where n is the number of elements in the list.
        # It's better than the brute force method, which takes O(n^2) time,
        # and the sorting method,and them compating adjacent numbers which takes O(n log n) time.
        count = set()
        for i in nums:
            if i in count:
                return True  # Duplicate found
            count.add(i)
        return False  # No duplicates found
