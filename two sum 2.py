class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1
        while l<r:
            sum_=numbers[l]+numbers[r]
            if sum_==target:
                return [l+1,r+1]
            elif sum_>target:
                r-=1
            else:
                l+=1