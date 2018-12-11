name_file = input("Enter name your txt file: ")

my_file = open(name_file+".txt", "r", encoding = "utf-8")
my_result = open("res.txt", "w", encoding = "utf-8")

my_text = my_file.read().lower()

for s in [",", "\"", ".", ":", "—","!", "?", ";", "(", ")", "\'","…","«","»"]:
	my_text = my_text.replace(s," ")

text_res = my_text.split()
set_word = set(text_res)
dict_word = {}
for word in set_word:
	dict_word[word] = text_res.count(word)

sort_by_frequency = sorted(dict_word.items(), key=lambda kv: kv[1])
for i in dict(sort_by_frequency):
	my_result.write(str(i)+" : "+str(dict(sort_by_frequency)[i])+"\n")

my_file.close()
my_result.close()

