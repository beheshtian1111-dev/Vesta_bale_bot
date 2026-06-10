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

LAMSE_IDS = ['181528713:7480628814542282496:0:ef01f5dbfaaa426d48d1e46b939b3a07', '181528713:-5871035327957557501:0:36696e581da9e85948d1e46b939b3a07', '181528713:7222313456172801792:0:ac55bf145561b39c48d1e46b939b3a07', '181528713:7662432913168801537:0:30cb28011b67094648d1e46b939b3a07', '181528713:-5656023503620137215:0:3f7406cc840f589348d1e46b939b3a07', '181528713:5781471483104206592:0:5bcb7c15220daddf48d1e46b939b3a07', '181528713:3644348171039743746:0:6f05e5447c3886e048d1e46b939b3a07', '181528713:-3684190441892667646:0:cc75305eff88278248d1e46b939b3a07', '181528713:2046769108871421698:0:8a8f50671aa9673348d1e46b939b3a07', '181528713:-7785589188324090112:0:bd2003e71dab0f5f48d1e46b939b3a07']
ABZAR_IDS = ['181528713:-7716135794017231104:0:43f4cc815cd50e4348d1e46b939b3a07', '181528713:-5295275485089685757:0:f6cd754862bdc9d548d1e46b939b3a07', '181528713:1272116883933110017:0:59e8ad5f0c88efc748d1e46b939b3a07', '181528713:692150713988292355:0:4342c1fb610f336c48d1e46b939b3a07', '181528713:-2178671994401579261:0:0127b63cbf05287d48d1e46b939b3a07', '181528713:-7522085076316971262:0:f0e8356a015503cf48d1e46b939b3a07', '181528713:-9005568367304827135:0:8fd4a8e29a7df632407d36e64a219bb497331796b1e0167d']

CAPTION_LAMSE = """💎 *لمسه پشت چسبدار*

📐 ابعاد: ۴۷ × ۴۷ سانتی‌متر
💰 قیمت پنلی: ۲۷۰ تومان

🛒 خرید مستقیم از سایت:
https://vestadeccor.com/product-category/wallcovering/adhesive-backed-tactile-wallcovering/

📞 ثبت سفارش:
@divar_posh"""
CAPTION_ABZAR = """🖼 *ابزار قاب بندی*

📞 برای قیمت و ثبت سفارش:
@divar_posh"""

@bot.message_handler(func=lambda m: m.text == "💎 لمسه پشت چسبدار")
def lamse(message):
    send_photos(message.chat.id, LAMSE_IDS, CAPTION_LAMSE, back_kb())

@bot.message_handler(func=lambda m: m.text == "🖼 ابزار قاب بندی")
def abzar(message):
    send_photos(message.chat.id, ABZAR_IDS, CAPTION_ABZAR, back_kb())

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
PVC_IDS = ['181528713:-6359706393042673919:1:d71a0507c98b48f3d7f84da89f35935837fa52e0cd7fa437bbef6dd7a1e4ee1c', '181528713:-8454597426428502269:1:d71a0507c98b48f3d7f84da89f3593584d332d6738a91709bbef6dd7a1e4ee1c', '181528713:-5610972478951973117:1:d71a0507c98b48f3d7f84da89f35935805a47f81651a84aabbef6dd7a1e4ee1c', '181528713:-4812677088037560574:1:d71a0507c98b48f3d7f84da89f3593583a6358cf9cdaafdfbbef6dd7a1e4ee1c', '181528713:-5852724689307164927:1:d71a0507c98b48f3d7f84da89f35935898fd4a62c703a9b4bbef6dd7a1e4ee1c', '181528713:8199534583358103299:1:d71a0507c98b48f3d7f84da89f3593582c3108f98d40275ebbef6dd7a1e4ee1c', '181528713:-3307287448484831486:1:d71a0507c98b48f3d7f84da89f359358693d5570e884ab8dbbef6dd7a1e4ee1c', '181528713:-1332988741735276798:1:d71a0507c98b48f3d7f84da89f35935804a79c741255b31dbbef6dd7a1e4ee1c', '181528713:4148632960874258178:1:d71a0507c98b48f3d7f84da89f359358bef39d925992ad14bbef6dd7a1e4ee1c', '181528713:-5698113112130576640:1:d71a0507c98b48f3d7f84da89f3593589dcd6465eb1f1334bbef6dd7a1e4ee1c', '181528713:-5753164990513864958:1:d71a0507c98b48f3d7f84da89f359358403219ba96e5c978bbef6dd7a1e4ee1c', '181528713:-6777740392750506239:1:d71a0507c98b48f3d7f84da89f359358ef1c7c067658e003bbef6dd7a1e4ee1c']
MDF_IDS = ['181528713:-5886479367132930302:1:d71a0507c98b48f32218db8ed3f2dc50d854b305ed626c19bbef6dd7a1e4ee1c', '181528713:-1870567644143018239:1:d71a0507c98b48f32218db8ed3f2dc50ee79bc5201e1e8b2bbef6dd7a1e4ee1c', '181528713:-5394457751463125245:1:d71a0507c98b48f32218db8ed3f2dc50ba9f1917e734c806bbef6dd7a1e4ee1c', '181528713:-4536717732469793023:1:d71a0507c98b48f32218db8ed3f2dc50556b989aecc787eabbef6dd7a1e4ee1c', '181528713:-2167114725740962045:1:d71a0507c98b48f32218db8ed3f2dc504526f44f8eeaa5ccbbef6dd7a1e4ee1c', '181528713:-1419028510941634816:1:d71a0507c98b48f32218db8ed3f2dc502ffd09e2d3a901b6bbef6dd7a1e4ee1c', '181528713:8158389194538950400:1:d71a0507c98b48f32218db8ed3f2dc503c8cc6b9ea9592a3bbef6dd7a1e4ee1c', '181528713:9148099177618415362:1:d71a0507c98b48f32218db8ed3f2dc509701afa068a12b8cbbef6dd7a1e4ee1c']

CAPTION_PVC = """🪵 *ترمووال PVC 20cm*

📐 ابعاد: ۲۰ × ۲۸۰ سانتی‌متر
💰 قیمت: ۶۵۰ تومان

🛒 خرید مستقیم از سایت:
https://vestadeccor.com/product-category/thermowall/pvc-thermowall/

📞 ثبت سفارش:
@divar_posh"""
CAPTION_MDF = """🪵 *ترمووال MDF 50cm*

📐 ابعاد: ۵۰ × ۲۸۰ سانتی‌متر
💰 قیمت: ۱.۶۵۰ تومان

🛒 خرید مستقیم از سایت:
https://vestadeccor.com/product-category/thermowall/iranian-coated-thermopanel/

📞 ثبت سفارش:
@divar_posh"""

def send_photos(chat_id, file_ids, caption, kb):
    for i, fid in enumerate(file_ids):
        if i == len(file_ids) - 1:
            bot.send_photo(chat_id, fid, caption=caption, parse_mode="Markdown")
        else:
            bot.send_photo(chat_id, fid)
    bot.send_message(chat_id, "👆 عکس‌های محصول", reply_markup=kb)

@bot.message_handler(func=lambda m: m.text == "🔵 PVC 20cm")
def pvc_product(message):
    send_photos(message.chat.id, PVC_IDS, CAPTION_PVC, thermowall_kb())

@bot.message_handler(func=lambda m: m.text == "🪵 MDF 50cm")
def mdf_product(message):
    send_photos(message.chat.id, MDF_IDS, CAPTION_MDF, thermowall_kb())

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
