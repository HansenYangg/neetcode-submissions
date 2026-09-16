class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        at idx 6, k = 4, need it to go to 2. 10 & 8 = 2
        idx 7, k = 4, need to go to 3. 11 % 8 = 3
        """
        arr = nums.copy()

        for i in range(len(nums)):
            if i + k >= len(nums):
                nums[(i + k) % len(nums)] = arr[i]
            else:
                nums[i + k] = arr[i]

        