

with open("num.txt", "r") as file:
    array = list(map(int, file.readline().split()))

array.pop(0)
print(sum(array)/len(array))

with open("num.txt","w") as file:
    a=[sum(array)/len(array)]+array
    file.write(str(a))
