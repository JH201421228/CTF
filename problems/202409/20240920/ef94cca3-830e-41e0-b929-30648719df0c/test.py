pumpkin = [ 124, 112, 59, 73, 167, 100, 105, 75, 59, 23, 16, 181, 165, 104, 43, 49, 118, 71, 112, 169, 43, 53 ]
counter = 0
pie = 1

for _ in range(100):
    for idx in range(len(pumpkin)):
        pumpkin[idx] ^= pie
        pie = ((pie ^ 0xff) + (idx * 10)) & 0xff

print(pumpkin)