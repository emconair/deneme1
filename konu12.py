#siralama algoritmalari
numbers=[7,5,4,3,9,8,2,1,6]

size= numbers.__len__()
for i in range(0,size):
    for j in range(1,size):
        if numbers[j-1]>numbers[j]:
            z=numbers[j-1]
            numbers[j-1]=numbers[j]
            numbers[j]=z
print(numbers)