import requests

word_list = []
webpage = requests.get("http://www-personal.umich.edu/~jlawler/wordlist")
word_list = webpage.text.split()

def conjugation(word_input):
    subword_count = 0
    subword_list = []
    word = []
    pointer_1 = 0
    for i in word_input:
        word.append(i)
    print(word)
    while pointer_1 < len(word)-1:
        pointer_2 = pointer_1 + 1
        while pointer_2 < len(word)+1:
            check_string = []
            check_string.append(word[pointer_1:pointer_2])
            if "".join("".join(x) for x in check_string) in word_list and len(check_string[0])>1:
                subword_list.append("".join("".join(x) for x in check_string))
                subword_count += 1
            pointer_2 += 1
        pointer_1 += 1


    return (str(subword_count) + " Subwords:", ", ".join(subword_list))

print(conjugation("Disproportionate"))
