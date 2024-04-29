class Solution:
    def twoSum(self, nums, target):  # self를 추가
        n = len(nums)
        for i in range(n):            # 0을 생략하고 range(n) 사용
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]     # 요구에 따라 인덱스를 반환
        return []                     # 요구에 따라 반환값 조정