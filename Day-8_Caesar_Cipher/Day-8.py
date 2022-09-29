from art import logo
print(logo)
condition = True
while condition:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    def caesar(start_text, shift_amount, cipher_direction):
        if shift_amount > 26:
            shift_amount = shift_amount % 26
        end_text = ""
        for char in start_text:
            if char in alphabet: 
                position = alphabet.index(char)
                if cipher_direction == "encode":                  
                    new_position = position + shift_amount      
                elif cipher_direction == "decode":              
                    new_position = position - shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += char
        print(f"The {cipher_direction} text is {end_text}")

    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)

    a = input("If you want to go again,'yes' or 'no': ")
    if a == "yes":
        condition = True                    
    elif a == "no":                       
        condition = False
        print("Goodbye")

