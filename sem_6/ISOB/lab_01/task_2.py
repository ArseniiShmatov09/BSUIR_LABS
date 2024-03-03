from task_1 import encrypt, ENG_Big

ENG_Big_str = ""
for i in ENG_Big:
    ENG_Big_str += i

ENG_Big_Matrix = []
for i in range(0, 26):
       ENG_Big_Matrix.append(encrypt(ENG_Big_str, i))

def get_new_key(key, text):
    new_key = ""
    j = 0 

    for i in range(0, len(text)):
        if text[i] in ENG_Big:
                new_key+=key[j % len(key)]
                j+=1
        else:
                new_key+=text[i]
    return new_key

def encrypt(text, k):
    new_key = get_new_key(k, text)
    new_text = ""
    for i in range(0, len(text)):
        if text[i] in ENG_Big:
            new_text+= ENG_Big_Matrix[ENG_Big.index(new_key[i])][ENG_Big.index(text[i])]
        else:
            new_text+=text[i]

    return new_text

def decrypt(text, k):
    new_key = get_new_key(k, text)
    new_text = ""
    for i in range(0, len(text)): 
        if text[i] in ENG_Big:
            new_text+= ENG_Big[ENG_Big_Matrix[ENG_Big.index(new_key[i])].index(text[i])]

        else:
            new_text+=text[i]
    return new_text

def main():
    with open('C:\\D\\BSUIR\\sem_6\\ISOB\\b.txt', 'r', encoding='utf-8') as f:
        text = f.read().upper()
    k = (input("Введите ключ для шифра: ")).upper()
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