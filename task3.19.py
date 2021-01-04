array=[]
with  open("num.txt","r",encoding="utf-8") as file:
    arrayOfStrings = file.readlines()
    for i in arrayOfStrings:
        array.append(i.split(","))

for i in range(len(array)-1):
    array[i][4] = array[i][4].rstrip("\n")#видаляє з кінця стрки певні символи



while True:
    print("\n")
    print("1. Вивести всю інформацію\n"
          "2. Знайти \n"
          "3. Вийти\n")

    choose = int(input("Виберіть номер:"))
    if choose == 1:
        for item in array:
            print(item)
    elif choose == 2:
        print("Знайти за:\n"
              "1.Паспортні дані\n"
              "2.Освіта\n"
              "3.Спеціальність\n"
              "4.Посада\n"
              "5.Оклад\n")
        choose2 = int(input("Виберіть номер:"))
        criteria = input("Введіть значення: ")
        if choose2 == 1:
            for item in array:
                if criteria in item[0]:
                    print(item)
        elif choose2 == 2:
            for item in array:
                if criteria == item[1]:
                    print(item)
        elif choose2 == 3:
            for item in array:
                if criteria in item[2]:
                    print(item)
        elif choose2 == 4:
            for item in array:
                if criteria == item[3]:
                    print(item)
        elif choose2 == 5:
            for item in array:
                if criteria == item[4]:
                    print(item)

    elif choose==3:
        break
    else: print("Немає такого номеру,повторіть спробу")