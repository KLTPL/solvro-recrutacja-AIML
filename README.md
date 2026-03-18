# Asystent Notatek Naukowych (KN Solvro rekrutacja do AI/ML)

Projekt rekrutacyjny do koła naukowego. Aplikacja CLI służąca do automatycznego streszczania artykułów naukowych przy użyciu LLM.

## O projekcie

Obecnie projekt znajduje się w fazie Minimum Viable Product (MVP). Aplikacja przyjmuje ścieżkę do pliku tekstowego jako argument z poziomu terminala, wysyła go do modelu OpenAI (gpt-4o-mini) i zwraca podsumowanie w terminalu.

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
   python main.py samples/input_file.txt
   ```

Aby zobaczyć panel pomocy, wpisz:

   ```bash
   python main.py -h
   ```
