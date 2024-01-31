def sponge_case():
    user_input = input("Enter your text here: ")
    spongebob_text = ""
    for i, char in enumerate(user_input):
        if i % 2 == 0:
            spongebob_text += char.upper()
        else:
            spongebob_text += char.lower()
    print(spongebob_text)

while True:
    sponge_case()

    exit_input = input("Do you want to exit? Y/N: ")
    if exit_input.upper() == "Y":
        break