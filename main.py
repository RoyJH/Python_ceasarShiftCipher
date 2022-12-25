from art import logo


def ceasar(direction, text, shift):
    alphabet_shift = []
    if shift > 26:
        shift = shift % 26
        n = shift % 26
    else:
        n = shift
    new_text = text
    for letter in alphabet:
        if int(n) < 26 and n >= shift:
            alphabet_shift.append(alphabet[n])
            n += 1
        elif int(n) >= 26:
            alphabet_shift.append(alphabet[n - 26])
            n += 1
    new_text = list(new_text)
    i = 0
    for letter in new_text:
        if direction == "encode":
            if letter in alphabet:
                assign = alphabet.index(letter)
            if letter == alphabet[assign]:
                new_text[i] = alphabet_shift[assign]
                i += 1
            else:
                new_text[i] = letter
                i += 1
            # print(f"The {direction}d message is:")
            # print(''.join(new_text))
        elif direction == "decode":
            if letter in alphabet_shift:
                assign = alphabet_shift.index(letter)
            if letter == alphabet_shift[assign]:
                new_text[i] = alphabet[assign]
                i += 1
            else:
                new_text[i] = letter
                i += 1
        elif direction != "encode" or direction != "decode":
            print(f"Invalid command: {direction}")
            break

    if direction == "encode" or direction == "decode":
        print(f"The {direction}d message is:")
        print(''.join(new_text))


alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
running = True

print(logo)
while running == True:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt, or 'end' to exit:\n"
    ).lower()
    if direction == "end":
        print("Exiting program...")
        break
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(direction=direction, text=text, shift=shift)
