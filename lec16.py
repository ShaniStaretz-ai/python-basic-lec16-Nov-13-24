nums = [89, 91, 23, 34, 15, 98, 71, 99, 101]
# sort by the length of the word and then by the number itself
print("by ahadot", sorted(nums, key=lambda n: (n % 10, n)))

words = ["a b c", "z b", "x y", "z"]
# sort by number of the words
print("by number of words", sorted(words, key=lambda w: len(w.split(' '))))

personal: dict[str, object] = {'f_name': "Shani", 'l_name': "staretz",
                               "age": 36, "smoker": True, 'siblings': [29, 40],
                               'address': {
                                   'city': 'kfar sava',
                                   'street': 'haestadrot',
                                   'number': 11,
                                   'zipcode': 98765

                               }}
print("before:", personal)
print("age:", personal["age"])
personal["smoker"] = False
print("l_name:", personal['l_name'])
print("sibling 1:",personal['siblings'][0])
print("address.zipcode:",personal.get('address')['zipcode'])
personal['address']['number'] += 1
print("address.number", personal.get('address').get('number'))
del personal['address']['zipcode']
print("after:", personal)

grades_d:dict[str,int]={}
