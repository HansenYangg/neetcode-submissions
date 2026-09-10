class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens, twenties = 0, 0, 0
        for bill in bills:
            if bill == 5:
                fives += 1

            elif bill == 10:
                if not fives:
                    return False
                tens, fives = tens + 1, fives - 1

            else:
                if fives < 3 and (fives < 1 or tens < 1):
                    return False
                if fives >= 3:
                    twenties, fives = twenties + 1, fives - 3
                else:
                    twenties, fives, tens = twenties + 1, fives - 1, tens - 1


        return True

    