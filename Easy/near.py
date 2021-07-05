def near(string1, string2):
    if len(string1) - len(string2) = 1:
        letter_condition = False
        count = 0
        for i in string2:
            if i == string1[count]:
                count +=1
            elif i == string1[count+1] and letter_condition == False:
                count +=2
                letter_condition = True
            else:
                return False

        return True
    else:
        return False

print(near("reset", "rest"))
print(near("dragoon", "dragon"))
print(near("eave", "leave"))
print(near("sleet", "lets"))



