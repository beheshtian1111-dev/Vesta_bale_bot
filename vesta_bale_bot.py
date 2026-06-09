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
WEBSITE      = "https://vestadeccor.com/"
ADMIN_ID     = 181528713

# ─── Flask ─────────────────────────────────────────────────
app = Flask(__name__)

@app.route('/')
def health():
    return 'OK'

threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8080), daemon=True).start()

# ─── ساخت بات ──────────────────────────────────────────────
bot = telebot.TeleBot(TOKEN)

# ─── متن محصولات ───────────────────────────────────────────
def product_text(name):
    return (
        f"🏷 *{name}*\n\n"
        f"📞 برای قیمت و سفارش:\n{MOBILE1}\n{SUPPORT_BALE}"
    )

# ─── کیبوردها ───────────────────────────────────────────────
def main_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(KeyboardButton("🛍 محصولات"), KeyboardButton("📍 آدرس و اطلاعات"))
    kb.add(KeyboardButton("🤝 پشتیبانی"), KeyboardButton("📸 اینستاگرام"))
    kb.add(KeyboardButton("🌐 سایت"))
    return kb

def products_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    kb.add(
        KeyboardButton("🧱 دیوارپوش فومی پشت چسبدار"),
        KeyboardButton("🌀 دیوارپوش فومی رولی"),
        KeyboardButton("🪨 ماربل شیت"),
        KeyboardButton("🪵 ترمووال"),
        KeyboardButton("⬜ کفپوش"),
        KeyboardButton("🖼 ابزار قاب بندی"),
        KeyboardButton("💎 لمسه پشت چسبدار"),
        KeyboardButton("🔙 بازگشت به منوی اصلی"),
    )
    return kb

def foam_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(
        KeyboardButton("🟫 آجر بهمنی"),
        KeyboardButton("🟧 آجر کلاسیک"),
        KeyboardButton("⬛ آجر تخت"),
        KeyboardButton("🔶 چهار پر"),
        KeyboardButton("🩶 طرح بتن"),
        KeyboardButton("🏛 آجر آنتیک"),
        KeyboardButton("🪨 سنگ آنتیک"),
        KeyboardButton("🌿 ترمو فوم"),
        KeyboardButton("🎋 بامبو"),
        KeyboardButton("💠 لوزی"),
        KeyboardButton("◼️ مربع"),
        KeyboardButton("💎 کریستال"),
        KeyboardButton("✨ هشت پر"),
    )
    kb.add(KeyboardButton("🔙 بازگشت به محصولات"))
    return kb

def thermowall_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(
        KeyboardButton("🪵 MDF 50cm"),
        KeyboardButton("🔵 PVC 20cm"),
    )
    kb.add(KeyboardButton("🔙 بازگشت به محصولات"))
    return kb

def floor_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(
        KeyboardButton("🌲 طرح پارکت"),
        KeyboardButton("🪨 طرح سنگ"),
    )
    kb.add(KeyboardButton("🔙 بازگشت به محصولات"))
    return kb

def back_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(KeyboardButton("🔙 بازگشت به محصولات"))
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
        "• قرنیز، ماربل شیت و بیشتر...\n\n"
        "از منوی پایین انتخاب کنید 👇",
        parse_mode="Markdown", reply_markup=main_kb())

# ── منوی اصلی ──
@bot.message_handler(func=lambda m: m.text == "🛍 محصولات")
def products(message):
    bot.send_message(message.chat.id,
        "📦 *دسته‌بندی محصولات وستا دکور*\n\nیک دسته انتخاب کنید:",
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

@bot.message_handler(func=lambda m: m.text == "🌐 سایت")
def website(message):
    bot.send_message(message.chat.id,
        f"🌐 *سایت وستا دکور*\n\n{WEBSITE}\n\n"
        "برای مشاهده کامل محصولات ما رو دنبال کنید!",
        parse_mode="Markdown", reply_markup=main_kb())

# ── دسته‌بندی محصولات ──
@bot.message_handler(func=lambda m: m.text == "🧱 دیوارپوش فومی پشت چسبدار")
def foam_menu(message):
    bot.send_message(message.chat.id,
        "🧱 *دیوارپوش فومی پشت چسبدار*\n\nیک طرح انتخاب کنید:",
        parse_mode="Markdown", reply_markup=foam_kb())

@bot.message_handler(func=lambda m: m.text == "🌀 دیوارپوش فومی رولی")
def foam_roli(message):
    bot.send_message(message.chat.id,
        product_text("دیوارپوش فومی رولی"),
        parse_mode="Markdown", reply_markup=back_kb())

@bot.message_handler(func=lambda m: m.text == "🪨 ماربل شیت")
def marble(message):
    bot.send_message(message.chat.id,
        product_text("ماربل شیت"),
        parse_mode="Markdown", reply_markup=back_kb())

@bot.message_handler(func=lambda m: m.text == "🪵 ترمووال")
def thermowall_menu(message):
    bot.send_message(message.chat.id,
        "🪵 *ترمووال*\n\nنوع را انتخاب کنید:",
        parse_mode="Markdown", reply_markup=thermowall_kb())

@bot.message_handler(func=lambda m: m.text == "⬜ کفپوش")
def floor_menu(message):
    bot.send_message(message.chat.id,
        "⬜ *کفپوش*\n\nطرح را انتخاب کنید:",
        parse_mode="Markdown", reply_markup=floor_kb())

@bot.message_handler(func=lambda m: m.text == "🖼 ابزار قاب بندی")
def abzar(message):
    bot.send_message(message.chat.id,
        product_text("ابزار قاب بندی"),
        parse_mode="Markdown", reply_markup=back_kb())

@bot.message_handler(func=lambda m: m.text == "💎 لمسه پشت چسبدار")
def lamse(message):
    bot.send_message(message.chat.id,
        product_text("لمسه پشت چسبدار"),
        parse_mode="Markdown", reply_markup=back_kb())

# ── زیرمنوی فومی ──
FOAM_PRODUCTS = {
    "🟫 آجر بهمنی", "🟧 آجر کلاسیک", "⬛ آجر تخت",
    "🔶 چهار پر", "🩶 طرح بتن", "🏛 آجر آنتیک",
    "🪨 سنگ آنتیک", "🌿 ترمو فوم", "🎋 بامبو",
    "💠 لوزی", "◼️ مربع", "💎 کریستال", "✨ هشت پر",
}

@bot.message_handler(func=lambda m: m.text in FOAM_PRODUCTS)
def foam_product(message):
    name = m.text if (m := message) else message.text
    bot.send_message(message.chat.id,
        product_text(message.text),
        parse_mode="Markdown", reply_markup=foam_kb())

# ── زیرمنوی ترمووال ──
@bot.message_handler(func=lambda m: m.text in {"🪵 MDF 50cm", "🔵 PVC 20cm"})
def thermowall_product(message):
    bot.send_message(message.chat.id,
        product_text(message.text),
        parse_mode="Markdown", reply_markup=thermowall_kb())

# ── زیرمنوی کفپوش ──
@bot.message_handler(func=lambda m: m.text in {"🌲 طرح پارکت", "🪨 طرح سنگ"})
def floor_product(message):
    bot.send_message(message.chat.id,
        product_text(message.text),
        parse_mode="Markdown", reply_markup=floor_kb())

# ── بازگشت ──
@bot.message_handler(func=lambda m: m.text == "🔙 بازگشت به محصولات")
def back_products(message):
    bot.send_message(message.chat.id,
        "📦 *دسته‌بندی محصولات*\n\nیک دسته انتخاب کنید:",
        parse_mode="Markdown", reply_markup=products_kb())

@bot.message_handler(func=lambda m: m.text == "🔙 بازگشت به منوی اصلی")
def back_main(message):
    bot.send_message(message.chat.id, "🏠 منوی اصلی", reply_markup=main_kb())

# ── هندلر عکس برای ادمین ──
@bot.message_handler(content_types=['photo'])
def get_file_id(message):
    if message.from_user.id == ADMIN_ID:
        file_id = message.photo[-1].file_id
        bot.send_message(message.chat.id, f"`{file_id}`", parse_mode="Markdown")

# ── فال‌بک ──
@bot.message_handler(func=lambda m: True)
def fallback(message):
    bot.send_message(message.chat.id,
        "لطفاً از منوی پایین انتخاب کنید 👇",
        reply_markup=main_kb())

# ─── اجرا ───────────────────────────────────────────────────
if __name__ == "__main__":
    print("✅ بات وستا دکور (بله) شروع به کار کرد...")
    bot.infinity_polling()
