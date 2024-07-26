from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton



main_menu = ReplyKeyboardMarkup(resize_keyboard=True)


main_menu.add(KeyboardButton('Menu'))

texno_menu = ReplyKeyboardMarkup(resize_keyboard=True)
texno_menu.add(
    KeyboardButton(text='🍏iPhone🍏'),
    KeyboardButton(text='📱Samsung📱'),
)
texno_menu.add(
    KeyboardButton(text='📱Xiaomi📱'),
    KeyboardButton(text='📱POCO📱'))

texno_menu.add(
    KeyboardButton(text='📱Infinix📱'),
    KeyboardButton(text='📱HONOR📱')
)

iPhone_menu = InlineKeyboardMarkup()

iPhone_menu.add(
    InlineKeyboardButton(text='iPhone 15 PRO MAX',callback_data='standart'),
    InlineKeyboardButton(text='iPhone 15 PRO',callback_data='acd'),
    )

iPhone_menu.add(
    InlineKeyboardButton(text='iPhone 15',callback_data='b'),
    InlineKeyboardButton(text='iPhone 14 PRO MAX',callback_data='c'))

iPhone_menu.add(
    InlineKeyboardButton(text='iPhone 14 PRO',callback_data='d'),
    InlineKeyboardButton(text='iPhone 14',callback_data='e')
)
iPhone_menu.add(
    InlineKeyboardButton(text='iPhone 13 PRO MAX',callback_data='ab'),
    InlineKeyboardButton(text='iPhone 13 PRO',callback_data='cd')
)
iPhone_menu.add(
    InlineKeyboardButton(text='iPhone 13',callback_data='dd'),
)



Samsung_menu = InlineKeyboardMarkup()

Samsung_menu.add(
    InlineKeyboardButton(text='Samsung S24 ULRA',callback_data='s24 ultra'),
    InlineKeyboardButton(text='Samsung S24',callback_data='s24'),
    )

Samsung_menu.add(
    InlineKeyboardButton(text='S23 ULTRA',callback_data='s23 ultra'),
    InlineKeyboardButton(text='Samsung S23',callback_data='s23'))

Samsung_menu.add(
    InlineKeyboardButton(text='Samsung S22 ULTRA',callback_data='s22 ulra'),
    InlineKeyboardButton(text='Samsung S22',callback_data='s22')
)
Samsung_menu.add(
    InlineKeyboardButton(text='Samsung S21 ULTRA',callback_data='s21 ultra'),
    InlineKeyboardButton(text='Samsung S21',callback_data='s21')
)


Xiaomi_menu = InlineKeyboardMarkup()

Xiaomi_menu.add(
    InlineKeyboardButton(text='Xiaomi 13',callback_data='15 pro max'),
    InlineKeyboardButton(text='Xiaomi POCO F5',callback_data='15 pro'),
    )

Xiaomi_menu.add(
    InlineKeyboardButton(text='Xiaomi 13T',callback_data='15'),
    InlineKeyboardButton(text='Xiaomi 11T PRO',callback_data='14 pro max'))

Xiaomi_menu.add(
    InlineKeyboardButton(text='Xiaomi 11 Lite 5G',callback_data='14 pro'),
    InlineKeyboardButton(text='Xiaomi 11 Lite 5G',callback_data='14')
)
Xiaomi_menu.add(
    InlineKeyboardButton(text='Xiaomi POCO M5',callback_data='13 pro max'),
    InlineKeyboardButton(text='Xiaomi POCO X5 5G',callback_data='13 pro')
)























