class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result =[]
        for i in range(len(nums)):
            flag = 0
            for j in range(len(nums)-1, 0, -1):
                if i < j:
                    if (nums[i] + nums[j]) == target:
                        result.append(i)
                        result.append(j)
                        flag = 1
                        break
                if flag == 1:
                    break
        return result