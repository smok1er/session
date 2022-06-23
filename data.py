from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("⚙ ابدا استخراج الجلسة ⚙", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 العودة للبداية 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("👨‍💻 المالك 👨‍💻", url="https://t.me/n_n_v")],
        [
            InlineKeyboardButton("❔ كيفية الاستخدام ❔", callback_data="المساعدة"),
            InlineKeyboardButton("ℹ نشط ℹ", callback_data="نشط")
        ],
    ]

    START = """
يمرحبا {}

مرحبا بك في {}

استخدم هذا الروبوت فقط إذا كنت تثق في هذا الروبوت ، أو احذف هذه الدردشة ولا تستخدمه.

 أنا روبوت منشئ سلسلة الجلسة لـ Pyrogram & Telethon.
 انقر فوق الأزرار أدناه لمعرفة المزيد.
    """

    HELP = """
🔥 **الأوامر المتاحة** 🔥

`/about` - حول هذا البوت.
`/help` - يعرض الك للمساعدة.
`/start` - ابداء.
`/generate` - انشاء جلسة.
`/cancel` - قم بإلغاء العملية.
`/restart` - اعد تشغيل من جديد.
"""

    ABOUT = """
🔥 **حول هذا البوت** 🔥

**اللنشاء جلسة بايروكرام وجلسة تيرمكس.**

**Framework** : [بايروكرام](https://docs.pyrogram.org)

**Language** : [جيبثون](https://www.python.org)
    """
