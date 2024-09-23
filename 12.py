def decrypt_message(characters, indices):   #fungsi ini digunakan untuk membaca pesan yang terenskripsi dengan cara membaca posisi pesan tersebut menggunakan indices
    message = ""                            #message ini nanti bakal diisi huruf-huruf yang diambil berdasarkan nomor yang ada.

    for index in indices:                   #dalam pengulangan for ini kita ngeliat semua angka dari si indices ini angka
        if index == -1:
            message += " "
        else:                   
            message += characters[index]    #Setiap message yang tertulis akan ditambah + dengan banyaknya character, lalu nanti index yang berasal dari indices akan dikurangkan satu
    return message

characters = input()          
n = int(input())
indices = list(map(int, input().split()))

decrypted_message = decrypt_message(characters, indices)
print(decrypted_message)
