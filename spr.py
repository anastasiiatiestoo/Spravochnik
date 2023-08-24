mport os, re


def phone_format(n): 
    n = n.removeprefix("+")
    n = re.sub("[ ()-]", "", n)
    return format(int(n[:-1]), ",").replace(",", "-") + n[-1]


def printData(data):  
    phoneBook = []
    splitLine = "=" * 49
    print(splitLine)
    print(" №  Фамилия        Имя          Номер телефона")
    print(splitLine)
    personID = 1

    for contact in data:
        lastName, name, phone = contact.rstrip().split(",")
        phoneBook.append(
            {
                "ID": personID,
                "Фамилия": lastName,
                "Имя": name,
                "Номер телефона": phone_format(phone),
            }
        )
        personID += 1

    for contact in phoneBook:
        personID, lastName, name, phone = contact.values()
        print(f"{personID:>2}. {lastName:<15} {name:<10} -- {phone:<15}")

    print(splitLine)


def showContacts(fileName):  
    os.system("cls")
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)
    input("\n--- Введите ключ ---")


def addContact(fileName):  
    os.system("cls")
    with open(fileName, "a", encoding="UTF-8") as file:
        res = ""
        res += input("Введите фамилию: ") + ","
        res += input("Введите имя: ") + ","
        res += input("Введите номер телефона: ")

        file.write(res + "\n")

    input("\nКонтакт был успешно добавлен!\n--- Введите ключ ---")


def findContact(fileName):  
    os.system("cls")
    target = input("Введите ключ для поиска: ")
    result = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = file.readlines()
        for person in data:
            if target in person:
                result.append(person)
           

    if len(result) != 0:
        printData(result)
    else:
        print(f"Нет контакта '{target}'.")

    input("--- Введите ключ ---")


def changeContact(fileName):  
    os.system("cls")
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Введите номер контакта для того чтобы ввести изменения или нажмите 0 для выхода: ")
        )
        print(data[numberContact - 1].rstrip().split(","))
        if numberContact != 0:
            newLastName = input("Введите новое имя: ")
            newName = input("Введите новую фамилию: ")
            newPhone = input("Введите новый номер телефона: ")
            data[numberContact - 1] = (
                newLastName + "," + newName + "," + newPhone + "\n"
            )
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))
                print("\nКонтакт был успешно изменен!")
                input("\n--- Введите ключ ---")
        else:
            return


def deleteContact(fileName):  
    os.system("cls")
    with open(fileName, "r+", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Введите ключ контакта для удаления или 0 для возврата в меню: ")
        )
        if numberContact != 0:
            print(f"Удаление: {data[numberContact-1].rstrip().split(',')}\n")
            data.pop(numberContact - 1)
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))

        else:
            return

    input("--- Введите ключ ---")


def drawInterface(): 
    print("#####   PHONE BOOK   #####")
    print("=" * 26)
    print(" [1] -- Показать контакт")
    print(" [2] -- Добавить контакт")
    print(" [3] -- Найти контакт")
    print(" [4] -- Изменить контакт")
    print(" [5] -- Удалить контакт")
    print("\n [0] -- Выход")
    print("=" * 26)


def main(file_name):  
    while True:
        os.system("cls")
        drawInterface()
        userChoice = int(input("Введите цифру от 1 до 5 или 0 для выхода: "))

        if userChoice == 1:
            showContacts(file_name)
        elif userChoice == 2:
            addContact(file_name)
        elif userChoice == 3:
            findContact(file_name)
        elif userChoice == 4:
            changeContact(file_name)
        elif userChoice == 5:
            deleteContact(file_name)
        elif userChoice == 0:
            print("Спасибо!")
            return


path = "phonebook.txt"

main(path)
