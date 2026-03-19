# Raport z realizacji zadania - Asystent Notatek Naukowych

## 1. Podejście do zadania

Projekt był robiony etapami. Zacząłem od weryfikacji pomysłu (PoC). Po zobaczeniu, że da się pobrać dane z pliku i wysłać je do modelu, rozubudowałem projekt do fazy MVP. Teraz program jest pełnoprawną aplikacją CLI, która rozwiązuje problem, z którym mogłaby się spotkać osoba ze środowiska PWr - analizy i streszczania długich abstraktów naukowych.

## 2. Najważniejsze decyzje techniczne (Trade-offy)

* **Odrzucenie LangChain/LangGraph:** Mimo że było to zaznaczone jako atut w treści zadania, dla moje MVP uzycie frameworka agentowego to byłby *overengineering*.
* **Architektura CLI i `argparse`:** Użyłem natywnej biblioteki `argparse`. Dzięki temu program działa jak pełnoprawne narzędzie terminalowe (flaga `--help` oraz opcjonalny argument do zapisu pliku wyjściowego `-o`).
* **Context Engineering i ograniczenie halucynacji:** Kluczem do sukcesu jest `System Prompt`. Wymusiłem rygorystyczny format wyjściowy (Markdown) oraz zabroniłem modelowi robienia niepotrzebnych wstępów czy innych ozdobników. Dodatkowo obniżyłem parametr `temperature` do 0.2, aby zmusić model do trzymania się faktów i zminimalizować ryzyko halucynacji.
* **Rozdzielenie logiki (SRP):** Kod podzielony na małe komponenty jest łatwiejszy w długoterminowym utrzymaniu.

## 3. Co AI zrobiło dobrze, a gdzie nie domagało?

**Mocne strony:**

* Model (gpt-4o-mini) bardzo dobrze radzi sobie z wyciąganiem sedna metodologii.
* Trzyma się narzuconego formatu Markdown.
* Dobrze identyfikuje "Ograniczenia" w badaniach, nawet jeśli są one ukryte w tekście.

**Słabe strony i problemy:**

* **Brak asynchroniczności:** Skypt działa synchronicznie, więc terminal się blokuje w oczekiwaniu na odpowiedź modelu. Gdyby trwało to długo user może mopyśleć, że program się zawiesił.
* **Utrata bardzo specyficznego kontekstu:** Przy bardzo specyficznym słownictwie isnieje ryzyko, że model mini może nie zrozumieć kontekstu i przekręcić prawdę.

## 4. Krótka ewaluacja na przykładach

Podczas testów używałem m\.in. abstraktów prac inżynierskich związanych z drukiem 3D (FDM).

* **Przykład 1 (Abstrakt o detekcji błędów druku z użyciem CNN):** Model bezbłędnie podzielił tekst. Zauważył, że problemem jest "nitkowanie", metodą są konwolucyjne sieci neuronowe (CNN), a głównym wynikiem skuteczność na poziomie 94%. Prawidłowo też wychwycił, że ograniczeniem systemu jest wrażliwość na światło.
* **Przykład 2:** Przeprowadziłem test na anglojęzycznym abstrakcie publikacji 'Attention Is All You Need'. AI bezbłędnie zidentyfikowało problem badawczy i automatycznie przetłumaczyło ustrukturyzowaną notatkę na język polski.

## 5. Kierunki dalszego rozwoju

Gdybym miał rozwijać to narzędzie poza fazę MVP, w pierwszej kolejności zaimplementowałbym **Model Context Protocol (MCP)**.

Przekształcenie jej w Serwer MCP pozwoliłoby na bezpośrednią integrację z nowoczesnymi agentami AI. Dzięki temu użytkownik nie musiałby opuszczać swojego środowiska pracy – agent AI mógłby natywnie wywoływać moją logikę streszczania jako zewnętrzne narzędzie.
