import pandas

data = pandas.read_csv("phonetic.csv")
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def gen_phonetic():
    word = input("Enter yout name: ").upper()
    try:
        output_list = [data_dict[letter] for letter in word]
    except KeyError:
        print("You can only enter")
        gen_phonetic()
    else:
         print(output_list)
gen_phonetic()
