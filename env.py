import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "").strip()
API_HASH = os.getenv("API_HASH", "").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "")

if not API_ID:
    print("لم يتم الثور على ايبي ايدي اخرج...")
    raise SystemExit
if not API_HASH:
    print("لم يتم العثور على ايبي هاش اخرج...")
    raise SystemExit
if not BOT_TOKEN:
    print("لم يتم العثور على بوت توكن اخرج...")
    raise SystemExit
if not DATABASE_URL:
    print("لم يتم العثور على قاعدة البينات...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("ايبي ايدي ليساَ صحيحاَ اخرج...")
    raise SystemExit

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
