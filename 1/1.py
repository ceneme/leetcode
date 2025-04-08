class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashmap = {}

        for i in range(n):
            complement = target - nums[i]

            if (complement not in hashmap):
                hashmap[nums[i]] = i
        
            else:
                return [i, hashmap[complement]]

        print(hashmap)