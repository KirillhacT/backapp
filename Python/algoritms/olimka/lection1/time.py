#Формат вывода времени - NN/NN/NN

def get_seconds(text: str):
    str = list(map(int, text.split(":")))
    hours = str[0]
    minutes = str[1]
    seconds = str[2]

    S = seconds + minutes * 60 + hours * 3600 #Алгоритм преобразования в секунды
    return S

#Для красоты
def get_null(value):
    if value < 10:
        return f"0{value}"
    return value

# Обратный алгоритм перевода из секунд во время
def get_number(S: int):
    hours = S // 3600 
    S %= 3600
    minuteS = S // 60
    S %= 60
    seconds = S

    hours = get_null(hours)
    minuteS = get_null(minuteS)
    seconds = get_null(seconds)
    return f"{hours}:{minuteS}:{seconds}"

b = get_seconds("11:30:00")
a = get_seconds("12:00:00")

formula = (b - a) % 86400
result = get_number(formula)
print(result)


