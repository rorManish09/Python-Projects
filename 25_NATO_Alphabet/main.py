
import pandas

data  = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dictionary= {row.letter : row.code for(index,row) in data.iterrows()}

word = input("Enter a word: ").upper()

output_list=[phonetic_dictionary[letter] for letter in word]

print(output_list)
