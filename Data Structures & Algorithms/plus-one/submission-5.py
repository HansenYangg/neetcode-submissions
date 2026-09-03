class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        needCarry = False
        carry = None

        if digits[-1] == 10:
            digits[-1] = 0
            needCarry = True
            carry = 1

        i = len(digits) - 2
        while needCarry and i >= 0:
            if digits[i] + carry < 10:
                digits[i] += carry
                needCarry = False
                break
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] = digits[i] % 10
            i -= 1


        if needCarry:
            return [carry] + digits
        return digits