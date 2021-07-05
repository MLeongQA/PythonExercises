def pass_or_fail(x,y,z):

    total_percentage = (int(x)+int(y)+int(z))/3

    if total_percentage >= 70:
        print("A")
    elif 70 > total_percentage >= 60:
        print("B")
    elif 60 > total_percentage >= 50:
        print("C")
    elif 50 > total_percentage >= 40:
        print("D")
    else:
        print("You failed")

pass_or_fail(input("Input your math mark: "), input("Input your chemistry mark: "), input("Input your physics mark: "))

