def sponge_case():
    user_input = input("Enter your text here: ")
    spongebob_text = ""
    for i, char in enumerate(user_input):
        if i % 2 == 0:
            spongebob_text += char.upper()
        else:
            spongebob_text += char.lower()
    print(spongebob_text)
    
sponge_case()

def exit():
    exit_input = input("Do you want to exit? y/n: ")
    if exit_input == "y" or "Y":
        exit()
    else:
        sponge_case()