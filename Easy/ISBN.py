def check_digit(digit):
    test_array = list(str(digit))
    index = 0
    total_sum = 0
    for i in test_array:
        if index%2 == 0 or index == 0:
            total_sum += int(i)
            index += 1
        else:
            total_sum += (int(i)*3)
            index += 1

    check_digit = 10 - (total_sum%10)
    print(check_digit)

check_digit(978030640615)
