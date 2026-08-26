from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
import sys

load_dotenv()

model = ChatMistralAI(model="mistral-small-2506")

response = model.invoke("hi")

#emojis ko handle krne ke liye h

sys.stdout.reconfigure(encoding="utf-8")

print(response.content)