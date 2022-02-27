def is_disarium(number: int):
    digits = []
    summ = 0
    for digit in str(number):
        digits.append(int(digit))

    for i in range(len(digits)):
        summ += digits[i] ** (i + 1)

    if summ == number:
        return True
    else:
        return False
