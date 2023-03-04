from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
    InlineKeyboardButton, InlineKeyboardMarkup

start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_b1 = KeyboardButton("Меню")
start_b2 = KeyboardButton("Помощь")
start_kb.add(start_b1)
start_kb.insert(start_b2)

ikb = InlineKeyboardMarkup(row_width=2)

ib1 = InlineKeyboardButton(text='Да', callback_data="like")
ib2 = InlineKeyboardButton(text='Нет', callback_data="dislike")
ib3 = InlineKeyboardButton(text='Следующее фото', callback_data="dont_like")
ikb.add(ib1, ib2).add(ib3)

class ExitReplay:
    def __init__(self, *params, exit=True):
        self.kb = ReplyKeyboardMarkup(resize_keyboard=True)
        if exit:
            self.kb.add(KeyboardButton("Выход"))

        for _param in params:
            self.params_add(_param)
    def __call__(self, *args, **kwargs):
        return self.kb

    def params_add(self, _param):
        k_i = KeyboardButton(_param)
        self.kb.add(k_i)

menu_kb = ExitReplay('Помощь', 'Отправить фото', 'Секрет', exit=False)()
# b1 = KeyboardButton('help')
# b2 = KeyboardButton('/echo')
# b3 = KeyboardButton('send_photo')
# kb.add(b1, b2, b3, b4)
