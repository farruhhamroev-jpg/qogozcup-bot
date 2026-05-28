import telebot

TOKEN = "8972711528:AAFaRdOJpklD6Y-56c6iZhz08uT9JBc3jNI"

bot = telebot.TeleBot(TOKEN)

total_quantity = 0
total_amount = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "📊 QogozCup Hisobchi Bot\n\n"
        "Format:\n"
        "20.05 50000 9850000"
    )

@bot.message_handler(func=lambda message: True)
def calculate(message):
    global total_quantity, total_amount

    try:
        data = message.text.split()

        date = data[0]
        quantity = int(data[1])
        amount = int(data[2])

        total_quantity += quantity
        total_amount += amount

        result = (
            f"✅ Qo'shildi\n\n"
            f"📅 Sana: {date}\n"
            f"📦 Sotilgan: {quantity:,} ta\n"
            f"💰 Savdo: {amount:,} so'm\n\n"
            f"📊 UMUMIY:\n"
            f"📦 {total_quantity:,} ta\n"
            f"💰 {total_amount:,} so'm"
        )

        bot.reply_to(message, result)

    except:
        bot.reply_to(
            message,
            "❌ Format noto'g'ri\n\n"
            "To'g'ri format:\n"
            "20.05 50000 9850000"
        )

bot.infinity_polling()
# up# update
