word = str(input("Digite uma palavra: "))
qntA = 0

for letterA in word:
    if letterA.upper() in "A":
        qntA = qntA + 1
print(f'A frase tem {qntA} letra(s) A(a)')