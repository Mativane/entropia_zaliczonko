import numpy as np

def calculate_entropy(dane):
    entropia = sum(np.negative(dane) * np.log2(dane))
    return entropia

def create_values_from_entropy(entropy, layers):
    #Obsługa dziwnych parametrów wejściowych oraz przypadku gdzie layers == 1:
    if entropy > layers / 2 or entropy < 0:
        print("Wartość niemożliwa do osiąnięcia")
        return None
    if layers == 1 and entropy != 0:
        print("Wartość niemożliwa do osiąnięcia")
        return None
    if round(layers) != layers:
        print("Argument layers musi być liczbą całkowitą")
        return None
    if layers == 1:
        values = np.asarray([1])
        print("Udało się! Rozkład procentowy to: " + str(values))
        return values
    if entropy == 0:
        print("Wartość niemożliwa do osiąnięcia")
        return None
    

    avg_value = layers / 4
    values = [avg_value] * layers #Robimy cięcie na środku możliwego przedziału (w przypadku layers=2 jest to 0,25 X 0,75)
    min_cut = 0 #Minimalne miejsce cięcia między dwoma values 
    max_cut = layers / 2 #Maksymalne miejsce cięcia między dwoma values
    #Nadpisując min_cut i max_cut zawężamy możliwy przedział wartości w którym występuje cięcię między liczebnością dwóch values
    
    #Przykład: zaczyna od podziału w 0,25 - czyli 0,25x0,75(1/4 obrazka na kolor1, 3/4 na kolor2)
    #Uznaje że entropia jest za duża, czyli cięcie w 0,25 na osi jest za wysoko
    #Czyli wiemy już że podział musi znajdować się w granicach 0 - 0,25 (Przyjmujemy je jako nowe min_cut i max_cut)
    #Próbujemy trafić w środek z podziałem, czyli dajemy 0,125 - czyli 0,125 obrazka to kolor1 a 0,675 obrazka to kolor2
    #Teraz entropia wyszła nam za mała. Czyli miejsce cięcia musi być pomiędzy 0,125 a 0,25 (Przyjmujemy je jako nowe min_cut i max_cut)
    #Podejmujemy kolejną próbę, i tak dalej, aż nie trafimy. Zajmuje to zwykle kilkanaście prób
    i = 0
    while True:
        i+=1
        entropy_guess = calculate_entropy(values)
        if round(entropy_guess,4) == round(entropy,4):
            print("Udało się! Rozkład procentowy to: " + str(values) + ". Zajęło to " + str(i) + " iteracji")
            return (values)
        else:
            current_cut = values[0]
            if entropy_guess > entropy:
                max_cut = current_cut
            else: 
                min_cut = current_cut
            values[0] = min_cut + ((max_cut - min_cut) / 2)
            values[len(values)-1] = 1 - values[0]


