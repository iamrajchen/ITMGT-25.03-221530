def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
    else:
        letter_num = ord(letter) - ord("A")
        shift = ord(letter_shift) - ord("A")
        shifted_num = (letter_num + shift) % 26
        shifted_ascii = shifted_num + ord("A")
        FV = chr(shifted_ascii)
    return FV


