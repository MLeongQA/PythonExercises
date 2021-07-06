def numbers_to_words(number):
    number_library = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
    12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
    17: "seventeen", 18: "eighteen", 19: "nineteen"}

    tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 
    6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

    big_numbers = {
    1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion'}

    if number in number_library:
        return number_library[number]
    elif number == 0:
        return ""
    elif number < 100:
        return (tens[number//10] + " " + numbers_to_words(number-(number //10 * 10)))
    elif 100 <= number < 1000:
        if number%100 == 0:
            return (number_library[number//100]+ " hundred" )
        else:
            return (number_library[number//100]+ " hundred and " + numbers_to_words(number-(number //100 * 100)))
    else: #number >= 1000 and number not in number_library 
        count_number = number
        count = 0
        while count_number > 999:
            count += 1
            count_number /= 1000
        if (number-(int(count_number)*1000**count)) > 0:
            return (numbers_to_words(int(count_number)) + " " + big_numbers[count] + ", " + numbers_to_words(number-(int(count_number)*1000**count)))
        else:
            return ((numbers_to_words(int(count_number)) + " " + big_numbers[count]))

while True:
    print(numbers_to_words(int(input("Enter any integer: "))).capitalize())
