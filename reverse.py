def reverse_str(num:int)->int:
    result :str= ""
    while num!=0:
        digit = num % 10
        if digit>0 :result += str(digit)
        num //=10
    return int(result)
print(reverse_str(200))
