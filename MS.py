def count_pairs(shoe_list):
    shoes = {}
    
    for shoe in shoe_list:
        size = shoe[:-1] 
        side = shoe[-1]   

        if size not in shoes:
            shoes[size] = {'L': 0, 'R': 0}
        shoes[size][side] += 1
    
    pairs = 0
    for size in shoes:
        pairs += min(shoes[size]['L'], shoes[size]['R'])
    return pairs

n = int(input("Enter the number of shoes: "))
shoe_list = []
for _ in range(n):
    shoe_list.append(input())
print(count_pairs(shoe_list))
