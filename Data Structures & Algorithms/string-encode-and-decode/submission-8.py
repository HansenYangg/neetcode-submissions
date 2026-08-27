class Solution:

    def encode(self, strs: List[str]) -> str:
        # strs = ["Hello","World"]
        # 5,5#HelloWorld --> each number is the length of that corresponding word
        # lengths and actual words separated by #
        if not strs:
            return ""
        lengths, res = [len(i) for i in strs], ""
        for length in lengths:
            res += str(length) + ","

        return res[:-1] + "---" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        arr, res, l = s.split("---"), [], 0
        nums = arr[0].split(",")
        
        for i in nums:
            num = int(i)
            res.append(arr[1][l:l + num])
            l += num

        return res
