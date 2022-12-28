import datetime 
import pytz #Библиотека для работы timezonaми


timezone = pytz.timezone("Europe/Moscow")
# print(type(now))
# print(now.minute) можно обращаться ко всем атрибутам времени

now_with_tz = timezone.localize(datetime.datetime.now())

print(now_with_tz)

now_formatted = now_with_tz.strftime("%d.%m.%Y")
print(now_formatted)

now = datetime.datetime.strptime("28.03.2022", "%d.%m.%Y")
print(now)


# if now.hour == 12:
#     print("Сейчас ровно 12 дня")
# else:
#     print(f"Сейчас {now.hour} часов")