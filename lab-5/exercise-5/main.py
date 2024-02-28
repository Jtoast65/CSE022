def sumOfDigits(n):
    if n < 0:
        return('Invalid entry')
    else:
        sum = 0
        for i in str(n):
            sum += int(i)
        return sum
    


s = sumOfDigits(425)
print(s)