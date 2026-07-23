class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        lst = []
        while(i < j):
            if numbers[i] + numbers[j] > target:
                j-=1
            elif numbers[i] + numbers[j] < target:
                i+=1
            elif numbers[i] + numbers[j] == target:
                lst.append(i+1)
                lst.append(j+1)
                break
        return lst