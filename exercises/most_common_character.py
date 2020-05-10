# Exercise to find the most common character in a sentence
sentence = "This is a common interview question"

character_frequency = {}

for character in sentence:
    if character in character_frequency:
        character_frequency[character] += 1
    else:
        character_frequency[character] = 1

result = sorted(character_frequency.items(),
                key=lambda kv: kv[1],
                reverse=True)

print(result[0])
