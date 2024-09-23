string = input().replace(" ", "").replace("\t", "")
def encode_string(S):   #Fungsi ini digunakan untuk memproses kalimat yang kita ketik tadi.
    seen = set()        #Buat Nyimpen kalimat yg baru ditemuin, klo udh ada sebelumnya ga disimpen lagi
    result = []

    for str in S:           #ini kita buat for loop
        if str != " ":      #buat mastiin kalimat yg disimpen itu berupa string bukan spasi
            if str not in seen:     #nah kalo kalimatnya ga kesimpen...
                seen.add(str)       #bakalan di add di sini lewat si seen
                result.append(str)  #ini juga fungsinya buat nambahin kalimat yg blm kesimpen, bedannya dia bakal nambahin di akhir kalimat/list
    return "".join(result)          #sesuai namanya join ngab, ini fungsinya buat gabungin string yang ada di result tadi

print(encode_string(string))
