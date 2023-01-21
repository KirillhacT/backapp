def get_null(value):
    if value < 10:
        return f"0{value}"
    return value


def leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 1
    return 0

dim = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_year(text):
    str = list(map(int, text.split("/")))
    d, m, y = str[0], str[1], str[2];
    count = 0

    while count < 10:
        d += 1
        if m == 2:
            if d == dim[m] + 1 + leap(y): #+1 чтобы он учитывал последний день
                d = 1
                m += 1
        elif d == dim[m] + 1:
            d = 1
            m += 1

        if m == 13:
            m = 1
            y += 1
        count += 1
        str = f"{get_null(d)}/{get_null(m)}/{y}"
        print(str)

get_year("27/2/2000")

def perevod(D: int, year):
    tag = 1
    flag = True
    if leap(year):
        dim[2] += 1
    while flag:
        if D <= dim[tag]:
            str = f"{get_null(D)}/{get_null(tag)}/{year}"
            print(str)
            flag = False
            continue
        D -= dim[tag]
        tag += 1
# perevod(60, 2000)

def col_days(d, m):
    D = 0
    for i in range(1, m):
        D += dim[i]
    D += d
    return D

print(col_days(3, 1))



