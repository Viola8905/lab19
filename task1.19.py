count=0
with open("numbers.txt","w") as file:
    array=list(map(int,file.readline().split()))

    for i in array:
        if i%2==0:
            count+=1

print(count)

# print(len([x for x in list(map(int,file.readline().split())) if x%2==0]))