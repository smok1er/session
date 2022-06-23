import env
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = Client(
    "bot",
    api_id=env.API_ID,
    api_hash=env.API_HASH,
    bot_token=env.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="BJ_Jbot"),
)


if __name__ == "__main__":
    print("ابداء تشغيل البوت")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("ايبي هاش وال ايدي غير صحيحاين.")
    except AccessTokenInvalid:
        raise Exception("توكن بوت غير صحيح.")
    uname = app.get_me().username
    print(f"@{uname} يعمل الان!")
    idle()
    app.stop()
    print("توقف البوت!")
