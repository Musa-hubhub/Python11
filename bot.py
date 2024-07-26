from aiogram import Dispatcher,Bot,executor,types
from keyboards import main_menu,texno_menu,iPhone_menu,Samsung_menu,Xiaomi_menu
api = '7281297788:AAG9ISNHsBJzgadz0U4A5CEfY6a_SrW8q7I'
bot = Bot(api)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def send_hi(sms:types.Message):
    logo = open(file='images\логотип.jpg',mode='rb')
    await sms.answer_photo(
        photo=logo,
        caption=f'''Assalamu aleykum {sms.from_user.first_name}.
Botimizga xosh keldiniz.
Menudi koriw ushin menu tuymesin basin
''',reply_markup=main_menu)
@dp.message_handler(text='Menu')#/
async def send_menu(sms:types.Message):
    await sms.answer(text='Bizdin texnoning menusi:',
                     reply_markup=texno_menu)
    
@dp.message_handler(text='🍏iPhone🍏')
async def send_lavashs(sms:types.Message):
    await sms.answer(
        text='У нас есть только такие Айфоны👇',
        reply_markup=iPhone_menu
        )
@dp.message_handler(text='📱Samsung📱')
async def send_lavashs(sms:types.Message):
    await sms.answer(
        text='У нас есть только такие Samsung👇',
        reply_markup=Samsung_menu
        )

@dp.message_handler(text='📱Xiaomi📱')
async def send_lavashs(sms:types.Message):
    await sms.answer(
        text='У нас есть только такие Xiaomi👇',
        reply_markup=Xiaomi_menu
        )








    # if data=='Pro max':
    #     standart = open(file='lesson_4/Photo/iPhone_15_Pro_Max_Natural_Titanium_PDP_Image_Position-1__GBEN_3f986b98-4f67-4d42-b16d-ea70ba35c6ef.webp',mode='rb')
    #     await bot.send_photo(
    #         chat_id=call.from_user.id,
    #         photo=standart,
    #         caption=''
        # )






@dp.callback_query_handler()
async def send_tamaqs(call:types.CallbackQuery):
    data = call.data
    if data=='standart':
        standart = open(file='images\proax.jpg',mode='rb')
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=standart,
            # photo=15 pro max,
            caption='')
    elif data=='acd':
        acd = open(file='images\propro.jpg',mode='rb')
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=acd,
            caption='')
    elif data=='b':
        b = open(file='images\standart.jpg',mode='rb')
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=b,
            caption='')
    elif data=='c':
        c = open(file='images\cpromax.jpg',mode='rb')
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=c,
            caption='')
    elif data=='d':
        d = open(file='images\cpro.jpg',mode='rb')
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=d,
            caption='')
    elif data=='e':
        e = open(file='images\cstandart.jpg',mode='rb')
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=e,
            caption='')
    elif data=='ab':
        ab = open(file='images\abpromax.jpg',mode='rb')
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=ab,
            caption='')
    elif data=='cd':
        cd = open(file='images\npro.jpg',mode='rb')
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=cd,
            caption='')
    elif data=='dd':
        dd = open(file='images\abstandart.jpg',mode='rb')
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=dd,
            caption='')
    # elif data=='b':
    #     b = open(file='images\standart.jpg',mode='rb')
    #     await bot.send_photo(
    #         chat_id=call.from_user.id,
    #         photo=b,
    #         caption='')
    # elif data=='b':
    #     b = open(file='images\standart.jpg',mode='rb')
    #     await bot.send_photo(
    #         chat_id=call.from_user.id,
    #         photo=b,
    #         caption='')
if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)

