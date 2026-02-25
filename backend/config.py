import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_API_KEY:
    print("DEBUG: OPENAI_API_KEY Loaded")
else:
    print("DEBUG: OPENAI_API_KEY NOT FOUND - please set in .env")

client = OpenAI()
MODEL = "qwen/qwen3-next-80b-a3b-instruct"


# import os
# from openai import OpenAI

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# if not OPENAI_API_KEY:
#     raise RuntimeError("OPENAI_API_KEY is not set")

# client = OpenAI(api_key=OPENAI_API_KEY)

# MODEL = "qwen/qwen3-next-80b-a3b-instruct"
