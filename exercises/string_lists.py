word = str(input("Enter a word: "))
reversed_word = word[::-1]

if word == reversed_word:
    print("Word is a palindrome")
else:
    print("Word is not a palindrome")


'''word = input("Enter a word: ")
regular_word = []
reversed_word = []

for a in word:
    regular_word.append(a)
    reversed_word.insert(0, a)

if regular_word == reversed_word:
    print("Word is a palindrome")
else:
    print("Word is not a palindrome")
'''
