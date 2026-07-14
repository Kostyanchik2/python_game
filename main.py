# доделать блокнот надо
import winsound 
import time
Directory = "C:/"
cmd = "Null"
File_one_C = "Pagefile.sys"
Folder_one_C = "users"
Folder_two_C = "system32"
File_two_C = ""
Folder_three_C = ""
papka = 0
notepad = ""
def save():
    if notepadsave == "y":
    if papka == 0:
        File_two_C = "File.txt"
        save_in_notepad = notepad
    elif papka == 1:
        File_one_users = "File.txt"
        save_in_notepad = notepad
def Ru():
    global File_one_users
    global Folder_one_users
    Folder_one_users = name
    global notepad 
    global File_one_C
    global Folder_one_C
    global Folder_two_C
    global File_two_C
    global Folder_three_C
    global papka
    global save_in_notepad
    save_in_notepad = ""
    File_one_users = ""
    while True:
        cmd = input(f"{Directory} > ")
        if cmd == "Null":
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
            print("notepad - Блокнот")
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
            elif Directory == "..":
                if papka == 1:
                    Directory = "C:/"
                elif papka == 0:
                    print("Ошибка 404 No found")
                    winsound.Beep(1000, 1000)
                    Directory = "C:/"
        elif cmd == "notepad":
            print("Блокнот - Безымянный")
            notepad = input("Впишите свой текст (Для открытия наберите open)")
            global notepadsave
            notepadsave = input("Сохранить? Y/N ").lower()
            if notepad == "open":
                if papka == 0:
                    if File_two_C == "File.txt":
                        notepad = input(f"Ваш текст: {save_in_notepad}, введите новый текст")
                        notepadsave = input("Сохранить? Y/N ").lower()
                        save()
                    else:
                        print("Ошибка 404")
                        ru()
            else:
                save()
                    
                
            


                    
                    
            else: 
                print("Ошибка 404")
                winsound.Beep(1000, 1000)
            
def En():
    while True:
        cmd = input(f"{Directory} > ")
        if cmd == "":
            print("Unknown error")
            winsound.Beep(1000, 1000)
            time.sleep(5)
            exit 
        if cmd == "dir":
            if papka == 0:
                print(f"{Folder_one_C}    Folder.   700 Mb ")
                print(f"{Folder_two_C}.   Folder.   35 Gb")
                print(f"{File_one_C}    File.   15 Gb ")
                print(f"{Folder_three_C}.")
                print(f"{File_two_C}")
            elif papka == 1:
                print(f"{name}")

        elif cmd == "help":
            print("dir - View directory ")
            print("echo - Display text")
            print("cd - Select a directory")
        elif cmd == echo:
            global tekst
            tekst = input("Enter text: ")
            print(f"{tekst}")
        elif cmd == cd:
            Directory = input("Select a directory").lower()
            if Directory == "users":
                auth = input("Your account password ")
                if auth == password:
                    Directory = "C:/users"
                    papka = 1
                else:
                    paint("A hacking attempt was detected.!")
            elif Directory == "..":
                if papka == 1:
                    Directory = "C:/"
                elif papka == 0:
                    print("Error 404 No found")
                    winsound.Beep(1000, 1000)
                    Directory = "C:/"
            else: 
                print("Error 404")
                winsound.Beep(1000, 1000)
                
name = input("Ваше имя(Your name) ")
password = input("Пароль(Password) ")
auth = ""
Lang = input("Выбирите язык (Select language): Ru/En ").lower()
if Lang == "ru":
    Ru()
elif Lang == "en":
    En()
        
        

        
            
