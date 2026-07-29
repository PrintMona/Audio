import os
import cohere
from dotenv import load_dotenv

# تحميل متغيرات البيئة من ملف .env
load_dotenv()

# قراءة مفتاح Cohere
api_key = os.getenv("COHERE_API_KEY")

if not api_key:
    print("Error: COHERE_API_KEY not found in .env file")
    exit()

# إنشاء عميل Cohere
co = cohere.Client(api_key)

# إدخال رسالة من المستخدم
user_text = input("Enter your message: ")

try:
    # إرسال الرسالة إلى Cohere
    response = co.chat(
        model="command-a-03-2025",
        message=user_text
    )

    print("\nAI Response:")
    print(response.text)

except Exception as e:
    print("\nError:")
    print(e)
    