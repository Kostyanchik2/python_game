# ТЫ ЗАЧЕМ СЮДА ЗАШЕЛ ЕМОЕ
def ru():
  global cmd
  print(f"{name} , Добро пожаловать!")
  Vhod = input("Введите ваш пароль")
  while True:
    cmd = input(f"{directory} > ").lower()
    if cmd == "help":
      print("cd (Не писать дальше!) - перейти в деректорию")
      print("dir - Посмотреть файлы в деректории") 
      print("Pokemon - ЧТО ЖЕ ЭТО ЗА ПОКЕМОН!? (Автор не присваевает себе права на франшизу Pockemon")
def VHOD():
  global Root_вход
  Root_вход = input("Для прав администратора введите пароль(для ограниченных прав напишите N")
  if Root_вход == password:
    root = "True"
    ru()
  elif Root_вход == "N"
    ru()
  elif Root_вход != password
    print("Не верный пароль, повторите попытку")
    VHOD()
    
  
    
    
  
  
  
directory = "C:/"
name = input("Хотите создать учетную запись? (Want to create an account?) Y/N").lower()
password = ""
root = "False"
if name == "Y":
  name = input("Имя учётной записи (Account name): ") 
  password = input("введите пароль")
  VHOD()
else:
  name = "User228"
  ru()
  
  
 
  
  
    
