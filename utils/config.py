from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI")
MONGO_URI_LOCAL = os.environ.get("MONGO_URI_LOCAL")
MONGO_URI_JC = os.environ.get("MONGO_URI_JC")

API_KEY_JC = os.environ.get("API_KEY_FB")
