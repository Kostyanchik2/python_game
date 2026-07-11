import winsound 
import time
Directory = "C:/"
cmd = "Null"
File_one_C = "Pagefile.sys"
Folder_one_C = "users"
Folder_two_C = "system32"
File_two_C = "None"
Folder_three_C = "None"
papka = 0
def Ru():
    while True:
        cmd = input(f"{Directory} > ")
        if cmd == "":
            print("Неизвестная ошибка")
            winsound.Beep(1000, 1000)
            time.sleep(5)
            exit 
        if cmd == "dir":
            if papka == 0:
                print(f"{Folder_one_C}    Папка.   700 Мб ")
                print(f"{Folder_two_C}.   Папка.   35 Гб")
                print(f"{File_one_C}    Файл.   15 ГБ ")
                print(f"{Folder_three_C}.")
                print(f"{File_two_C}")
            elif papka == 1:
                print(f"{name}")

        elif cmd == "help":
            print("dir - Посмотреть директорию")
            print("echo - показать текст")
            print("cd - открыть директорию")
        elif cmd == echo:
            global tekst
            tekst = input("Введите текст: ")
            print(f"{tekst}")
        elif cmd == cd:
            Directory = input("Выбирите директорию").lower()
            if Directory == "users":
                auth = input("Ваш пароль от акккаунта ")
                if auth == password:
                    Directory = "C:/users"
                    papka = 1
                else:
                    paint("Обнаружена попытка взлома!")
                    Ru()
            elif Directory == "..":
                if papka == 1:
                    Directory = "C:/"
                elif papka == 0:
                    print("Ошибка 404 No found")
                    winsound.Beep(1000, 1000)
                    Directory = "C:/"
            else: 
                print("Ошибка 404")
                winsound.Beep(1000, 1000)
                
name = input("Ваше имя ")
password = input("Пароль ")
auth = ""
Ru()
        
        

        
            
