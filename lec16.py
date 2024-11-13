nums=[89,91,23,34,15,98,71,99,101]
#sort by the length of the word and then by the number itself
print("by ahadot", sorted(nums,key=lambda n:(n%10,n)))

words=["a b c","z b","x y","z"]
#sort by number of the words
print("by number of words", sorted(words,key=lambda w:len(w.split(' '))))