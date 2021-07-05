def timestable(digit):
    if digit > 0:
        timestable_array = []
        multiplication_factor = 1
        while digit >= multiplication_factor:
            array2 = []
            count = 1
            while digit >= count:
                array2.append(count*multiplication_factor)
                count += 1
            multiplication_factor += 1
            timestable_array.append(array2)
        for i in timestable_array:
            print(*i, sep = " ")
    else:
        print("Choose a integer other than 0")

timestable(10)
