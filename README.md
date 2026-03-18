# Asystent Notatek Naukowych (KN Solvro rekrutacja do AI/ML)

Projekt rekrutacyjny do koła naukowego. Aplikacja CLI służąca do automatycznego streszczania artykułów naukowych przy użyciu LLM.

## O projekcie

Obecnie projekt znajduje się w fazie Proof of Concept (PoC). Skrypt wczytuje przykładowy abstrakt pracy inżynierskiej z pliku, wysyła go do modelu OpenAI (gpt-4o-mini) i zwraca podsumowanie w terminalu.

## Uruchomienie lokalne

1. Sklonuj repozytorium i wejdź do folderu:

   ```bash
   git clone <link-do-twojego-repo>
   cd <nazwa-folderu>
   ```

2. Stwórz i aktywuj środowisko wirtualne:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Zainstaluj wymagane biblioteki:

   ```bash
   pip install openai python-dotenv
   ```

4. Skonfiguruj klucz API:
   - Stwórz plik `.env` w głównym folderze projektu.
   - Wklej do niego swój klucz OpenAI w formacie: `OPENAI_API_KEY=sk-twoj-klucz`

5. By zmienić dane wejściowe, edytuj plik `samples/input_file.txt`.

6. Uruchom skrypt:

   ```bash
   python main.py
   ```
