def decrypt_message(characters, indices):
    message = ""
    for index in indices:
        message += characters[index - 1]
    return message

characters = input("Enter the string of characters: ")
n = int(input("Enter the number of times to decrypt: "))
indices = list(map(int, input("Enter the indices separated by spaces: ").split()))

decrypted_message = decrypt_message(characters, indices)

print("Decrypted message:", decrypted_message)
