import pandas

data = pandas.read_csv("nato_phonetic.csv")
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}


word = input("Enter your name: ").upper()
output_list = [data_dict[letter] for letter in word]
print(output_list)
