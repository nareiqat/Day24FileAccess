# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
from typing import List, Any

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


#My solution
with open("./Input/Names/invited_names") as file:
    list1 = [line.rstrip('\n') for line in file]
    print(list1)

letters = []
with open("Input/Letters/starting_letter.txt", mode="r") as file:
    contents = file.read()
    for i in list1:
        x = contents.replace('[name]', i)
        letters.append(x)

print(letters)

for i in range(len(letters) - 1):
    with open(f"Output/ReadyToSend/letter_to_{list1[i]}", mode="w") as file:
        file.write(letters[i])


#Original solution

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names") as names_file:
    names = names_file.readlines()
    print(names)


with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    print(letter_contents)
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)