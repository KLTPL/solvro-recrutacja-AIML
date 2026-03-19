import argparse
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Streszczanie artykułów naukowych z AI"
    )

    parser.add_argument(
        "filepath", type=str, help="Ścieżka do pliku .txt który chcesz streścić"
    )

    return parser.parse_args()


def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Plik nie znaleziony {file_path}")
        return None


def summarize_text(file_content):
    print("Czytanie i analizowanie pliku")
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Podsumuj to: {file_content}"}],
    )
    return res.choices[0].message.content


def main():
    args = parse_args()

    file_content = read_file(args.filepath)

    if file_content:
        summary = summarize_text(file_content)
        print(summary)


if __name__ == "__main__":
    main()
