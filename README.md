# Generator obrazu o zadanej entropii

Projekt zaliczeniowy na zajęcia z Algorytmów Heurystycznych. 
Algorytm, wyposażony w GUI, wykorzystuje algorytm ewolucyjny aby obliczyć wartości spełniające wymóg zadanej entropii a następnie wynik przedstawia w postaci obrazka.

## Algorytm - w skrócie - działa w następujący sposób:
- generuje wyniki wejściowe (losowanie z wagami)
- wybiera z nich według pewnego prawdopodobieństwa grupę rodziców
- dopóki wynik nie zostanie osiągnięty:
  - wybiera losowych 2 rodziców
  - tworzy z nich 2 dzieci
  - mutuje dzieci
  - ze zbioru 2 rodziców i 2 dzieci wybiera 2 najlepsze rozwiązania
  - podmienia oryginalnych rodziców wybranymi dwoma rozwiązaniami (więc jeśli dzieci były nieudane - nic się nie zmienia)
 
 W ten sposób grupa wyników cały czas staje się bardziej podobna do zadanej entropi, aż w końcu któryś z nich okaże się poprawną odpowiedzią.
 
## Instrukcja instalacji
  1. W pliku tekstowym req.txt znajdują się zależności niezbędne do uruchomienia programu.
  2. Można je zainstalować przez pip - `pip install -r req.txt` lub w przypadku dwóch pythonów `pip3 install -r req.txt`
  3. Po pomyślnym zainstalowaniu pakietów, program uruchamia się z pliku `run.py`

## Parametry wejściowe
  - Rozmiar rastra - pozwala określić wielkość rastra wynikowego, im większy tym większa złożoność obliczeniowa
  - Entropia - szukana wartość entropii Shannona
  - Klasy - ilość klas na rastrze wynikowym
  - Dokładność - precyzja, z jaką algorytm szuk rozwiązania, im mniejsza tym większa złożoność
  
  *W przypadku niemożliwości znalezienia pożądanego wyniku, po dłuższym czasie algorytm podaje najlepszy znaleziony wynik*
