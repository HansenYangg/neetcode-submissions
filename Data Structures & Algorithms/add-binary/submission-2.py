class Solution:
    def addBinary(self, a: str, b: str) -> str:
        


        if len(a) > len(b):
            a, b = b, a

        carry = False

        a = "0" * (len(b) - len(a)) + a
        res = ["0"] * len(a)

       
        for i in range(len(a) -1, -1, -1):
            if a[i] == "1" and b[i] == "1":
                if carry:
                    res[i] = "1"
        
                else:
                    carry = True
                    res[i] = "0"

            elif a[i] == "0" and b[i] == "0":
                if carry:
                    res[i] = "1"
                    carry = False
                else:
                    res[i] = "0"

            else:
                if carry:
                    res[i] = "0"
                    
                else:
                    res[i] = "1"

      
        if carry:
            return "1" + "".join(res)

        return "".join(res)








