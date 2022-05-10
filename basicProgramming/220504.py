# 삽입 정렬

L_insert = [1, 2, 4, 7, 3, 5]

print('before : ', L_insert)

for i in range(len(L_insert)) :
    j = i
    while j > 0 and L_insert[j] > L_insert[j+1] :
        temp = L_insert
        L_insert[j] = L_insert[j+1]
        L_insert[j+1] = temp
        j -= 1

# 버블 정렬