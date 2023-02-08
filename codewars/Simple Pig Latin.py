pig_str = "Pig latin is cool"
print(new_str := " ".join(list(map(lambda word: f"{word[1:]}{word[0]}ay" if len(word) > 1 or word not in "!" else word, pig_str.split(" ")))))