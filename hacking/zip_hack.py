from zipfile import ZipFile
from os import mkdir

line = "--------------------------------"
def generator(string):
    for word in string:
        passwd = word.replace("\n", '')
        archive.setpassword(passwd.encode())
        try:
            archive.extractall(directory)
        except:
            yield f"[False]: {passwd}"
        else:
            yield line + f"\n[True]: {passwd}"
            return


directory = "ExtractArchive"
try:
    mkdir(directory)
except FileExistsError: pass

print(line)
with open(input("Dictionary: "), errors="ignore") as dictionary:
    with ZipFile(input("Archive: ")) as archive:
        print(line)
        for password in generator(dictionary):
            print(password)
print(line)