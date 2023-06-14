def addStrings(num1, num2):
    adding_value = 0
    new_num = ""
    p1, p2 = len(num1) - 1, len(num2) - 1
    if len(num1) == 1 and len(num2) == 1:
        return str(int(num1[p1]) + int(num2[p1]))
    while p1 >= 0 and p2 >= 0:
        value1 = num1[p1]
        value2 = num2[p2]
        total_sum = int(value1) + int(value2) + adding_value
        next_value = total_sum % 10
        adding_value = total_sum // 10
        new_num += str(next_value)
        p1, p2 = p1 - 1, p2 - 1
    if p1 >= 0:
        while p1 >= 0:
            total_sum = int(num1[p1]) + adding_value
            next_value = total_sum % 10
            adding_value = total_sum // 10
            new_num += str(next_value)
            p1 -= 1
    else:
        while p2 >= 0:
            total_sum = int(num2[p2]) + adding_value
            next_value = total_sum % 10
            adding_value = total_sum // 10
            new_num += str(next_value)
            p2 -= 1
    if adding_value > 0:
        new_num += str(adding_value)
    return new_num[::-1]


num1 = '77'
num2 = '456'
print(addStrings(num1, num2))
