# Generator obrazku o zadanej entropii

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
 
