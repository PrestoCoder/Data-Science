def countVowels(sentence):
	vowels = {
		'a':0,
		'e':0,
		'i':0,
		'o':0,
		'u':0
	}
	for i in sentence:
		if i in vowels.keys():
			vowels[i] += 1

	print(vowels)