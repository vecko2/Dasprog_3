def count_pairs(shoe_list):     #fungsi ini dipake buat menghitung jumlah pasangan elemen dalam struktur data
    shoes ={}                  #buat nyimpen informasi berapa banyak sepatu yang nanti dimasukin
    
    for shoe in shoe_list:       #ini bakal ada perulangan tiap sepatu 
        if shoe[-1] in ["L", "R"]:
            size = "".join([char for char in shoe if char.isdigit()])
            side = shoe[-1]

            if size:
                if size not in shoes:   #kalo sepatu blm ada di keranjang program bakal bikin
                    shoes[size] = {'L': 0, 'R': 0}  #tempat baru buat isinya dua slot, buat kanan dan kiri, diawali dri 0 karena kondisinya sepatunya blm dimasukin
                shoes[size][side] += 1     #terus pas dimasukin klo yg dimasukinnya sepatu kanan maka nanti ditambah 1 sepatu kiri, begitupun sebaliknya
    
    pairs = 0
    for size in shoes:  #buat setiap ukuran, program akan ngembil jumlah sepatu kiri dan sepatu kanan
        pairs += min(shoes[size]['L'], shoes[size]['R'])  #lalu menghitung jumlah pasang dengan menggunakan fungsi min().
    return pairs        #nanti total pasangan nya di simpen di variabel pairs

n = int(input())
shoe_list = [input() for _ in range(n)]
print(count_pairs(shoe_list))
