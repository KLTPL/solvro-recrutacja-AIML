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
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="summary.md",
        help="Ścieżka do pliku .md z wynikiem",
    )
    return parser.parse_args()


def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Plik nie znaleziony {file_path}")
        return None


def save_to_file(content, file_path):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Zapisano podsumowanie do pliku {file_path}")
    except Exception as e:
        print(f"Nie udało się zapisać do pliku. Błąd: {e}")


def summarize_text(file_content):
    SYSTEM_PROMPT = """Jesteś doświadczonym asystentem naukowym pracującym na politechnice.
Twoim zadaniem jest analiza abstraktów artykułów naukowych i wyciąganie z nich kluczowych informacji.

Zwróć wynik w czystym formacie Markdown, używając DOKŁADNIE poniższej struktury:

## Główny problem badawczy
(Opisz w 1-2 zdaniach, jaki problem rozwiązują autorzy)

## Zaproponowana metoda
(Wymień w krótkich punktach użyte technologie/metody)

## Najważniejsze wyniki
(Wymień w punktach główne osiągnięcia i metryki, jeśli są podane)

## Ograniczenia
(Jeśli autorzy wspominają o wadach/ograniczeniach, opisz je. Jeśli nie, napisz "Brak danych")

ZASADY:
1. Pisz zwięźle, akademickim stylem.
2. Zwróć TYLKO kod Markdown. Nie dodawaj żadnych wstępów (np. "Oto podsumowanie") ani zakończeń.
3. Opieraj się WYŁĄCZNIE na dostarczonym tekście. Nie zmyślaj informacji (zero halucynacji)."""
    print("Czytanie i analizowanie pliku")
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": file_content},
        ],
        temperature=0.2,
    )
    return res.choices[0].message.content


def main():
    args = parse_args()

    file_content = read_file(args.filepath)

    if file_content:
        summary = summarize_text(file_content)

        print("---ODPOWIEDŹ AI---")
        print(summary)
        print("-------------")

        save_to_file(summary, args.output)


if __name__ == "__main__":
    main()
