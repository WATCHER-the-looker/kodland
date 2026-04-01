import telebot
import random
bot = telebot.TeleBot("мой токен")

def get_random_image():
    roll = random.uniform(0, 100)

    if roll < 50:
        return "6903ac1485f5404e332e6fb2.png"
    elif roll < 80:
        return "89518987c90ee6c435b424d07ef05c24.png"
    elif roll < 95:
        return "5b4ab6e9be0df963f46e760042278a42.png"
    elif roll < 99:
        return "360_F_295727820_PN5rz0RvRipElZxhJlidd5vjVWuLAZsQ.png"
    elif roll < 99.9:
        return "9359e5bce024e3aa9ea1c0a988535b6b.png"
    else:
        return "6e909f0c3bd2ba68b3f9b87e475fa07b.png"

captions = {
    "6903ac1485f5404e332e6fb2.png": "Обычный мем",
    "89518987c90ee6c435b424d07ef05c24.png": "Неплохой мем",
    "5b4ab6e9be0df963f46e760042278a42.png": "Редкий мем",
    "360_F_295727820_PN5rz0RvRipElZxhJlidd5vjVWuLAZsQ.png": "Очень редкий мем",
    "9359e5bce024e3aa9ea1c0a988535b6b.png": "Мифический мем!",
    "6e909f0c3bd2ba68b3f9b87e475fa07b.png": "УЛЬТРА ЛЕГЕНДАРНЫЙ МЕМ!!!"
}

@bot.message_handler(commands=['meme'])
def send_meme(message):
    img_name = get_random_image()

    caption = captions.get(img_name, "")

    with open(f'images/{img_name}', 'rb') as f:
        bot.send_photo(message.chat.id, f, caption=caption)