# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
text = "[name]"
with open("./Input/Names/invited_names.txt") as guest:
    guestlist = guest.readlines()
with open("./Input/Letters/starting_letter.txt") as letter:
    sample_letter = letter.read()
    for name in guestlist:
        name = name.strip()
        final_letter = sample_letter.replace(text, name)
        with open(f"./Output/ReadyToSend/{name}.txt","w") as email:
            email.write(final_letter)
