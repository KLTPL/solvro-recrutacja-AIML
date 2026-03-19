# Asystent Notatek Naukowych (KN Solvro rekrutacja do AI/ML)

Projekt rekrutacyjny do koła naukowego Solvro. Aplikacja CLI służąca do automatycznego streszczania artykułów naukowych przy użyciu LLM.

## O projekcie

Obecnie projekt znajduje się w fazie Minimum Viable Product (MVP). Aplikacja przyjmuje ścieżkę do pliku tekstowego jako argument z poziomu terminala, wykorzystuje *Context Engineering* do precyzyjnego instruowania modelu OpenAI (gpt-4o-mini) i zapisuje wynik w postaci podsumowania podzielonego na sekcje (problem, metody, wyniki, ograniczenia) do pliku wskazanego przy wywołaniu.

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

    **Podstawowe użycie** (zapisze wynik w domyślnym pliku `wynik.md`):

   ```bash
   python main.py samples/input_file.txt
   ```

   **Zapis do konkretnego pliku** (użyj flagi `-o` lub `--output`):

   ```bash
   python main.py samples/input_file.txt -o moja_notatka.md
   ```

   Aby zobaczyć panel pomocy, wpisz:

   ```bash
   python main.py -h
   ```

## Trade-offy

- **Brak obsługi PDF:** Obecnie MVP przyjmuje tylko czysty tekst (`.txt`).
- **Brak chunkingu:** Skrypt wysyła cały tekst naraz. Przy bardzo długich artykułach API odrzuci zapytanie.
- **Halucynacje modelu:** Mimo ustawienia niskiej temperatury i rygorystycznego System Promptu, modele LLM mogą sporadycznie przekręcić specyficzne terminy techniczne. Wynik zawsze wymaga weryfikacji przez człowieka.
- **Blokowanie terminala:** Skrypt działa synchronicznie. Przy dłuższych tekstach użytkownik musi czekać kilka sekund na odpowiedź zablokowanego terminala.
