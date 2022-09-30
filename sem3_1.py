a = [7, 4, 5, 1, 33, 27, 4]
sum = 0
for i in range(1, len(a), 2):
    if i % 2 == 1:
        sum += a[i]       
print(sum)