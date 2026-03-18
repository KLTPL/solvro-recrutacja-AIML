from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

with open("samples/input_file.txt", "r", encoding="utf-8") as file:
    file_content = file.read()

res = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": f"Podsumuj to: {file_content}"}],
)

print(res.choices[0].message.content)
