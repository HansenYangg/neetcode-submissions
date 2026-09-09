class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # start from index 0, iterate up to index n (exclusive), swapping the elements with the elements in nums2
        # now have start index and end index incremented by n each, swapping the next n elements

        # [10, 20, 30, 40, 0, 0] // [10, 30]
        if not n:
            return
          
        last = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums2[n - 1] > nums1[m - 1]
                nums1[last] = nums2[n - 1]
                n -= 1

            last -= 1

        while m > 0:
            nums1[last] = nums1[m - 1]
            last -= 1
            m -= 1

        while n > 0:
            nums1[last] = nums2[n - 1]
            last -= 1
            n -= 1

           






        