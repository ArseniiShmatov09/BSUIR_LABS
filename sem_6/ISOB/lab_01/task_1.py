n_ru = 33
n_eng = 26

RU_Big = []
for i in range(1040, 1072):
    if i != 1046:
        RU_Big.append(chr(i))
    else:
        RU_Big.append("Ё")
        RU_Big.append("Ж")

RU_Small = []
for i in range(1072, 1104):
    if i != 1078:
        RU_Small.append(chr(i))
    else:
        RU_Small.append("ё")
        RU_Small.append("ж")

ENG_Big = []
for i in range(65, 91):
        ENG_Big.append(chr(i))

ENG_Small = []
for i in range(97, 123):
        ENG_Small.append(chr(i))

def encrypt(text, k):
    new_text = ""
    for i in text:
        if i in RU_Big:
            new_text+= RU_Big[(RU_Big.index(i)+k) % n_ru]
        elif i in RU_Small:
            new_text+= RU_Small[(RU_Small.index(i)+k) % n_ru]
        elif i in ENG_Big:
            new_text+= ENG_Big[(ENG_Big.index(i)+k) % n_eng]
        elif i in ENG_Small:
            new_text+= ENG_Small[(ENG_Small.index(i)+k) % n_eng]
        else: 
            new_text+=i
    return new_text

def decrypt(text, k):
    new_text = ""
    for i in text:
        if i in RU_Big:
            new_text+= RU_Big[(RU_Big.index(i)-k) % n_ru]
        elif i in RU_Small:
            new_text+= RU_Small[(RU_Small.index(i)-k) % n_ru]
        elif i in ENG_Big:
            new_text+= ENG_Big[(ENG_Big.index(i)-k) % n_eng]
        elif i in ENG_Small:
            new_text+= ENG_Small[(ENG_Small.index(i)-k) % n_eng]
        else: 
            new_text+=i
    return new_text

def main():
    with open('C:\\D\\BSUIR\\sem_6\\ISOB\\a.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    k = int(input("Введите ключ для шифра: "))
    while True:
        
        operation = input("Выберете операцию(1 - Зашифровать, 2 - Расшифровать, 3 - Вывести текст файла, 0 - Завершить работу программы): ")

        if operation == "1":
            print(encrypt(text, k))
        elif operation == "2":
            print(decrypt(text, k))
        elif operation == "3":
            print(text)
        elif operation == "0":
            break
        else:
            print("Введите корректный номер операции")

if __name__ == "__main__":
    main()