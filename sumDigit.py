def sumDigit(anInt):
    num1 = anInt%10
    ##print(num1)
    num2 = (anInt // 10) % 10
    ##print(num2)
    num3 = ((anInt // 10) // 10) % 10
    ##print(num3)
    num4 = (((anInt // 10) // 10) // 10)% 10
    ans = num1 + num2 + num3 + num4
    return ans
