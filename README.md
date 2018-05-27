Windows:

1. Ściągnąć i zainstalować Python 3 (np: 3.6.5)
https://www.python.org/downloads/

2. Ściągnąć Graphviz
https://graphviz.gitlab.io/_pages/Download/Download_windows.html w wersji .msi <br />
Zainstalować zgodnie z instalatorem

dodać ściężke(z zainstalowanym graphvizem) do PATH (C:\Program Files (x86)\Graphviz2.38\bin\dot.exe) w zmiennych środowiskowych systemu <br />
dodać ściężke(z zainstalowanym graphvizem) do PATH (C:\Program Files (x86)\Graphviz2.38\bin) w zmiennych środowiskowych użytkownika <br />

3. Zaintalować następujace moduły: <br />
W CMD wpisać: <br />
pip install Pillow <br />
pip install sympy <br />
pip install mpmath <br />

4. Dojść do ścieżki z folderem pobranym z githuba, wpisać: cwiczenie1.py 

5. Wpisać 1 w celu utworzenia kodu Huffmana  <br />
    a) podać ścieżkę do pliku tekstowego (np: test.txt) <br />
    b) podać ścieżkę/nazwę dla obrazu wyjściowego bez rozszerzenia(np: testGraphOutput) <br />
    c) podać ścieżkę/nazwę dla tekstu wyjściowego (np: testOutput.txt) <br />
    
6. Wpisać 2 w celu zdekodwania pliku tekstowego i utworzenia grafu <br />
    a) podać ściężkę do pliku tekstowego (np: testOutput.txt) <br />
    a) podać ściężkę do obrazu wyjściowego bez rozszerzenia (np: graphFinal) <br />

7. Wpisać 3 do wyjścia

8. Weryfikacja pliku testOutput.txt z graphFinal.png oraz testGrahpOutput.png
