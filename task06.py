sentence = "olol radar makka non"
words = sentence.split()
palindromes = [word for word in words if word == word[::-1]]
print(palindromes)
