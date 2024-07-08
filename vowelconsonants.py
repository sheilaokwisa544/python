# a program that allows you to enter an alphabet as  either
# as a vowel or a constant
l = input("input an alphabet letter :")
if l in ('a', 'e', 'i', 'o', 'u'):
    print("the letter is a vowel.")
else:
    print("the letter is a consonant.")