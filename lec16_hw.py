# 1.sort by key
# sort strings
from random import randint
from statistics import mean

cities: list[str] = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]
# a
print("by length of word", sorted(cities, key=lambda city: len(city)))
# b
print("by number of words", sorted(cities, key=lambda city: len(city.split(' '))))
# c
print("by last character", sorted(cities, key=lambda city: city[-1]))
# d
print("by reverse word", sorted(cities, key=lambda city: city[::-1]))
# e
print("by counter of 'a's ", sorted(cities, key=lambda w: w.count('a')))
# f
cities_miles = [["Tokyo", 5760, "Asia"], ["New York", 5690, "North America"],
                ["Paris", 2050, "Europe"], ["London", 2240, "Europe"],
                ["Sydney", 8780, "Australia"],
                ["Dubai", 1300, "Asia"], ["Shanghai", 4920, "Asia"]]
# f.1.
print("by miles", sorted(cities_miles, key=lambda city: city[1]))
# f.2.
print("by miles reverse", sorted(cities_miles, key=lambda city: city[1], reverse=True))
# f.3.
print("by continent", sorted(cities_miles, key=lambda city: city[2]))
print("by continent than by miles", sorted(cities_miles, key=lambda city: (city[2], city[1])))

# sort numbers:
numbers = [randint(1, 100) for _ in range(50)]
print("by number", sorted(numbers, key=lambda n: n))
avg = mean(numbers)
print(avg)
print("by number", sorted(numbers, key=lambda n: abs(n - avg)))

# 2. dictionary:
sentence = ("This chocolate cake is rich, moist, and full of delicious chocolate flavor."
            " To make the cake, you will need chocolate, flour, sugar, eggs, and butter."
            "After baking the chocolate cake, let the cake cool before adding the chocolate frosting.")
dictionary_words: dict[str] = {}
sentence_words = sentence.replace(',', ' ').replace('.', ' ').split()
for word in sentence_words:
    dictionary_words[word] = dictionary_words.get(word, 0) + 1
else:
    print(dictionary_words)

max_word_value = None
max_word = ''
for w in dictionary_words:
    if max_word_value is None or max_word_value < dictionary_words.get(w, 0):
        max_word = w
        max_word_value = dictionary_words.get(w, 0)
else:
    print(f"the word '{max_word}' appeared {max_word_value} times in the sentence")

dictionary_characters: dict[str] = {}
for word in sentence_words:
    for c in word:
        dictionary_characters[c] = dictionary_characters.get(c, 0) + 1
else:
    print(dictionary_characters)

max_character_value = None
max_character = ''
for c in dictionary_characters:
    if max_character_value is None or max_character_value < dictionary_characters.get(c, 0):
        max_character = c
        max_character_value = dictionary_characters.get(c, 0)
else:
    print(f"the character '{max_character}' appeared {max_character_value} times in the sentence")
