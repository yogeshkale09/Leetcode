class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        
        # Loop through the array
        for i, num in enumerate(nums):
            # Calculate the complement by subtracting the current number from the target
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in num_to_index:
                # Return the indices if a match is found
                return [num_to_index[complement], i]
            
            # Store the current number and its index in the dictionary
            num_to_index[num] = i
        