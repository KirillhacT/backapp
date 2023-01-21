import calendar
import datetime
import time
import locale

# date — для годов, месяцев и дней;
# time — для часов, минут, секунд и долей секунды;
# datetime — для даты и времени одновременно;
# timedelta — для интервалов даты и/или времени.

#Високосные года (каждый 4 год + не каждый 100 + каждый 400)
def is_leap():
    print(calendar.isleap(1900))
    print(calendar.isleap(1996))
    print(calendar.isleap(1999))
    print(calendar.isleap(2000))
    print(calendar.isleap(2002))
    print(calendar.isleap(2004))
# is_leap()

def dated():
    hallowen = datetime.date(2023, 10, 31)
    print(hallowen.isoformat())
    print(hallowen.day)
    print(hallowen.month)
    print(hallowen.year)

# dated()

def timedelt():
    #today() - сегоднешнее число
    now = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    print(tomorrow := now + one_day)
    # print(now + 31*one_day)
    print(yesterday := now - one_day)
# timedelt()

# Спецификатор Единица даты/времени Диапазон
# %Y Год 1900–…
# %m Месяц 01–12
# %B Название месяца Январь…
# %b Сокращение для месяца Янв…
# %d День месяца 01–31
# %А Название дня Воскресенье…
# А Сокращение для дня Вск…
# %Н Часы (24 часа) 00–23
# %I Часы (12 часов) 01–12
# %p AM или PM AM, PM
# %M Минуты 00–59
# %S Секунды 00–59


def time_example():
    # now = time.time()
    #полная информация о времени
    # e = time.localtime(now)
    # print(e)

    # now_ct = time.ctime(now)
    # print(now_ct)

    #strftime с модулем time
    fmt = f"It's %A, %B %d, %Y, local time %I:%M:%S%p"
    t = time.localtime()
    new_time = time.strftime(fmt, t)
    print(new_time)

    # strftime с модулем datetime
    hallowen = datetime.date(2023, 10, 31)
    hal = hallowen.strftime("%A, %B %d")
    print(hal)
time_example()


