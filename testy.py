from algorytm import create_values_from_entropy

#DZIAŁA TYLKO DLA LAYERS RÓWNE 1 LUB 2
#Należy sie zastanowić jak szukać miejsc cięć podziałów w przypadku w którym jest więcej niż jeden podział
#(a więc nie dzielimy osi od 0 do layers/2 na dwie części, a na ich większą ilość)

result = create_values_from_entropy(0, 1)
result = create_values_from_entropy(1, 1) #nieprawdiłowy
result = create_values_from_entropy(0, 2) #nieprawdiłowy
result = create_values_from_entropy(100, 2) #nieprawdiłowy

result = create_values_from_entropy(1, 2)
result = create_values_from_entropy(0.6, 2)
result = create_values_from_entropy(0.99999, 2)
result = create_values_from_entropy(0.00001, 2)
result = create_values_from_entropy(0.15, 2)
result = create_values_from_entropy(0.1234, 2)