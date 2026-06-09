import telebot
from telebot import apihelper
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from flask import Flask
import threading

# تنظیم endpoint بله
apihelper.API_URL = "https://tapi.bale.ai/bot{0}/{1}"

# ─── تنظیمات ───────────────────────────────────────────────
TOKEN        = "560660765:yORGFoVOwJN8qEk2iToVDdSRSXwEzOoO4FE"
MOBILE1      = "09120646909"
MOBILE2      = "09370072236"
LANDLINE1    = "02155278487"
LANDLINE2    = "02155278488"
ADDRESS      = "تهران، بزرگراه آیت الله سعیدی، چهاردانگه، خیابان کریمی، میدان شهدا، وستا دکور"
INSTAGRAM    = "https://www.instagram.com/divar.posh?igsh=b2ZlbmkycGU3M2Rj&utm_source=qr"
WHATSAPP     = "https://wa.me/989120646909"
SUPPORT_BALE = "@divar_posh"

# ─── Flask برای زنده نگه داشتن سرویس ──────────────────────
app = Flask(__name__)

@app.route('/')
def health():
    return 'OK'

def run_flask():
    app.run(host='0.0.0.0', port=8080)

threading.Thread(target=run_flask, daemon=True).start()

# ─── ساخت بات ──────────────────────────────────────────────
bot = telebot.TeleBot(TOKEN)

# ─── محصولات ────────────────────────────────────────────────
PRODUCTS = {
    "🧱 دیوارپوش فومی": (
        "🏷 *دیوارپوش فومی سه‌بعدی*\n\n"
        "✅ سبک، عایق صدا و حرارت\n"
        "📐 ابعاد: ۵۰×۵۰ سانتی‌متر\n\n"
        f"📞 سفارش:\n09120646909\n@divar_posh"
    ),
    "🏠 دیوارپوش فومی رولی": (
        "🏷 *دیوارپوش فومی رولی*\n\n"
        "✅ نرم و انعطاف‌پذیر\n"
        "📏 مناسب فضاهای بزرگ\n\n"
        f"📞 سفارش:\n09120646909\n@divar_posh"
    ),
    "🪵 ترمووال": (
        "🏷 *پانل ترمووال*\n\n"
        "✅ عایق حرارتی و صوتی\n"
        "✅ مناسب دیوار و سقف\n\n"
        f"📞 سفارش:\n09120646909\n@divar_posh"
    ),
    "⬜ کفپوش": (
        "🏷 *کفپوش لمینت و وینیل*\n\n"
        "✅ طرح‌های متنوع چوب و سنگ\n"
        "✅ مقاوم در برابر رطوبت\n\n"
        f"📞 سفارش:\n09120646909\n@divar_posh"
    ),
    "📐 قرنیز": (
        "🏷 *قرنیز PVC و MDF*\n\n"
        "✅ رنگ‌بندی متنوع\n"
        "✅ مقاوم در برابر رطوبت\n\n"
        f"📞 سفارش:\n09120646909\n@divar_posh"
    ),
    "🪨 ماربل شیت": (
        "🏷 *ماربل شیت*\n\n"
        "✅ ظاهر لوکس، وزن سبک\n"
        "✅ مناسب آشپزخانه و سرویس\n\n"
        f"📞 سفارش:\n09120646909\n@divar_posh"
    ),
}

# ─── کیبوردها ───────────────────────────────────────────────
def main_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(KeyboardButton("🛍 محصولات"), KeyboardButton("📍 آدرس و اطلاعات"))
    kb.add(KeyboardButton("🤝 پشتیبانی"), KeyboardButton("📸 اینستاگرام"))
    return kb

def products_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for name in PRODUCTS:
        kb.add(KeyboardButton(name))
    kb.add(KeyboardButton("🔙 بازگشت به منوی اصلی"))
    return kb

# ─── هندلرها ────────────────────────────────────────────────
@bot.message_handler(commands=["start"])
def start(message):
    name = message.from_user.first_name or "کاربر عزیز"
    bot.send_message(message.chat.id,
        f"سلام {name} عزیز 👋\n\n"
        "به بات رسمی 🏠 *وستا دکور* خوش آمدید!\n\n"
        "• دیوارپوش فومی و ترمووال\n"
        "• کفپوش لمینت و وینیل\n"
        "• قرنیز، ماربل شیت\n\n"
        "از منوی پایین انتخاب کنید 👇",
        parse_mode="Markdown", reply_markup=main_kb())

@bot.message_handler(func=lambda m: m.text == "🛍 محصولات")
def products(message):
    bot.send_message(message.chat.id,
        "📦 *محصولات وستا دکور*\n\nیک محصول انتخاب کنید:",
        parse_mode="Markdown", reply_markup=products_kb())

@bot.message_handler(func=lambda m: m.text in PRODUCTS)
def product_detail(message):
    bot.send_message(message.chat.id, PRODUCTS[message.text],
        parse_mode="Markdown", reply_markup=products_kb())

@bot.message_handler(func=lambda m: m.text == "📍 آدرس و اطلاعات")
def address(message):
    bot.send_message(message.chat.id,
        f"🏪 *وستا دکور*\n\n"
        f"📍 *آدرس:*\n{ADDRESS}\n\n"
        f"☎️ *تلفن ثابت:*\n{LANDLINE1}\n{LANDLINE2}\n\n"
        f"📱 *موبایل:*\n{MOBILE1}\n{MOBILE2}\n\n"
        "🕐 *ساعت کاری:*\nشنبه تا پنج‌شنبه | ۹ صبح تا ۷ شب",
        parse_mode="Markdown", reply_markup=main_kb())

@bot.message_handler(func=lambda m: m.text == "🤝 پشتیبانی")
def support(message):
    bot.send_message(message.chat.id,
        f"👨‍💼 *پشتیبانی وستا دکور*\n\n"
        f"💬 بله: {SUPPORT_BALE}\n"
        f"📱 واتساپ: {WHATSAPP}\n"
        f"📞 تماس: {MOBILE1}\n\n"
        "⏰ شنبه تا پنج‌شنبه | ۹ صبح تا ۷ شب",
        parse_mode="Markdown", reply_markup=main_kb())

@bot.message_handler(func=lambda m: m.text == "📸 اینستاگرام")
def instagram(message):
    bot.send_message(message.chat.id,
        f"📸 *اینستاگرام وستا دکور*\n\n{INSTAGRAM}\n\n"
        "آخرین طرح‌ها رو دنبال کنید! 🎨",
        parse_mode="Markdown", reply_markup=main_kb())

@bot.message_handler(func=lambda m: m.text == "🔙 بازگشت به منوی اصلی")
def back(message):
    bot.send_message(message.chat.id, "منوی اصلی 🏠", reply_markup=main_kb())

@bot.message_handler(func=lambda m: True)
def fallback(message):
    bot.send_message(message.chat.id,
        "لطفاً از منوی پایین انتخاب کنید 👇",
        reply_markup=main_kb())

# ─── اجرا ───────────────────────────────────────────────────
if __name__ == "__main__":
    print("✅ بات وستا دکور (بله) شروع به کار کرد...")
    bot.infinity_polling()
