class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            flag = True
        else:
            flag = False
        
        if flag:
            b = abs((len(a)-len(b)))*'0'+b
        else:
            a = abs((len(a)-len(b)))*'0'+a
        print(a)
        print(b)
        result = ''
        carry = 0
        for i in range(len(a)-1, -1, -1):
            add = carry + int(a[i]) + int(b[i])
            if add == 0 or add == 1:
                carry = 0
                result+=str(add)
            elif add == 2:
                carry = 1
                result+='0'
            else:
                carry = 1
                result+='1'
        if carry:
            result+=str(carry)
        return result[::-1]



        