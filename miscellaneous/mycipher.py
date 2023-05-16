# Caesar cipher.
text = input("Enter your message: ")
shift = input("Enter a shift value from 1..25: ")
try:
    shiftValue: int = int(shift)
    if 1 <= shiftValue <= 25:
        cipher = ''
        for char in text:
            if char.isnumeric() or not char.isalpha():
                cipher += char
                continue
            if char.isalpha() and char.isupper():
                shiftOrd = ord(char) + shiftValue
                if chr(shiftOrd).islower():
                    shiftOrd += 32
                cipher += chr(shiftOrd)
                continue
            if char.isalpha() and char.islower():
                shiftOrd = ord(char) + shiftValue
                if chr(shiftOrd).isupper():
                    shiftOrd -= 32
                cipher += chr(shiftOrd)
                continue

        print(cipher)
    else:
        print("Shift has to be a valid number from 1 to 25.")
except:
    print("Shift has to be a valid number from 1 to 25.")
