class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = i = 0
        while i < len(nums):
            if i == len(nums) - 1:
                score += nums[i]
                break

            if nums[i] <= nums[i + 1]:
                score += nums[i]
                i += 2
            else:
                i += 1
                if i == len(nums) - 1:
                    score += nums[i]
                    break

                if nums[i] <= nums[i + 1]:
                    score += nums[i]
                    i += 2
                elif nums[i] > nums[i + 1]:
                    # decreasing block search
                    i += 1
                    j = 3
                    odd, even = nums[i - 2] + nums[i], nums[i - 1]
                    if i == len(nums) - 1:
                        score += odd
                        break

                    while nums[i] > nums[i + 1]:
                        i += 1
                        j += 1
                        if j % 2 == 0:
                            even += nums[i]
                        else:
                            odd += nums[i]

                        if i == len(nums) - 1:
                            score += even if j % 2 == 0 else odd
                            return score

                    score += even if j % 2 == 0 else odd
                    i += 2
                else:
                    score += nums[i - 1]
                    i += 1

        return score
            
        