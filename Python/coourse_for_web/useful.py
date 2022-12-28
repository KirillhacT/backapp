from pprint import pprint #Красивый вывод
import csv
users = [{
    "name": "Vasya",
    "phone": 123,
    "lol": "kek"
},{
    "name": "Petya",
    "phone": 228,
    "aboba": 123
}]
# pprint(users)

with open("users.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Алексей", "gyyn"])
    writer.writerow(["Егор", "Michacha"])
    writer.writerow(["Петр", "Petyn"])

