# Projekt zaliczeniowy - program do obliczeń statystycznych
Skład grupy: Piotr Gołąb, Martyna Guzik
## Założenia projektu
1.  Użytkownik dodaje plik csv z danymi w postaci szeregu prostego, szeregu rozdzielczego prostego lub szeregu rozdzielczego przedziałowego. Na ich podstawie program oblicza podstawowe miary statystyki opisowej (średnia, mediana, kwartyle, odchylenie standardowe, współczynniki zmienności i asymetrii, skośność, kurtoza, rozstęp międzykwartylowy). Do  wyników podane są ich interpretacje. Program rysuje także histogram.
2.  Można także wczytać szereg prosty z pliku csv lub wpisując dane w odpowiednie pola. Program dokona wtedy obliczeń potrzebnych do stworzenia szeregu rozdzielczego prostego lub przedziałowego, stworzy tabelę z możliwością wyeksportowania jej w pliku csv oraz dokona obliczeń jak w punkcie 1).

Projekt został zrealizowany zgodnie z większością założeń. Nie udało się jedynie policzyć niektórych miar statystycznych oraz stworzyć histogram dla szeregów rozdzielczych. 
# Uruchomienie projektu
Do uruchomienia programu konieczne jest zainstalowanie zaimplementowanych w nim bibliotek.

    pip install tkinter

    pip install matplotlib
Po zainstalowaniu bibliotek, należy uruchomić program poprzez skrypt main.py znajdujący się w głównym folderze projektu.
## Przygotowanie danych

W programie możliwe jest importowanie danych z plików w formacie .csv. Struktura tych plików różni się w zależności od typu szeregu.

### Szereg prosty
To plik składający się jedynie z danych liczbowych oddzielonych znakami nowej linii.
||
|--|
| 1 | 
| 2 |
| 3 | 
| 4 |
| 5 | 
| 6 |
|...| 
### Szereg rozdzielczy prosty
W tym pliku muszą znajdować się także nagłówki tabeli.
| dane | liczebność |
|--|--|
| 2 | 6 |
| 3 | 7 |
| 3.5 | 7 |
| 4 | 5 |
| 4.5 | 2 |
| 5 | 1 |

![Przykładowe dane](https://i.imgur.com/CYbGAeF.png)
### Szereg rozdzielczy przedziałowy
Plik z podobną strukturą do szeregu rozdzielczego prostego. Ważne jest, aby przedziały były oznaczane za pomocą '-'.
| dane | liczebność |
|--|--|
| 18 - 24 | 125 |
| 24 - 30 | 118 |
| 30 - 36 | 94 |
| 36 - 42 | 89 |
| 42 - 48 | 76 |
| 48 - 54 | 21 |
| 54 - 60 | 47 |

![Przykładowe dane](https://i.imgur.com/vUY5HZW.png)

