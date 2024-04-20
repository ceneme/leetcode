class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(nums)

        # Time complexity is O(n), since hashmap lookups take constant time on avg.
        for i in range(n):
            complement = target - nums[i]
            if (complement not in hashmap):
                hashmap[nums[i]] = i
            else:
                return [hashmap[complement], i]

        return []
