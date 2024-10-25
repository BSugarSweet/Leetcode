class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""

        #1000
        tmp = num // 1000
        num = num % 1000
        for i in range(tmp):
             res += "M"

        #900
        if num >= 900:
            res += "CM"
            num = num % 100
        #899 ~ 500
        elif num >= 500:
            res += "D"
            num = num - 500
            tmp = num // 100
            for i in range(tmp):
                res += "C"
            num = num % 100
        #499 ~ 400
        elif num >= 400:
            res += "CD"
            num = num % 100
        #399 ~ 100
        else:
            tmp = num // 100
            for i in range(tmp):
                res += "C"
            num = num % 100

        #90
        if num >= 90:
            res += "XC"
            num = num % 10
        #89 ~ 50
        elif num >= 50:
            res += "L"
            num = num - 50
            tmp = num // 10
            for i in range(tmp):    
                res += "X"
            num = num % 10
        #49 ~ 40
        elif num >= 40:
            res += "XL"
            num = num % 10
        #39 ~ 10
        else:
            tmp = num // 10
            for i in range(tmp):    
                res += "X"
            num = num % 10

        #9
        if num >= 9:
            res += "IX"
        #8 ~ 5
        elif num >= 5:
            res += "V"
            num = num - 5
            for i in range(num):    
                res += "I"
        #4
        elif num >= 4:
            res += "IV"
        #3 ~ 1
        else:
            for i in range(num):    
                res += "I"

        return res
        
        


        