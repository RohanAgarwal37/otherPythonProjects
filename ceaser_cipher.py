alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def ceaser(start_hex, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_hex:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            end_text += new_letter
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")


from art_ceaser import logo

print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    ceaser(start_hex=text, shift_amount=shift, cipher_direction=direction)
    result = input("Type 'yes' if you want to try again, else type 'no'.")
    if result == "no":
        should_continue = False
        print("GoodBye")
