# Go to the output folder and delete all the letter except main.py

PLACEHOLDER = '[name]'
with open("ENTER THE PATH OF invited_names.txt FILE FROM THE Names FOLDER") as names_file:

    names = names_file.readlines()

with open("ENTER THE PATH OF starting_letter.txt FROM Letters") as letter_file:

    letter_contents = letter_file.read()

    for name in names:

        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        with open(f"Output/ReadyToSend/letter_for_{stripped_name}","w") as ready_letter:

                ready_letter.write(new_letter)