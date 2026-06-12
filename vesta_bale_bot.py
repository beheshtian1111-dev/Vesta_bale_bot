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
        KeyboardButton("📏 قرنیز"),
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
    send_photos(message.chat.id, ROLI_IDS, CAPTION_ROLI, back_kb())

@bot.message_handler(func=lambda m: m.text == "🪨 ماربل شیت")
def marble(message):
    send_photos(message.chat.id, MARBLE_G1, CAPTION_MARBLE_G1, back_kb())
    send_photos(message.chat.id, MARBLE_G2, CAPTION_MARBLE_G2, back_kb())
    send_photos(message.chat.id, MARBLE_G3, CAPTION_MARBLE_G3, back_kb())

@bot.message_handler(func=lambda m: m.text == "📏 قرنیز")
def qarniz(message):
    send_photos(message.chat.id, QARNIZ_IDS, CAPTION_QARNIZ, back_kb())

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


BAMBOO_IDS = ['181528713:-8846584967199711485:0:f438fe58f2dc674d48d1e46b939b3a07', '181528713:-7718948603575197952:0:5f366fee5154001d48d1e46b939b3a07', '181528713:3835147929704603393:0:865ffc213585bcac48d1e46b939b3a07', '181528713:-4458717605028225279:0:021547e46484b27348d1e46b939b3a07', '181528713:2103382821087682305:0:f2d89bc2c97b880748d1e46b939b3a07', '181528713:3462309347983171329:0:64b072e1d2d9db5148d1e46b939b3a07', '181528713:913279536457195265:0:13d4cb0bcc77bbfb48d1e46b939b3a07', '181528713:-6137187829753897215:0:26c5a96ee4f45e8248d1e46b939b3a07']
CRYSTAL_IDS = ['181528713:-1456819791996051709:0:4b04f71552168d6148d1e46b939b3a07', '181528713:-1686165163510391038:0:6b4452375657de0048d1e46b939b3a07', '181528713:3904915696284868354:0:4098c1fb662dcba948d1e46b939b3a07', '181528713:-4951137671106781438:0:06c5c1aa7061d71048d1e46b939b3a07', '181528713:1428122762226573058:0:b526d95d31917afc48d1e46b939b3a07', '181528713:8703735548184633089:0:c5c24774de3cf56148d1e46b939b3a07', '181528713:4933961372677840640:0:2f73aa280bf7134c48d1e46b939b3a07', '181528713:-132638156957868286:0:9fd48b737682b45c48d1e46b939b3a07']
SQUARE_IDS = ['181528713:-4368466984624185597:0:cde90923a478931648d1e46b939b3a07', '181528713:-7359405894251307262:0:937677e2ca9cbd9848d1e46b939b3a07', '181528713:6841535286996836099:0:abcd57d7f369342c48d1e46b939b3a07', '181528713:-225077135332466944:0:a7e31917b4b9f37248d1e46b939b3a07', '181528713:-4100657503466676479:0:b42e3ecc770582d048d1e46b939b3a07', '181528713:2002342139369365248:0:ac16be42e609a57f48d1e46b939b3a07', '181528713:-1438656072494276861:0:3aad2f2efb170daa48d1e46b939b3a07', '181528713:8293855970983485187:0:5d2c05da65fa31a248d1e46b939b3a07', '181528713:-149518542996758784:0:9c1ea39ed5ebd9b948d1e46b939b3a07', '181528713:-4275100878987714816:0:abcd57d7f369342c48d1e46b939b3a07']
HASHTPAR_IDS = ['181528713:-2706134723315818751:0:f279527a75b20a8448d1e46b939b3a07', '181528713:-6807655666948301056:0:fa4b92e488ae3d0f48d1e46b939b3a07', '181528713:-1561220768909549824:0:92b85c60a80a644548d1e46b939b3a07', '181528713:-8987980156348260606:0:df60678f02a1110348d1e46b939b3a07', '181528713:5629063968022667011:0:ec74418c375a2eea48d1e46b939b3a07', '181528713:-7917715187329720575:0:2917cc8f27a08b8b48d1e46b939b3a07', '181528713:118367415512342274:0:de897ff28fde992d48d1e46b939b3a07', '181528713:-6152629478107177213:0:cb3b374df781b8d648d1e46b939b3a07', '181528713:-6500047426357813504:0:1a098387e9ae6e5048d1e46b939b3a07', '181528713:3666764036614135553:0:2e8caa25d9c32ddc48d1e46b939b3a07', '181528713:-8512770284441035007:0:c1d6b5cfe7c5268e48d1e46b939b3a07']
LOZI_IDS = ['181528713:-2304635161169289470:0:a208bd43e887d26248d1e46b939b3a07', '181528713:-1024262276109820158:0:2f8503fef507923748d1e46b939b3a07', '181528713:-7616151961720578301:0:1b6b2cff0f96b21f48d1e46b939b3a07']
SANGANTIK_IDS = ['181528713:4592963488385343233:0:919cb47ed65f4b6b48d1e46b939b3a07', '181528713:-528201902866686206:0:e3e4119b49a6481b48d1e46b939b3a07', '181528713:1579190637460594434:0:620054133bbe1f9248d1e46b939b3a07']
TERMOFOAM_IDS = ['181528713:-1982896307895984383:0:057d3baff7ecfbb448d1e46b939b3a07', '181528713:8492903830393331458:0:e7bb543f8f02b51248d1e46b939b3a07', '181528713:-4316815333157167357:0:91583cae231774f948d1e46b939b3a07', '181528713:2847725497301409536:0:3f4a0ff84d78ee6d48d1e46b939b3a07', '181528713:106266746842914560:0:427f8c0dd4a547fa48d1e46b939b3a07']
TARHBETON_IDS = ['181528713:-5661211372930982141:0:868eae743033ef4148d1e46b939b3a07', '181528713:-6600655671499546879:0:f0f117102298e80648d1e46b939b3a07', '181528713:1297403719822548737:0:1f078875edc6112248d1e46b939b3a07', '181528713:-982601145137750270:0:510179119fe8e52648d1e46b939b3a07']
AJRANTIK_IDS = ['181528713:5139279663511052032:0:78f999a33ba377d148d1e46b939b3a07', '181528713:-6236291792911065341:0:feb52e9504f06e7748d1e46b939b3a07', '181528713:1502589646432837377:0:4f865d4149135d1c48d1e46b939b3a07']
AJRTAKHT_IDS = ['181528713:8428972734353317633:0:f2e49627524a714448d1e46b939b3a07', '181528713:2029918750214528770:0:5fad548b7b8fa0d248d1e46b939b3a07', '181528713:8447806431558639361:0:6bfa3770193dd3ad48d1e46b939b3a07', '181528713:-3791781659575967999:0:55d104a042e338a848d1e46b939b3a07', '181528713:-5494810067628122366:0:4b539d7f0881847a48d1e46b939b3a07']
CHAHARPAR_IDS = ['181528713:-1405792213190041855:0:0cb27fa42d08aafefa6b055f138b54ae3c7b7805ace94705', '181528713:-3849744956241666304:0:141dca8596008569fa6b055f138b54ae3c7b7805ace94705', '181528713:-7585320176711229693:0:2bacce0c765690ccfa6b055f138b54ae3c7b7805ace94705', '181528713:4208441476753661698:0:90db0509f640bf56fa6b055f138b54ae3c7b7805ace94705', '181528713:8297513454822891265:0:906f049b95ba3e22fa6b055f138b54ae3c7b7805ace94705', '181528713:4963150999500365568:0:feec48488e69d084fa6b055f138b54ae3c7b7805ace94705', '181528713:-361445798277865728:0:8a02cab71989709cfa6b055f138b54ae3c7b7805ace94705', '181528713:-3347220470157861117:0:10a756f261867a2cfa6b055f138b54ae3c7b7805ace94705', '181528713:3931289030962454275:0:e6b838ca3077fd07fa6b055f138b54ae3c7b7805ace94705']
AJRBAHMANI_IDS = ['181528713:6446424329124781826:0:820bb4c3885627e048d1e46b939b3a07', '181528713:5947256525417946882:0:a120100d436bddcf48d1e46b939b3a07', '181528713:-2442916190307148029:0:5f990ec5199cc55348d1e46b939b3a07', '181528713:6032868109459922688:0:760b19eaf25ed26b48d1e46b939b3a07', '181528713:2551798482272657155:0:f5600f3ac9aef10948d1e46b939b3a07', '181528713:-5742830945565335808:0:a757e02494ccb1a248d1e46b939b3a07', '181528713:1640506405123923713:0:0fca0fe7706b567b48d1e46b939b3a07', '181528713:7440036235314536192:0:28b5295263b3fff048d1e46b939b3a07', '181528713:-5683819085774184701:0:b2b23e1c9c20781e48d1e46b939b3a07']
AJRKLASIK_IDS = ['181528713:7698811229813415681:0:3aed7145b7d9044548d1e46b939b3a07', '181528713:8877832658839084802:0:66edf08fce984dc448d1e46b939b3a07', '181528713:988645911329971969:0:7d2c9566f4205a4e48d1e46b939b3a07', '181528713:2920981420811886337:0:d447a41bfbce94e248d1e46b939b3a07', '181528713:1817568857063628545:0:27369ba1a92e5af348d1e46b939b3a07', '181528713:-4043727497327141120:0:e319fbc48d06916948d1e46b939b3a07', '181528713:1382662084538670849:0:93bc2492caef074b48d1e46b939b3a07', '181528713:2859829607966908160:0:9822eb6f37db64f448d1e46b939b3a07', '181528713:-2523735763617177856:0:74faa97ce7ac304a48d1e46b939b3a07', '181528713:1778813854641364737:0:d17f72d28dbab54348d1e46b939b3a07', '181528713:-5225907149776871678:0:d229ddf07aba3f9948d1e46b939b3a07']

ROLI_IDS = ['181528713:2277605811037675264:0:3923e9d015e3830048d1e46b939b3a07', '181528713:-3120241250404196608:0:91fc9a4b76362f5f48d1e46b939b3a07', '181528713:-5970157200608452864:0:6469c766ffad4af448d1e46b939b3a07', '181528713:-496707899798315261:0:9f6358fbcab75b9848d1e46b939b3a07', '181528713:50728513325637378:0:fb7c5ae97748463f48d1e46b939b3a07', '181528713:-4121018440910692606:0:90010d1993128a5448d1e46b939b3a07', '181528713:-3977163342781538558:0:e601b9b8a02f7ebd48d1e46b939b3a07', '181528713:2239465123522289409:0:4fc809404d08a83048d1e46b939b3a07', '181528713:6029700853335858947:0:0f898371abf151ab48d1e46b939b3a07', '181528713:2664301585857453827:0:9a1c8eef5d0a0ab848d1e46b939b3a07', '181528713:-2728677194070745344:0:2cb03a2f984fdb4348d1e46b939b3a07']
SANG_IDS = ['181528713:-3088832492519809279:0:66ea02aefd12ea7048d1e46b939b3a07', '181528713:-2791543480284995840:0:fab49a91fa48d62c48d1e46b939b3a07', '181528713:-3253093671585571071:0:6bc80f874d0f2ab048d1e46b939b3a07', '181528713:-3310541895511957758:0:3b78860ef38c5ede48d1e46b939b3a07', '181528713:-4038912801334288637:0:df0ca75c22c24a9c48d1e46b939b3a07', '181528713:7843175267465240323:0:937e9b106cff103b48d1e46b939b3a07', '181528713:4685155729057390336:0:4405a81774a3407848d1e46b939b3a07', '181528713:4961638188830170882:0:62c8939531a442bd48d1e46b939b3a07', '181528713:-3601367084425666814:0:6b1c708ad9d41f0748d1e46b939b3a07', '181528713:4809484807673683713:0:e8e993f40a76e17d48d1e46b939b3a07', '181528713:-742464589321003261:0:aee9268b5d70c62c48d1e46b939b3a07']
PARQUET_IDS = ['181528713:-6995466618114203902:1:3c6de7e1921ff4a36a6a136ed1f145293efd9f00f41af509ea130887ea03757f7759857a58f1df7851af907ceccb70d8f0f1ab81c812a7688211e6c76420e4b7', '181528713:8940626534975217408:1:3c6de7e1921ff4a36a6a136ed1f145293efd9f00f41af509307ab5ed55cd03ff7759857a58f1df7851af907ceccb70d8f0f1ab81c812a7688211e6c76420e4b7', '181528713:1836957141952765696:1:3c6de7e1921ff4a36a6a136ed1f145293efd9f00f41af5092808f37a0372c1e77759857a58f1df7851af907ceccb70d8f0f1ab81c812a7688211e6c76420e4b7', '181528713:7729316696326020865:1:3c6de7e1921ff4a36a6a136ed1f145293efd9f00f41af50925593e414ee291cc7759857a58f1df7851af907ceccb70d8f0f1ab81c812a7688211e6c76420e4b7', '181528713:-6799239181579444478:1:3c6de7e1921ff4a36a6a136ed1f145293efd9f00f41af509b80a9581642016127759857a58f1df7851af907ceccb70d8f0f1ab81c812a7688211e6c76420e4b7', '181528713:-6046639874538660096:1:3c6de7e1921ff4a36a6a136ed1f145293efd9f00f41af5095b99a84a223ac4e47759857a58f1df7851af907ceccb70d8f0f1ab81c812a7688211e6c76420e4b7', '181528713:-4756493050489528576:1:3c6de7e1921ff4a36a6a136ed1f145293efd9f00f41af5090a607527b20742657759857a58f1df7851af907ceccb70d8f0f1ab81c812a7688211e6c76420e4b7', '181528713:-2666260111889916159:1:3c6de7e1921ff4a36a6a136ed1f145293efd9f00f41af509cf21cdd0159e228f7759857a58f1df7851af907ceccb70d8f0f1ab81c812a7688211e6c76420e4b7', '181528713:-4177520130533089533:1:3c6de7e1921ff4a36a6a136ed1f145293efd9f00f41af509ae0bcd99364a26317759857a58f1df7851af907ceccb70d8f0f1ab81c812a7688211e6c76420e4b7', '181528713:1966841039034195712:1:3c6de7e1921ff4a36a6a136ed1f145293efd9f00f41af50955bcc6177da9d5207759857a58f1df7851af907ceccb70d8f0f1ab81c812a7688211e6c76420e4b7', '181528713:-2228990852470202623:1:3c6de7e1921ff4a36a6a136ed1f145293efd9f00f41af50928d12a1ac2279b827759857a58f1df7851af907ceccb70d8f0f1ab81c812a7688211e6c76420e4b7', '181528713:1663116816725188355:1:3c6de7e1921ff4a36a6a136ed1f145293efd9f00f41af5098e6eafe34615f8ad7759857a58f1df7851af907ceccb70d8f0f1ab81c812a7688211e6c76420e4b7']
QARNIZ_IDS = ['181528713:-6767833320078106877:0:5a9445d11fb3086a48d1e46b939b3a07', '181528713:-8620548539406475519:0:480af727188bf37e48d1e46b939b3a07', '181528713:7825047112868568835:0:e84b1c37504aad8f48d1e46b939b3a07', '181528713:-220156065819189501:0:eb53fbf6261fcd7448d1e46b939b3a07', '181528713:3123272799232597762:0:7fc516f4ea5cc79e48d1e46b939b3a07', '181528713:9048478242171657984:0:8cc0bf1379d4067648d1e46b939b3a07', '181528713:2531792540979240707:0:fcd70a9f4e9f5a2c48d1e46b939b3a07']

CAPTION_FOAM_7777 = "📐 ابعاد: ۷۰ × ۷۷ سانتی‌متر\n💰 قیمت: ۳۸۰,۰۰۰ تومان\n\n📞 ثبت سفارش:\n@divar_posh"
CAPTION_FOAM_7070 = "📐 ابعاد: ۷۰ × ۷۰ سانتی‌متر\n💰 قیمت: ۳۸۰,۰۰۰ تومان\n\n📞 ثبت سفارش:\n@divar_posh"
CAPTION_ROLI = "🌀 *دیوارپوش فومی رولی*\n\n📐 ابعاد: ۷۰ × ۲۸۰ سانتی‌متر\n💰 قیمت: ۱,۰۰۰,۰۰۰ تومان\n\n📞 ثبت سفارش:\n@divar_posh"
CAPTION_SANG = "🪨 *کفپوش طرح سنگ*\n\n📐 ابعاد: ۶۰ × ۶۰ سانتی‌متر\n💰 قیمت تایلی: ۳۷۰,۰۰۰ تومان\n\n📞 ثبت سفارش:\n@divar_posh"
CAPTION_PARQUET_NEW = "🌲 *کفپوش طرح پارکت*\n\n📐 هر کارتن: ۳ متر و ۶۰ سانت (تایل ۲۰×۱۲۰)\n💰 قیمت هر کارتن: ۳,۹۶۰,۰۰۰ تومان\n\n📞 ثبت سفارش:\n@divar_posh"
CAPTION_QARNIZ = "📏 *قرنیز*\n\n📐 ابعاد: ۹ سانت × ۳ متر\n💰 قیمت شاخه‌ای: ۲۶۰,۰۰۰ تومان\n\n📞 ثبت سفارش:\n@divar_posh"


MARBLE_G1 = ['2054771725:-1275542834963013888:1:d71a0507c98b48f3923c77614b4757d236988f50bb2937f2', '2054771725:9172055987987750657:1:d71a0507c98b48f3923c77614b4757d28f02bbefa4f7dbe1', '2054771725:-4086072726375489791:1:d71a0507c98b48f3923c77614b4757d28227bd0edab10e83', '2054771725:5934182262166265602:1:d71a0507c98b48f34673a348ec3d7408e4a8ab514a344a95', '2054771725:504405399466876672:1:d71a0507c98b48f3923c77614b4757d29b8ccace61877985', '2054771725:-4409069751647592704:1:d71a0507c98b48f34673a348ec3d740896b8b8cd309c174c', '2054771725:1262058431941582592:1:d71a0507c98b48f3923c77614b4757d2c961bc4b72de8bf2', '2054771725:-4423171849971687678:1:d71a0507c98b48f3923c77614b4757d2a30b8aafa629672a', '2054771725:-3849136685987586301:1:d71a0507c98b48f34673a348ec3d74082a0b639ee8a93a48', '181528713:-4699672401949090047:0:78f2b553deff5da948d1e46b939b3a07', '181528713:4621913676549136130:0:ad4a0e4e27f49ef148d1e46b939b3a07']
MARBLE_G2 = ['181528713:-1019861749952930045:1:d71a0507c98b48f34673a348ec3d740842da7c34ba59788e', '181528713:-1134915341008298240:1:d71a0507c98b48f34673a348ec3d740885f455ce530bbd17', '181528713:-4509640862970994944:1:d71a0507c98b48f3923c77614b4757d24a78071226052d58', '181528713:1203835600857931522:1:d71a0507c98b48f34673a348ec3d74085e130f71ce7a9f6e', '181528713:1926717488835272450:1:d71a0507c98b48f3923c77614b4757d216d4ca243d873e27', '181528713:973101849239494403:1:d71a0507c98b48f3923c77614b4757d2f65ded7c20fee4df', '181528713:-5629160587719139581:1:d71a0507c98b48f3923c77614b4757d287b04ffad662ace0', '181528713:-5143661295671501056:1:d71a0507c98b48f3923c77614b4757d2fc798c0a4858cae3', '181528713:6038054375679139586:1:d71a0507c98b48f34673a348ec3d7408a7576c3cad646da8', '181528713:7622258543891062528:1:d71a0507c98b48f3923c77614b4757d28c7737cfdcc4cace', '181528713:-8679236419997458687:1:d71a0507c98b48f3923c77614b4757d2a7576c3cad646da8', '181528713:5325558911563210497:1:d71a0507c98b48f34673a348ec3d74086041127ca7d9100e', '181528713:-5842255665774321919:1:d71a0507c98b48f3923c77614b4757d2dc84f3cd8a1d2a49', '181528713:7662708590433869570:1:d71a0507c98b48f3923c77614b4757d2ec6acd87b90585fa', '181528713:4437322869773770496:1:d71a0507c98b48f3923c77614b4757d283e5a9f9a4d07341', '181528713:386798711418003203:1:d71a0507c98b48f3923c77614b4757d2c92c400565e84814', '181528713:5626857407666986754:0:b2ba7bdf54b7ca4248d1e46b939b3a07']
MARBLE_G3 = ['181528713:-6459640778087457023:1:d71a0507c98b48f34673a348ec3d7408676f126eb1b82d65', '181528713:-2076380550997729534:1:d71a0507c98b48f3923c77614b4757d250ba4b363a5975a8', '181528713:7128713802385923840:1:d71a0507c98b48f3923c77614b4757d2ff31b1ab5d361b36', '181528713:5494117150043086593:1:d71a0507c98b48f3923c77614b4757d2c5b8aadf07854687', '181528713:-4526877505499619584:1:d71a0507c98b48f34673a348ec3d7408d651bb57b49156f8', '181528713:-4133462982753771775:1:d71a0507c98b48f3923c77614b4757d21c38ced0dcb4e327', '181528713:-8905184238499455232:1:d71a0507c98b48f34673a348ec3d7408d628a48826410c84', '181528713:4573165092645314304:0:dba2c91e67a16e2848d1e46b939b3a07', '181528713:3314546584662515457:0:50c467a014c289ee48d1e46b939b3a07', '181528713:-3392470167227982079:0:baec927815eb1c2d48d1e46b939b3a07', '181528713:8159048754939895552:0:51394fa7e3fbfda848d1e46b939b3a07', '181528713:6514573642594066179:0:7cad253250b0b87b48d1e46b939b3a07', '181528713:8898444379717443330:0:8fb72611c1bb7f3848d1e46b939b3a07', '181528713:-6963610273050779901:0:e360ff09171f2f8d48d1e46b939b3a07', '181528713:-510137030642622718:0:78787e7bbee1489848d1e46b939b3a07', '181528713:117558542154931969:0:ac42b4cf761a909448d1e46b939b3a07', '181528713:8459110019446742787:0:6c65b277bbed5c6d48d1e46b939b3a07']

MARBLE_LINK_6090 = "https://vestadeccor.com/product-category/wallcovering/marblesheet-wallcovering/"
MARBLE_LINK_120280 = "https://vestadeccor.com/product-category/wallcovering/marblesheet-wallcovering122280/"

CAPTION_MARBLE_G1 = (f"🪨 *ماربل شیت*\n\n"
    f"📐 سایز ۶۰×۱۲۰: ۸۵۰,۰۰۰ تومان/ورق\n"
    f"📐 سایز ۱۲۰×۲۸۰: ۳,۳۵۰,۰۰۰ تومان/ورق\n\n"
    f"🛒 خرید ۶۰×۱۲۰:\n{MARBLE_LINK_6090}\n"
    f"🛒 خرید ۱۲۰×۲۸۰:\n{MARBLE_LINK_120280}\n\n"
    f"📞 ثبت سفارش:\n@divar_posh")

CAPTION_MARBLE_G2 = (f"🪨 *ماربل شیت*\n\n"
    f"📐 سایز ۶۰×۱۲۰: ۷۲۰,۰۰۰ تومان/ورق\n"
    f"📐 سایز ۱۲۰×۲۸۰: ۳,۱۰۰,۰۰۰ تومان/ورق\n\n"
    f"🛒 خرید ۶۰×۱۲۰:\n{MARBLE_LINK_6090}\n"
    f"🛒 خرید ۱۲۰×۲۸۰:\n{MARBLE_LINK_120280}\n\n"
    f"📞 ثبت سفارش:\n@divar_posh")

CAPTION_MARBLE_G3 = (f"🪨 *ماربل شیت*\n\n"
    f"📐 سایز ۶۰×۱۲۰: ۷۰۰,۰۰۰ تومان/ورق\n"
    f"📐 سایز ۱۲۰×۲۸۰: ۳,۰۰۰,۰۰۰ تومان/ورق\n\n"
    f"🛒 خرید ۶۰×۱۲۰:\n{MARBLE_LINK_6090}\n"
    f"🛒 خرید ۱۲۰×۲۸۰:\n{MARBLE_LINK_120280}\n\n"
    f"📞 ثبت سفارش:\n@divar_posh")

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

FOAM_IDS_MAP = {
    "🟫 آجر بهمنی": (AJRBAHMANI_IDS, CAPTION_FOAM_7777),
    "🟧 آجر کلاسیک": (AJRKLASIK_IDS, CAPTION_FOAM_7777),
    "⬛ آجر تخت": (AJRTAKHT_IDS, CAPTION_FOAM_7070),
    "🔶 چهار پر": (CHAHARPAR_IDS, CAPTION_FOAM_7070),
    "🩶 طرح بتن": (TARHBETON_IDS, CAPTION_FOAM_7070),
    "🏛 آجر آنتیک": (AJRANTIK_IDS, CAPTION_FOAM_7070),
    "🪨 سنگ آنتیک": (SANGANTIK_IDS, CAPTION_FOAM_7070),
    "🌿 ترمو فوم": (TERMOFOAM_IDS, CAPTION_FOAM_7070),
    "🎋 بامبو": (BAMBOO_IDS, CAPTION_FOAM_7070),
    "💠 لوزی": (LOZI_IDS, CAPTION_FOAM_7070),
    "◼️ مربع": (SQUARE_IDS, CAPTION_FOAM_7070),
    "💎 کریستال": (CRYSTAL_IDS, CAPTION_FOAM_7070),
    "✨ هشت پر": (HASHTPAR_IDS, CAPTION_FOAM_7070),
}

@bot.message_handler(func=lambda m: m.text in FOAM_PRODUCTS)
def foam_product(message):
    ids, caption = FOAM_IDS_MAP[message.text]
    full_caption = f"{message.text} 🏷\n\n{caption}"
    send_photos(message.chat.id, ids, full_caption, foam_kb())

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
@bot.message_handler(func=lambda m: m.text == "🌲 طرح پارکت")
def floor_parquet(message):
    send_photos(message.chat.id, PARQUET_IDS, CAPTION_PARQUET_NEW, floor_kb())

@bot.message_handler(func=lambda m: m.text == "🪨 طرح سنگ")
def floor_sang(message):
    send_photos(message.chat.id, SANG_IDS, CAPTION_SANG, floor_kb())

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
