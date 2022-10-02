from art import logo
from art import alphabet

print(logo)


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        try:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        except:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % len(alphabet)
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    if input("Would you like to continue? (Y/N): ") == "Y":
        continue
    else:
        print("Thank you for using our cipher!")
        break
